# calculadora_subgerente.py

from flask import Blueprint, render_template, request

calculadora_subgerente_bp = Blueprint('calculadora_subgerente', __name__)

@calculadora_subgerente_bp.route('/calculadora_subgerente', methods=['GET', 'POST'])
def calculadora_subgerente():
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
        nps = float(request.form['nps'])
        rv_sem_acelerador = float(request.form['rv_sem_acelerador'])

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
        status_loja_mes = calcular_status(percentual_meta_loja)
        status_individual_mes = calcular_status(percentual_meta_individual)

        # Cálculo do RV
        rv_dezena_loja_1 = calcular_rv_dezena(venda_loja_dezena_1, percentual_meta_loja, status_loja_dezena_1)
        rv_dezena_loja_2 = calcular_rv_dezena(venda_loja_dezena_2, percentual_meta_loja, status_loja_dezena_2)
        rv_dezena_loja_3 = calcular_rv_dezena(venda_loja_dezena_3, percentual_meta_loja, status_loja_dezena_3)
        rv_dezena_individual_1 = calcular_rv_dezena(venda_individual_dezena_1, percentual_meta_individual, status_individual_dezena_1)
        rv_dezena_individual_2 = calcular_rv_dezena(venda_individual_dezena_2, percentual_meta_individual, status_individual_dezena_2)
        rv_dezena_individual_3 = calcular_rv_dezena(venda_individual_dezena_3, percentual_meta_individual, status_individual_dezena_3)
        rv_nps = calcular_rv_nps(nps, percentual_meta_individual)
        total_rv = calcular_total_rv(percentual_meta_individual, rv_sem_acelerador)

        # Renderização do template da calculadora para o método POST
        return render_template('calculadora_subgerente.html',
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
            nps=nps,
            rv_sem_acelerador=rv_sem_acelerador,
            percentual_meta_loja=percentual_meta_loja,
            percentual_meta_individual=percentual_meta_individual,
            status_loja_dezena_1=status_loja_dezena_1,
            status_loja_dezena_2=status_loja_dezena_2,
            status_loja_dezena_3=status_loja_dezena_3,
            status_individual_dezena_1=status_individual_dezena_1,
            status_individual_dezena_2=status_individual_dezena_2,
            status_individual_dezena_3=status_individual_dezena_3,
            status_loja_mes=status_loja_mes,
            status_individual_mes=status_individual_mes,
            rv_dezena_loja_1=rv_dezena_loja_1,
            rv_dezena_loja_2=rv_dezena_loja_2,
            rv_dezena_loja_3=rv_dezena_loja_3,
            rv_dezena_individual_1=rv_dezena_individual_1,
            rv_dezena_individual_2=rv_dezena_individual_2,
            rv_dezena_individual_3=rv_dezena_individual_3,
            rv_nps=rv_nps,
            total_rv=total_rv
        )

    # Renderização do template da calculadora para o método GET
    return render_template('calculadora_subgerente.html')

# Função para calcular o status com base no percentual de meta alcançado
def calcular_status(percentual_meta):
    if percentual_meta >= 100:
        return 'Atingido'
    elif percentual_meta >= 70:
        return 'Em Evolução'
    else:
        return 'Não Atingido'

# Função para calcular o RV da dezena
def calcular_rv_dezena(venda_dezena, percentual_meta, status):
    if status == 'Atingido':
        return venda_dezena * 0.02
    elif status == 'Em Evolução':
        return venda_dezena * 0.01
    else:
        return 0

# Função para calcular o RV com base no NPS
def calcular_rv_nps(nps, percentual_meta):
    if nps >= 80 and percentual_meta >= 70:
        return 500
    elif nps >= 70 and percentual_meta >= 70:
        return 300
    else:
        return 0

# Função para calcular o Total de RV
def calcular_total_rv(percentual_meta, rv_sem_acelerador):
    if percentual_meta >= 70:
        return rv_sem_acelerador + 500
    else:
        return rv_sem_acelerador
