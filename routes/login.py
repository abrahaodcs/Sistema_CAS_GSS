from flask import Blueprint, render_template, request, redirect, url_for, session
from routes.base import get_db_connection

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if 'cpf' in session:
        return redirect(url_for('pagina_inicial.pagina_inicial'))

    if request.method == 'POST':
        cpf = request.form['cpf']
        senha = request.form['senha']

        conn = get_db_connection()
        cursor = conn.cursor()
        query = "SELECT Senha, SenhaProvisoria, NivelAcesso, NivelOrganizacional FROM usuarios WHERE CPF = %s"
        cursor.execute(query, (cpf,))
        result = cursor.fetchone()

        if result:
            senha_normal = result[0]
            senha_provisoria = result[1]
            nivel_acesso = result[2]
            nivel_organizacional = result[3]

            if senha == senha_provisoria:
                session['cpf'] = cpf
                return redirect(url_for('primeiro_acesso.primeiro_acesso'))
            elif senha == senha_normal:
                session['cpf'] = cpf
                session['nivel_acesso'] = nivel_acesso
                session['nivel_organizacional'] = nivel_organizacional
                return redirect(url_for('index.index'))

    return render_template('login.html')
