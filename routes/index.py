from flask import Blueprint, render_template

index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def index():
    # Lógica para a página inicial (index)
    return render_template('index.html')

@index_bp.route('/dashboard')
def dashboard():
    # Lógica para a página de painel de controle (dashboard)
    return render_template('dashboard.html')

@index_bp.route('/relatorios')
def relatorios():
    # Lógica para a página de relatórios
    return render_template('relatorios.html')
