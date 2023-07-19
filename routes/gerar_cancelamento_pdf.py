# gerar_cancelamento_pdf.py

from flask import Blueprint, render_template, request, session, send_file
from datetime import datetime
import pdfkit

gerar_cancelamento_pdf_bp = Blueprint('gerar_cancelamento_pdf', __name__)

@gerar_cancelamento_pdf_bp.route('/gerar_cancelamento_pdf', methods=['POST'])
def gerar_relatorio_pdf():
    contrato = request.form['contrato']

    # Obtenha os dados do cancelamento do contrato da sessão
    cancelamentoItems = session.get('cancelamentoItems', [])

    # Calcule o valor total do cancelamento do contrato
    valorSessoesContrato = sum([item['valor_sessoes'] for item in cancelamentoItems])
    valorMultaContrato = sum([item['valor_multa'] for item in cancelamentoItems])
    valorPago = float(request.form['valor-pago'].replace(',', '.'))
    valorCancelamentoContrato = valorSessoesContrato + valorMultaContrato - valorPago

    # Crie um dicionário com os dados do contrato e dos itens de cancelamento
    dados_relatorio = {
        'contrato': contrato,
        'cancelamentoItems': cancelamentoItems,
        'valorSessoesContrato': valorSessoesContrato,
        'valorMultaContrato': valorMultaContrato,
        'valorPago': valorPago,
        'valorCancelamentoContrato': valorCancelamentoContrato
    }

    # Renderize o template do relatório com os dados
    html = render_template('relatorio_cancelamento.html', dados=dados_relatorio)

    # Crie um nome de arquivo único para o relatório PDF
    data_atual = datetime.now().strftime("%d-%m-%Y")
    nome_arquivo = f'cancelamento_contrato_{data_atual}_{contrato}.pdf'

    # Caminho completo para o diretório de arquivos estáticos
    static_dir = os.path.join(os.path.dirname(__file__), 'static')

    # Caminho completo para o arquivo de estilo CSS
    css_file = os.path.join(static_dir, 'relatorio.css')

    # Configuração do PDFKit
    pdfkit_config = pdfkit.configuration(wkhtmltopdf="C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

    # Converta o HTML em PDF e salve o arquivo
    pdfkit.from_string(html, nome_arquivo, configuration=pdfkit_config, css=css_file)

    # Limpe a lista de cancelamento de itens da sessão
    session.pop('cancelamentoItems', None)

    # Envie o arquivo PDF para download
    return send_file(nome_arquivo, as_attachment=True)