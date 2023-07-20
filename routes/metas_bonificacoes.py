# metas_bonificacoes.py

from flask import Blueprint, render_template, redirect, url_for, session
from routes.base import get_db_connection

metas_bonificacoes_bp = Blueprint('metas_bonificacoes', __name__)

@metas_bonificacoes_bp.route('/metas_bonificacoes')
def metas_bonificacoes():
    if 'cpf' not in session:
        return redirect(url_for('login.login'))

    cpf = session['cpf']
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT CPF, Cargo, NivelOrganizacional, Nome, Email, Celular, DATE_FORMAT(DataNascimento, '%%d/%%m/%%Y') AS DataNascimento, DATE_FORMAT(DataIngresso, '%%d/%%m/%%Y') AS DataIngresso FROM usuarios WHERE CPF = %s"
    cursor.execute(query, (cpf,))
    usuario = cursor.fetchone()

    conn.close()

    if not usuario:
        return "Usuário não encontrado"

    return render_template('metas_bonificacoes.html', usuario=usuario)
