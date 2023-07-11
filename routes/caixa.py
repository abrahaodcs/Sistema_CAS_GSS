# caixa.py

from flask import Blueprint, render_template, request, redirect, url_for, session, send_file
import datetime
from reportlab.pdfgen import canvas
from io import BytesIO
from decimal import Decimal
from routes.base import get_db_connection

caixa_bp = Blueprint('caixa', __name__)

@caixa_bp.route('/caixa', methods=['GET'])
def caixa():
    if 'cpf' not in session:
        return redirect(url_for('login.login'))
    data_sistema = datetime.date.today().strftime("%Y-%m-%d")
    nivel_organizacional = session.get('nivel_organizacional')
    cpf = session.get('cpf')
    nome = session.get('nome')
    return render_template('caixa.html', data_sistema=data_sistema, nivel_organizacional=nivel_organizacional, cpf_usuario=cpf, nome_usuario=nome)

@caixa_bp.route('/caixa/inserir_movimentacao', methods=['POST'])
def inserir_movimentacao():
    data = request.form['data_movimentacao']
    tipo_movimentacao = request.form['tipo_movimentacao']
    forma_pagamento = request.form['forma_pagamento']
    valor = float(request.form['valor'])
    cliente = request.form['cliente']
    contrato = request.form['contrato']
    observacao = request.form['observacao']

    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO caixa (data_insercao, unidade, cpf, nome, data, tipo_movimentacao, forma_pagamento, valor, cliente, contrato, observacao) VALUES (CURRENT_DATE(), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (session['nivel_organizacional'], session['cpf'], session['nome'], data, tipo_movimentacao, forma_pagamento, valor, cliente, contrato, observacao))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('caixa.caixa'))

@caixa_bp.route('/caixa/gerar_relatorio_diario', methods=['POST'])
def gerar_relatorio_diario():
    data_atual = datetime.date.today()
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT SUM(valor) FROM caixa WHERE unidade = %s AND data = %s"
    cursor.execute(query, (session['nivel_organizacional'], data_atual))
    total_movimentacao = cursor.fetchone()[0]

    query = "SELECT SUM(valor) FROM caixa WHERE unidade = %s AND data = %s AND tipo_movimentacao = 'Venda'"
    cursor.execute(query, (session['nivel_organizacional'], data_atual))
    total_venda = cursor.fetchone()[0]

    query = "SELECT SUM(valor) FROM caixa WHERE unidade = %s AND data = %s AND tipo_movimentacao = 'Regularização'"
    cursor.execute(query, (session['nivel_organizacional'], data_atual))
    total_regularizacao = cursor.fetchone()[0]

    query = "SELECT SUM(valor) FROM caixa WHERE unidade = %s AND data = %s AND forma_pagamento = 'Dinheiro'"
    cursor.execute(query, (session['nivel_organizacional'], data_atual))
    total_dinheiro = cursor.fetchone()[0]

    query = "SELECT SUM(valor) FROM caixa WHERE unidade = %s AND data = %s AND forma_pagamento = 'Pix'"
    cursor.execute(query, (session['nivel_organizacional'], data_atual))
    total_pix = cursor.fetchone()[0]

    query = "SELECT SUM(valor) FROM caixa WHERE unidade = %s AND data = %s AND forma_pagamento = 'Débito'"
    cursor.execute(query, (session['nivel_organizacional'], data_atual))
    total_debito = cursor.fetchone()[0]

    query = "SELECT SUM(valor) FROM caixa WHERE unidade = %s AND data = %s AND forma_pagamento = 'Crédito'"
    cursor.execute(query, (session['nivel_organizacional'], data_atual))
    total_credito = cursor.fetchone()[0]

    query = "SELECT SUM(valor) FROM caixa WHERE unidade = %s AND data = %s AND forma_pagamento = 'Recorrente'"
    cursor.execute(query, (session['nivel_organizacional'], data_atual))
    total_recorrente = cursor.fetchone()[0]

    query = "SELECT SUM(valor) FROM caixa WHERE unidade = %s AND data = %s AND forma_pagamento = 'Outros'"
    cursor.execute(query, (session['nivel_organizacional'], data_atual))
    total_outros = cursor.fetchone()[0]

    query = "SELECT nome, SUM(valor) FROM caixa WHERE unidade = %s AND data = %s GROUP BY nome"
    cursor.execute(query, (session['nivel_organizacional'], data_atual))
    usuarios = cursor.fetchall()

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)

    pdf.setFont("Helvetica", 14)
    pdf.drawString(50, 750, "Relatório diário caixa")

    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 700, f"Total de movimentação no dia: R$ {Decimal(total_movimentacao):,.2f}")
    pdf.drawString(50, 680, f"Total Venda: R$ {Decimal(total_venda):,.2f}")
    pdf.drawString(50, 660, f"Total Regularização: R$ {Decimal(total_regularizacao):,.2f}")
    pdf.drawString(50, 640, f"Total Dinheiro: R$ {Decimal(total_dinheiro):,.2f}")
    pdf.drawString(50, 620, f"Total Pix: R$ {Decimal(total_pix):,.2f}")
    pdf.drawString(50, 600, f"Total Débito: R$ {Decimal(total_debito):,.2f}")
    pdf.drawString(50, 580, f"Total Crédito: R$ {Decimal(total_credito):,.2f}")
    pdf.drawString(50, 560, f"Total Recorrente: R$ {Decimal(total_recorrente):,.2f}")
    pdf.drawString(50, 540, f"Total Outros: R$ {Decimal(total_outros):,.2f}")

    pdf.setFont("Helvetica", 10)
    pdf.drawString(50, 500, "Total recebido por cada usuário no mesmo dia da solicitação:")
    y = 480
    for usuario in usuarios:
        nome_usuario, total_usuario = usuario
        pdf.drawString(50, y, f"{nome_usuario}: R$ {Decimal(total_usuario):,.2f}")
        y -= 20

    pdf.showPage()
    pdf.save()

    buffer.seek(0)

    cursor.close()
    conn.close()

    return send_file(buffer, attachment_filename='relatorio_diario.pdf', as_attachment=True)


@caixa_bp.route('/caixa/gerar_relatorio_mensal', methods=['POST'])
def gerar_relatorio_mensal():
    data_atual = datetime.date.today()
    mes_atual = data_atual.month
    ano_atual = data_atual.year

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT SUM(valor) FROM caixa WHERE unidade = %s AND EXTRACT(MONTH FROM data) = %s AND EXTRACT(YEAR FROM data) = %s"
    cursor.execute(query, (session['nivel_organizacional'], mes_atual, ano_atual))
    total_movimentacao = cursor.fetchone()[0]

    query = "SELECT SUM(valor) FROM caixa WHERE unidade = %s AND EXTRACT(MONTH FROM data) = %s AND EXTRACT(YEAR FROM data) = %s AND tipo_movimentacao = 'Venda'"
    cursor.execute(query, (session['nivel_organizacional'], mes_atual, ano_atual))
    total_venda = cursor.fetchone()[0]

    query = "SELECT SUM(valor) FROM caixa WHERE unidade = %s AND EXTRACT(MONTH FROM data) = %s AND EXTRACT(YEAR FROM data) = %s AND tipo_movimentacao = 'Regularização'"
    cursor.execute(query, (session['nivel_organizacional'], mes_atual, ano_atual))
    total_regularizacao = cursor.fetchone()[0]

    query = "SELECT SUM(valor) FROM caixa WHERE unidade = %s AND EXTRACT(MONTH FROM data) = %s AND EXTRACT(YEAR FROM data) = %s AND forma_pagamento = 'Dinheiro'"
    cursor.execute(query, (session['nivel_organizacional'], mes_atual, ano_atual))
    total_dinheiro = cursor.fetchone()[0]

    query = "SELECT SUM(valor) FROM caixa WHERE unidade = %s AND EXTRACT(MONTH FROM data) = %s AND EXTRACT(YEAR FROM data) = %s AND forma_pagamento = 'Pix'"
    cursor.execute(query, (session['nivel_organizacional'], mes_atual, ano_atual))
    total_pix = cursor.fetchone()[0]

    query = "SELECT SUM(valor) FROM caixa WHERE unidade = %s AND EXTRACT(MONTH FROM data) = %s AND EXTRACT(YEAR FROM data) = %s AND forma_pagamento = 'Débito'"
    cursor.execute(query, (session['nivel_organizacional'], mes_atual, ano_atual))
    total_debito = cursor.fetchone()[0]

    query = "SELECT SUM(valor) FROM caixa WHERE unidade = %s AND EXTRACT(MONTH FROM data) = %s AND EXTRACT(YEAR FROM data) = %s AND forma_pagamento = 'Crédito'"
    cursor.execute(query, (session['nivel_organizacional'], mes_atual, ano_atual))
    total_credito = cursor.fetchone()[0]

    query = "SELECT SUM(valor) FROM caixa WHERE unidade = %s AND EXTRACT(MONTH FROM data) = %s AND EXTRACT(YEAR FROM data) = %s AND forma_pagamento = 'Recorrente'"
    cursor.execute(query, (session['nivel_organizacional'], mes_atual, ano_atual))
    total_recorrente = cursor.fetchone()[0]

    query = "SELECT SUM(valor) FROM caixa WHERE unidade = %s AND EXTRACT(MONTH FROM data) = %s AND EXTRACT(YEAR FROM data) = %s AND forma_pagamento = 'Outros'"
    cursor.execute(query, (session['nivel_organizacional'], mes_atual, ano_atual))
    total_outros = cursor.fetchone()[0]

    query = "SELECT nome, SUM(valor) FROM caixa WHERE unidade = %s AND EXTRACT(MONTH FROM data) = %s AND EXTRACT(YEAR FROM data) = %s GROUP BY nome"
    cursor.execute(query, (session['nivel_organizacional'], mes_atual, ano_atual))
    usuarios = cursor.fetchall()

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)

    pdf.setFont("Helvetica", 14)
    pdf.drawString(50, 750, "Relatório mensal caixa")

    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 700, f"Total de movimentação no mês: R$ {Decimal(total_movimentacao):,.2f}")
    pdf.drawString(50, 680, f"Total Venda: R$ {Decimal(total_venda):,.2f}")
    pdf.drawString(50, 660, f"Total Regularização: R$ {Decimal(total_regularizacao):,.2f}")
    pdf.drawString(50, 640, f"Total Dinheiro: R$ {Decimal(total_dinheiro):,.2f}")
    pdf.drawString(50, 620, f"Total Pix: R$ {Decimal(total_pix):,.2f}")
    pdf.drawString(50, 600, f"Total Débito: R$ {Decimal(total_debito):,.2f}")
    pdf.drawString(50, 580, f"Total Crédito: R$ {Decimal(total_credito):,.2f}")
    pdf.drawString(50, 560, f"Total Recorrente: R$ {Decimal(total_recorrente):,.2f}")
    pdf.drawString(50, 540, f"Total Outros: R$ {Decimal(total_outros):,.2f}")

    pdf.setFont("Helvetica", 10)
    pdf.drawString(50, 500, "Total recebido por cada usuário no mesmo mês da solicitação:")
    y = 480
    for usuario in usuarios:
        nome_usuario, total_usuario = usuario
        pdf.drawString(50, y, f"{nome_usuario}: R$ {Decimal(total_usuario):,.2f}")
        y -= 20

    pdf.showPage()
    pdf.save()

    buffer.seek(0)

    cursor.close()
    conn.close()

    return send_file(buffer, attachment_filename='relatorio_mensal.pdf', as_attachment=True)
