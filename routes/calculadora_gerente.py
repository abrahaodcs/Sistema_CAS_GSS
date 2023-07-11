# calculadora_gerente.py

from flask import Blueprint, render_template, request

calculadora_gerente_bp = Blueprint('calculadora_gerente', __name__)

@calculadora_gerente_bp.route('/calculadora_gerente', methods=['GET', 'POST'])
def calculadora_gerente():
    if request.method == 'POST':
        # Obter os valores dos campos preenchidos pelo usuário
        meta_loja_dezena_1 = float(request.form.get('meta_loja_dezena_1', 0))
        venda_loja_dezena_1 = float(request.form.get('venda_loja_dezena_1', 0))
        meta_loja_dezena_2 = float(request.form.get('meta_loja_dezena_2', 0))
        venda_loja_dezena_2 = float(request.form.get('venda_loja_dezena_2', 0))
        meta_loja_dezena_3 = float(request.form.get('meta_loja_dezena_3', 0))
        venda_loja_dezena_3 = float(request.form.get('venda_loja_dezena_3', 0))
        meta_individual_dezena_1 = float(request.form.get('meta_individual_dezena_1', 0))
        venda_individual_dezena_1 = float(request.form.get('venda_individual_dezena_1', 0))
        meta_individual_dezena_2 = float(request.form.get('meta_individual_dezena_2', 0))
        venda_individual_dezena_2 = float(request.form.get('venda_individual_dezena_2', 0))
        meta_individual_dezena_3 = float(request.form.get('meta_individual_dezena_3', 0))
        venda_individual_dezena_3 = float(request.form.get('venda_individual_dezena_3', 0))
        nps = int(request.form.get('nps', 0))

        # Cálculos dos campos
        meta_mes_loja = meta_loja_dezena_1 + meta_loja_dezena_2 + meta_loja_dezena_3
        venda_mes_loja = venda_loja_dezena_1 + venda_loja_dezena_2 + venda_loja_dezena_3
        percentual_meta_mes_loja = (venda_mes_loja / meta_mes_loja) * 100 if meta_mes_loja > 0 else 0

        meta_mes_individual = meta_individual_dezena_1 + meta_individual_dezena_2 + meta_individual_dezena_3
        venda_mes_individual = venda_individual_dezena_1 + venda_individual_dezena_2 + venda_individual_dezena_3
        percentual_meta_mes_individual = (venda_mes_individual / meta_mes_individual) * 100 if meta_mes_individual > 0 else 0

        status_loja_dezena_1 = calcular_status(percentual_meta_mes_loja)
        status_individual_dezena_1 = calcular_status(percentual_meta_mes_individual)
        rv_dezena_individual_1 = calcular_rv_dezena(venda_individual_dezena_1, percentual_meta_mes_loja, status_individual_dezena_1)
        rv_dezena_loja_1 = calcular_rv_dezena(venda_loja_dezena_1, percentual_meta_mes_individual, status_loja_dezena_1)

        status_loja_dezena_2 = calcular_status(percentual_meta_mes_loja)
        status_individual_dezena_2 = calcular_status(percentual_meta_mes_individual)
        rv_dezena_individual_2 = calcular_rv_dezena(venda_individual_dezena_2, percentual_meta_mes_loja, status_individual_dezena_2)
        rv_dezena_loja_2 = calcular_rv_dezena(venda_loja_dezena_2, percentual_meta_mes_individual, status_loja_dezena_2)

        status_loja_dezena_3 = calcular_status(percentual_meta_mes_loja)
        status_individual_dezena_3 = calcular_status(percentual_meta_mes_individual)
        rv_dezena_individual_3 = calcular_rv_dezena(venda_individual_dezena_3, percentual_meta_mes_loja, status_individual_dezena_3)
        rv_dezena_loja_3 = calcular_rv_dezena(venda_loja_dezena_3, percentual_meta_mes_individual, status_loja_dezena_3)

        status_loja_mes = calcular_status(percentual_meta_mes_loja)
        status_individual_mes = calcular_status(percentual_meta_mes_individual)
        rv_nps = calcular_rv_nps(nps, percentual_meta_mes_individual)

        rv_sem_acelerador = (
            rv_dezena_individual_1 + rv_dezena_individual_2 + rv_dezena_individual_3 +
            rv_dezena_loja_1 + rv_dezena_loja_2 + rv_dezena_loja_3 + rv_nps
        )

        total_rv = calcular_total_rv(percentual_meta_mes_individual, rv_sem_acelerador)

        # Renderização do template com os resultados
        return render_template(
            'calculadora_gerente.html',
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
            meta_mes_loja=meta_mes_loja,
            venda_mes_loja=venda_mes_loja,
            percentual_meta_mes_loja=percentual_meta_mes_loja,
            meta_mes_individual=meta_mes_individual,
            venda_mes_individual=venda_mes_individual,
            percentual_meta_mes_individual=percentual_meta_mes_individual,
            status_loja_dezena_1=status_loja_dezena_1,
            status_individual_dezena_1=status_individual_dezena_1,
            rv_dezena_individual_1=rv_dezena_individual_1,
            rv_dezena_loja_1=rv_dezena_loja_1,
            status_loja_dezena_2=status_loja_dezena_2,
            status_individual_dezena_2=status_individual_dezena_2,
            rv_dezena_individual_2=rv_dezena_individual_2,
            rv_dezena_loja_2=rv_dezena_loja_2,
            status_loja_dezena_3=status_loja_dezena_3,
            status_individual_dezena_3=status_individual_dezena_3,
            rv_dezena_individual_3=rv_dezena_individual_3,
            rv_dezena_loja_3=rv_dezena_loja_3,
            status_loja_mes=status_loja_mes,
            status_individual_mes=status_individual_mes,
            rv_nps=rv_nps,
            rv_sem_acelerador=rv_sem_acelerador,
            total_rv=total_rv
        )

    # Renderização do template da calculadora para o método GET
    return render_template('calculadora_gerente.html')

# Função para calcular o status com base no percentual de meta alcançado
def calcular_status(percentual_meta):
    if percentual_meta >= 100:
        return 'Atingido'
    elif percentual_meta >= 75:
        return 'Parcial'
    else:
        return 'Não Atingido'

# Função para calcular o RV de uma dezena com base nas vendas, percentual de meta alcançado e status
def calcular_rv_dezena(vendas, percentual_meta, status):
    if status == 'Atingido':
        return vendas * 0.1
    elif status == 'Parcial':
        return vendas * 0.05
    else:
        return 0

# Função para calcular o RV do NPS com base no valor do NPS e percentual de meta alcançado
def calcular_rv_nps(nps, percentual_meta):
    if percentual_meta >= 100:
        if nps >= 75:
            return 100
        elif nps >= 50:
            return 50
    return 0

# Função para calcular o RV total considerando o percentual de meta e o RV sem acelerador
def calcular_total_rv(percentual_meta, rv_sem_acelerador):
    if percentual_meta >= 100:
        return rv_sem_acelerador * 1.5
    else:
        return rv_sem_acelerador
