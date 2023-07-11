from flask import Blueprint, render_template, redirect, url_for, request, session
from routes.base import get_db_connection

primeiro_acesso_bp = Blueprint('primeiro_acesso', __name__)

@primeiro_acesso_bp.route('/primeiro_acesso', methods=['GET', 'POST'])
def primeiro_acesso():
    if 'cpf' not in session:
        return redirect(url_for('login.login'))

    cpf = session['cpf']
    if request.method == 'POST':
        senha = request.form['senha']

        conn = get_db_connection()
        cursor = conn.cursor()
        query = "UPDATE usuarios SET Senha = %s, SenhaProvisoria = NULL WHERE CPF = %s"
        cursor.execute(query, (senha, cpf))
        conn.commit()
        conn.close()

        return redirect(url_for('index.index'))

    return render_template('primeiro_acesso.primeiro_acesso')
