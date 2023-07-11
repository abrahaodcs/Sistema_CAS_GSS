from flask import Blueprint, render_template, request
from routes.base import get_db_connection

metas_unidades_bp = Blueprint('metas_unidades', __name__)

@metas_unidades_bp.route('/metas_unidades', methods=['GET', 'POST'])
def metas_unidades():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        mes = request.form['mes']
        unidade = request.form['unidade']
        meta_mes = float(request.form['meta_mes'])
        super_mes = meta_mes - (meta_mes * 1.2)
        hiper_mes = meta_mes - (meta_mes * 1.44)

        # Inserir as metas no banco de dados
        query = "INSERT INTO metas_unidades (mes, unidade, meta_loja, super_loja, hiper_loja) VALUES (%s, %s, %s, %s, %s)"
        values = (mes, unidade, meta_mes, super_mes, hiper_mes)
        cursor.execute(query, values)
        conn.commit()

    # Buscar as unidades do banco de dados
    cursor.execute("SELECT unidade FROM unidades")
    unidades = [row[0] for row in cursor.fetchall()]

    cursor.close()
    conn.close()

    return render_template('metas_unidades.html', unidades=unidades)
