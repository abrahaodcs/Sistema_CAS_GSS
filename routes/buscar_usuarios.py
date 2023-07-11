from flask import Blueprint, render_template
from routes.base import get_db_connection

buscar_usuarios_bp = Blueprint('buscar_usuarios_bp', __name__)

@buscar_usuarios_bp.route('/buscar_usuarios')
def buscar_usuarios():
    # Obtém a conexão com o banco de dados
    conn = get_db_connection()

    # Realiza a lógica para buscar usuários no banco de dados
    cursor = conn.cursor()
    query = "SELECT * FROM usuarios"
    cursor.execute(query)
    usuarios = cursor.fetchall()

    # Fecha a conexão com o banco de dados
    cursor.close()
    conn.close()

    # Retorna os usuários encontrados na renderização do template
    return render_template('buscar_usuarios.html', usuarios=usuarios)
