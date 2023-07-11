from flask import Blueprint, render_template, redirect, url_for, request, session
from routes.base import get_db_connection
import string
import random

adicionar_usuario_bp = Blueprint('adicionar_usuario_bp', __name__)

@adicionar_usuario_bp.route('/adicionar_usuario', methods=['GET', 'POST'])
def adicionar_usuario():
    if 'cpf' not in session:
        return redirect(url_for('login_bp.login'))

    if request.method == 'POST':
        cpf = request.form['cpf']
        nivel_acesso = request.form['nivel-acesso']
        nivel_organizacional = request.form['nivel-organizacional']
        cargo = request.form['cargo']

        # Gerar senha provisória
        caracteres_permitidos = string.ascii_letters + string.digits
        senha_provisoria = ''.join(random.choice(caracteres_permitidos) for _ in range(8))

        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO usuarios (CPF, NivelAcesso, NivelOrganizacional, Cargo, SenhaProvisoria) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (cpf, nivel_acesso, nivel_organizacional, cargo, senha_provisoria))
        conn.commit()

        # Obter informações do usuário adicionado
        query = "SELECT CPF, SenhaProvisoria FROM usuarios WHERE CPF = %s LIMIT 1"
        cursor.execute(query, (cpf,))
        usuario = cursor.fetchone()

        # Fechar a conexão com o banco de dados
        cursor.close()
        conn.close()

        # Verificar se o usuário foi encontrado
        if usuario:
            cpf_usuario = usuario[0]
            senha_provisoria = usuario[1]

            # Limpar os campos do formulário
            cpf = ''
            nivel_acesso = ''
            nivel_organizacional = ''
            cargo = ''

            # Renderizar mensagem de resposta em HTML
            return render_template('adicionar_usuario.html', cpf_usuario=cpf_usuario, senha_provisoria=senha_provisoria)

    return render_template('adicionar_usuario.html')
