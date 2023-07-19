# app.py

from flask import Flask, g
import mysql.connector

app = Flask(__name__)
with open('app.secret_key.txt', 'r') as f:
    app.secret_key = f.read().strip()

# Configurações do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Hinata@82',
    'database': 'cas_gss'
}

# Função para obter a conexão com o banco de dados
def get_db_connection():
    if 'db_connection' not in g:
        g.db_connection = mysql.connector.connect(**db_config)
    return g.db_connection

# Registro dos blueprints
from routes.calculadora_cancelamento import calculadora_cancelamento_bp
from routes.gerar_cancelamento_pdf import gerar_cancelamento_pdf_bp
from routes.editar_usuarios import editar_usuarios_bp
from routes.index import index_bp
from routes.login import login_bp
from routes.logout import logout_bp
from routes.pagina_inicial import pagina_inicial_bp
from routes.primeiro_acesso import primeiro_acesso_bp
from routes.usuarios import usuarios_bp
from routes.adicionar_usuario import adicionar_usuario_bp
from routes.caixa import caixa_bp
from routes.buscar_usuarios import buscar_usuarios_bp
from routes.metas_bonificacoes import metas_bonificacoes_bp
from routes.calculadora_gerente import calculadora_gerente_bp
from routes.calculadora_plena import calculadora_plena_bp
from routes.calculadora_subgerente import calculadora_subgerente_bp
from routes.calculadora_consultora import calculadora_consultora_bp
from routes.calculadora_consultora_avaliacao import calculadora_consultora_avaliacao_bp
from routes.calculadora_especialista import calculadora_especialista_bp

app.register_blueprint(calculadora_cancelamento_bp, url_prefix='/calculadora_cancelamento')
app.register_blueprint(gerar_cancelamento_pdf_bp)
app.register_blueprint(editar_usuarios_bp)
app.register_blueprint(index_bp)
app.register_blueprint(login_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(pagina_inicial_bp)
app.register_blueprint(primeiro_acesso_bp)
app.register_blueprint(usuarios_bp)
app.register_blueprint(adicionar_usuario_bp)
app.register_blueprint(caixa_bp)
app.register_blueprint(buscar_usuarios_bp, name='buscar_usuarios')
app.register_blueprint(metas_bonificacoes_bp)
app.register_blueprint(calculadora_gerente_bp)
app.register_blueprint(calculadora_plena_bp)
app.register_blueprint(calculadora_subgerente_bp)
app.register_blueprint(calculadora_consultora_bp)
app.register_blueprint(calculadora_consultora_avaliacao_bp)
app.register_blueprint(calculadora_especialista_bp)

# Função para verificar o acesso às rotas protegidas
@app.before_request
def before_request():
    g.db_connection = get_db_connection()

    cursor = g.db_connection.cursor()
    query = "SELECT DISTINCT NivelAcesso FROM usuarios"
    cursor.execute(query)
    niveis_acesso = [result[0] for result in cursor.fetchall()]
    g.niveis_acesso = niveis_acesso

    cursor = g.db_connection.cursor()
    query = "SELECT DISTINCT NivelOrganizacional FROM usuarios"
    cursor.execute(query)
    niveis_organizacionais = [result[0] for result in cursor.fetchall()]
    g.niveis_organizacionais = niveis_organizacionais

# Execução do aplicativo Flask
if __name__ == '__main__':
    app.run()