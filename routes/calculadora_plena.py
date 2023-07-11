# calculadora_plena.py

from flask import Blueprint, render_template, request

calculadora_plena_bp = Blueprint('calculadora_plena', __name__)

@calculadora_plena_bp.route('/calculadora_plena', methods=['GET', 'POST'])
def calculadora_plena():
    if request.method == 'POST':
        # Obtendo os valores enviados pelo formulário
        meta_loja_dezena_1 = float(request.form['meta_loja_dezena_1'])
        venda_loja_dezena_1 = float(request.form['venda_loja_dezena_1'])
        meta_loja_dezena_2 = float(request.form['meta_loja_dezena_2'])
        venda_loja_dezena_2 = float(request.form['venda_loja_dezena_2'])
        meta_loja_dezena_3 = float(request.form['meta_loja_dezena_3'])
        venda_loja_dezena_3 = float(request.form['venda_loja_dezena_3'])
        meta_individual_dezena_1 = float(request.form['meta_individual_dezena_1'])
        venda_individual_dezena_1 = float(request.form['venda_individual_dezena_1'])
        meta_individual_dezena_2 = float(request.form['meta_individual_dezena_2'])
        venda_individual_dezena_2 = float(request.form['venda_individual_dezena_2'])
        meta_individual_dezena_3 = float(request.form['meta_individual_dezena_3'])
        venda_individual_dezena_3 = float(request.form['venda_individual_dezena_3'])

        # Cálculo do percentual de meta alcançado
        percentual_meta_loja = (venda_loja_dezena_1 + venda_loja_dezena_2 + venda_loja_dezena_3) / (meta_loja_dezena_1 + meta_loja_dezena_2 + meta_loja_dezena_3) * 100
        percentual_meta_individual = (venda_individual_dezena_1 + venda_individual_dezena_2 + venda_individual_dezena_3) / (meta_individual_dezena_1 + meta_individual_dezena_2 + meta_individual_dezena_3) * 100

        # Cálculo do status
        status_loja_dezena_1 = calcular_status(percentual_meta_loja)
        status_loja_dezena_2 = calcular_status(percentual_meta_loja)
        status_loja_dezena_3 = calcular_status(percentual_meta_loja)
        status_individual_dezena_1 = calcular_status(percentual_meta_individual)
        status_individual_dezena_2 = calcular_status(percentual_meta_individual)
        status_individual_dezena_3 = calcular_status(percentual_meta_individual)

        # Renderização do template da calculadora para o método POST
        return render_template('calculadora_plena.html',
            meta_loja_dezena_1=meta_loja_dezena_1,
            venda_loja_dezena_1=venda_loja_dezena_1,
            meta_loja_dezena_2=meta_loja_dezena_2,
            venda_loja_dezena_2=venda_loja_dezena_2,
            meta_loja_dezena_3=meta_loja_dezena_3,
            venda_loja_dezena_3=venda_loja_dezena_3,
            meta_individual_dezena_1=meta_individual_dezena_1,
            venda_individual_dezena_1=venda_individual_dezena_1,
            meta_individual_dezena_2=meta_individual_dezena_2,
            venda_individual_dezena_2=venda_individual_dezena_2,
            meta_individual_dezena_3=meta_individual_dezena_3,
            venda_individual_dezena_3=venda_individual_dezena_3,
            percentual_meta_loja=percentual_meta_loja,
            percentual_meta_individual=percentual_meta_individual,
            status_loja_dezena_1=status_loja_dezena_1,
            status_loja_dezena_2=status_loja_dezena_2,
            status_loja_dezena_3=status_loja_dezena_3,
            status_individual_dezena_1=status_individual_dezena_1,
            status_individual_dezena_2=status_individual_dezena_2,
            status_individual_dezena_3=status_individual_dezena_3
        )

    # Renderização do template da calculadora para o método GET
    return render_template('calculadora_plena.html')

# Função para calcular o status com base no percentual de meta alcançado
def calcular_status(percentual_meta):
    if percentual_meta >= 100:
        return 'Atingido'
    elif percentual_meta >= 70:
        return 'Em Evolução'
    else:
        return 'Não Atingido'
