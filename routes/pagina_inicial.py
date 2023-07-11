# pagina_inicial

from flask import Blueprint, render_template, redirect, url_for, session
from routes.base import get_db_connection

pagina_inicial_bp = Blueprint('pagina_inicial', __name__)

@pagina_inicial_bp.route('/pagina_inicial')
def pagina_inicial():
    if 'cpf' not in session:
        return redirect(url_for('login.login'))

    cpf = session['cpf']
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT CPF, Cargo, NivelOrganizacional, Nome, Email, Celular, DATE_FORMAT(DataNascimento, '%d/%m/%Y') AS DataNascimento, DATE_FORMAT(DataIngresso, '%d/%m/%Y') AS DataIngresso FROM usuarios WHERE CPF = %s"
    cursor.execute(query, (cpf,))
    usuario = cursor.fetchone()

    conn.close()

    return render_template('pagina_inicial.html', usuario=usuario)

