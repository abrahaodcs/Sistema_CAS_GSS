from flask import Blueprint, render_template, session, send_file
from datetime import datetime, timedelta
import pdfkit

gerar_relatorio_cancelamento_bp = Blueprint('gerar_relatorio_cancelamento', __name__)

@gerar_relatorio_cancelamento_bp.route('/gerar_relatorio_cancelamento', methods=['POST'])
def gerar_relatorio_cancelamento():
    contrato = request.form['contrato']

    # Obtenha os dados do cancelamento do contrato da sessão
    cancelamentoItems = session.get('cancelamentoItems', [])

    # Calcule o valor total do cancelamento do contrato
    calculoCancelamentoContrato = sum(cancelamentoItems)

    # Obtenha os dados adicionais do formulário
    nome_cliente = session.get('nome_cliente')

    # Crie um dicionário com os dados do contrato e dos itens de cancelamento
    dados_relatorio = {
        'nome_cliente': nome_cliente,
        'contrato': contrato,
        'cancelamentoItems': cancelamentoItems,
        'calculoCancelamentoContrato': calculoCancelamentoContrato,
        'totalValorContrato': sum([item['valor_item'] for item in cancelamentoItems]),
        'totalValorSessoes': sum([item['valor_sessoes'] for item in cancelamentoItems]),
        'totalValorMulta': sum([item['valor_multa'] for item in cancelamentoItems]),
        'totalValorPago': sum([item['valor_pago'] for item in cancelamentoItems]),
        'totalCancelamento': sum([item['valor_cancelamento_item'] for item in cancelamentoItems])
    }

    # Renderize o template do relatório com os dados
    html = render_template('relatorio_cancelamento.html', dados=dados_relatorio)

    # Crie um nome de arquivo único para o relatório PDF
    data_atual = datetime.now().strftime("%d-%m-%Y")
    nome_arquivo = f'cancelamento_contrato_{data_atual}_{contrato}.pdf'

    # Configuração do PDFKit
    pdfkit_config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')

    # Converta o HTML em PDF e salve o arquivo
    pdfkit.from_string(html, nome_arquivo, configuration=pdfkit_config)

    # Limpe a lista de cancelamento de itens da sessão
    session.pop('cancelamentoItems', None)
    session.pop('nome_cliente', None)

    # Envie o arquivo PDF para download
    return send_file(nome_arquivo, as_attachment=True)
