from flask import Blueprint, render_template

editar_usuarios_bp = Blueprint('editar_usuarios', __name__)

@editar_usuarios_bp.route('/editar_usuarios')
def editar_usuarios():
    # Lógica para exibir/editar usuários
    return render_template('editar_usuarios.html')
