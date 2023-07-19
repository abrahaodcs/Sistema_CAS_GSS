# calculadora_cancelamento.py

from flask import Blueprint, render_template, request, session, send_file
from datetime import datetime
import pdfkit
import os

calculadora_cancelamento_bp = Blueprint('calculadora_cancelamento', __name__)

@calculadora_cancelamento_bp.route('/calcular_cancelamento_contrato', methods=['GET', 'POST'])
def calcular_cancelamento_contrato():
    cancelamentoItems = []

    if request.method == 'POST':
        # Obter os dados dos itens de cancelamento do formulário
        form_data = request.form.to_dict(flat=False)
        for key, value in form_data.items():
            if key.startswith('cancelamento-item-'):
                cancelamento_item = float(value[0].replace(',', '.'))
                cancelamentoItems.append(cancelamento_item)

        # Calcular o valor total do cancelamento do contrato
        valor_cancelamento_contrato = sum(cancelamentoItems)

        return render_template('calculadora_cancelamento.html', valor_cancelamento_contrato=valor_cancelamento_contrato,
                               cancelamentoItems=cancelamentoItems)

    return render_template('calculadora_cancelamento.html')

@calculadora_cancelamento_bp.route('/calcular_cancelamento', methods=['POST'])
def calcular():
    dados = request.form

    valor_sessoes = (float(dados['valor-item'].replace(',', '.')) / 5) * float(dados['sessoes'])
    valor_multa = ((float(dados['valor-item'].replace(',', '.')) - valor_sessoes) / 100) * float(dados['multa'].replace(',', '.'))
    calculo_cancelamento_item = valor_sessoes + valor_multa

    # Armazena o cálculo na sessão para uso posterior
    cancelamentoItems = session.get('cancelamentoItems', [])
    cancelamentoItems.append({
        'valor_sessoes': valor_sessoes,
        'valor_multa': valor_multa,
        'calculo_cancelamento_item': calculo_cancelamento_item
    })
    session['cancelamentoItems'] = cancelamentoItems

    return {
        'valor_sessoes': valor_sessoes,
        'valor_multa': valor_multa,
        'calculo_cancelamento_item': calculo_cancelamento_item
    }
