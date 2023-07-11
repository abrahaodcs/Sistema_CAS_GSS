# calculadora_cancelamento.py

from flask import Blueprint, render_template, request, session, send_file
from datetime import datetime, timedelta
from werkzeug.datastructures import ImmutableMultiDict

calculadora_cancelamento_bp = Blueprint('calculadora_cancelamento', __name__)

@calculadora_cancelamento_bp.route('/calcular_cancelamento_contrato', methods=['GET', 'POST'])
def calcular_cancelamento_contrato():
    cancelamentoItems = []

    # Obter os dados dos itens de cancelamento do formulário
    form_data = ImmutableMultiDict(request.form)
    for key, value in form_data.items():
        if key.startswith('cancelamento-item-'):
            cancelamento_item = float(value.replace(',', '.'))
            cancelamentoItems.append(cancelamento_item)

    # Calcular o valor total do cancelamento do contrato
    valor_cancelamento_contrato = sum(cancelamentoItems)

    # Configurar a expiração do arquivo PDF
    data_expiracao = datetime.now() + timedelta(days=5)
    session['pdf_expiracao'] = data_expiracao

    return render_template('calculadora_cancelamento.html', valor_cancelamento_contrato=valor_cancelamento_contrato,
                           cancelamentoItems=cancelamentoItems)

@calculadora_cancelamento_bp.route('/calcular_cancelamento', methods=['POST'])
def calcular():
    dados = request.form

    valor_sessoes = (float(dados['valor_item'].replace(',', '.')) / 5) * float(dados['sessoes'])
    valor_multa = (float(dados['valor_item'].replace(',', '.')) / 100) * float(dados['multa'].replace(',', '.'))
    calculo_cancelamento_item = (valor_sessoes + valor_multa) - float(dados['valor_pago'].replace(',', '.'))

    # Armazena o cálculo na sessão para uso posterior
    cancelamentoItems = session.get('cancelamentoItems', [])
    cancelamentoItems.append(calculo_cancelamento_item)
    session['cancelamentoItems'] = cancelamentoItems

    return {
        'valor_sessoes': valor_sessoes,
        'valor_multa': valor_multa,
        'calculo_cancelamento_item': calculo_cancelamento_item
    }
