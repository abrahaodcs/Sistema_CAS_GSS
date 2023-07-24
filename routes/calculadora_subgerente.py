# calculadora_subgerente.py

from flask import Blueprint, render_template, request

calculadora_subgerente_bp = Blueprint('calculadora_subgerente', __name__)

@calculadora_subgerente_bp.route('/calculadora_subgerente', methods=['GET', 'POST'])
def calcular_bonificacao():
    if request.method == 'POST':
        meta_loja_dezena1 = float(request.form['meta_loja_dezena1'].replace('R$', '').replace(',', '.'))
        meta_loja_dezena2 = float(request.form['meta_loja_dezena2'].replace('R$', '').replace(',', '.'))
        meta_loja_dezena3 = float(request.form['meta_loja_dezena3'].replace('R$', '').replace(',', '.'))
        total_meta_loja = meta_loja_dezena1 + meta_loja_dezena2 + meta_loja_dezena3

        meta_individual_dezena1 = float(request.form['meta_individual_dezena1'].replace('R$', '').replace(',', '.'))
        meta_individual_dezena2 = float(request.form['meta_individual_dezena2'].replace('R$', '').replace(',', '.'))
        meta_individual_dezena3 = float(request.form['meta_individual_dezena3'].replace('R$', '').replace(',', '.'))
        total_meta_individual = meta_individual_dezena1 + meta_individual_dezena2 + meta_individual_dezena3

        venda_loja_dezena1 = float(request.form['venda_loja_dezena1'].replace('R$', '').replace(',', '.'))
        venda_loja_dezena2 = float(request.form['venda_loja_dezena2'].replace('R$', '').replace(',', '.'))
        venda_loja_dezena3 = float(request.form['venda_loja_dezena3'].replace('R$', '').replace(',', '.'))
        total_venda_loja = venda_loja_dezena1 + venda_loja_dezena2 + venda_loja_dezena3

        venda_individual_dezena1 = float(request.form['venda_individual_dezena1'].replace('R$', '').replace(',', '.'))
        venda_individual_dezena2 = float(request.form['venda_individual_dezena2'].replace('R$', '').replace(',', '.'))
        venda_individual_dezena3 = float(request.form['venda_individual_dezena3'].replace('R$', '').replace(',', '.'))
        total_venda_individual = venda_individual_dezena1 + venda_individual_dezena2 + venda_individual_dezena3

        atingimento_meta_loja1 = venda_loja_dezena1 / meta_loja_dezena1 if meta_loja_dezena1 != 0 else 0
        atingimento_meta_loja2 = venda_loja_dezena2 / meta_loja_dezena2 if meta_loja_dezena2 != 0 else 0
        atingimento_meta_loja3 = venda_loja_dezena3 / meta_loja_dezena3 if meta_loja_dezena3 != 0 else 0
        atingimento_meta_loja_mes = total_venda_loja / total_meta_loja if total_meta_loja != 0 else 0

        atingimento_meta_individual1 = venda_individual_dezena1 / meta_individual_dezena1 if meta_individual_dezena1 != 0 else 0
        atingimento_meta_individual2 = venda_individual_dezena2 / meta_individual_dezena2 if meta_individual_dezena2 != 0 else 0
        atingimento_meta_individual3 = venda_individual_dezena3 / meta_individual_dezena3 if meta_individual_dezena3 != 0 else 0
        atingimento_meta_individual_mes = total_venda_individual / total_meta_individual if total_meta_individual != 0 else 0

        status_loja1 = calcular_status(atingimento_meta_loja1)
        status_loja2 = calcular_status(atingimento_meta_loja2)
        status_loja3 = calcular_status(atingimento_meta_loja3)
        status_loja_mes = calcular_status(atingimento_meta_loja_mes)

        status_individual1 = calcular_status(atingimento_meta_individual1)
        status_individual2 = calcular_status(atingimento_meta_individual2)
        status_individual3 = calcular_status(atingimento_meta_individual3)

        bonificacao_individual1 = calcular_bonificacao_percentual(atingimento_meta_individual1)
        bonificacao_individual2 = calcular_bonificacao_percentual(atingimento_meta_individual2)
        bonificacao_individual3 = calcular_bonificacao_percentual(atingimento_meta_individual3)

        rv1 = venda_individual_dezena1 * bonificacao_individual1 if atingimento_meta_loja1 >= 1.0 else 0
        rv2 = venda_individual_dezena2 * bonificacao_individual2 if atingimento_meta_loja2 >= 1.0 else 0
        rv3 = venda_individual_dezena3 * bonificacao_individual3 if atingimento_meta_loja3 >= 1.0 else 0

        nps = int(request.form['nps'])
        rv_nps = calcular_rv_nps(nps, atingimento_meta_loja_mes)

        rv_sem_acelerador = rv1 + rv2 + rv3 + rv_nps

        acelerador = calcular_acelerador(atingimento_meta_individual_mes)

        rv_total = (rv_sem_acelerador * acelerador) + rv_sem_acelerador

        return render_template('calculadora_subgerente.html',
                                meta_loja_dezena1=format_money(meta_loja_dezena1),
                                meta_loja_dezena2=format_money(meta_loja_dezena2),
                                meta_loja_dezena3=format_money(meta_loja_dezena3),
                                total_meta_loja=format_money(total_meta_loja),
                                meta_individual_dezena1=format_money(meta_individual_dezena1),
                                meta_individual_dezena2=format_money(meta_individual_dezena2),
                                meta_individual_dezena3=format_money(meta_individual_dezena3),
                                total_meta_individual=format_money(total_meta_individual),
                                venda_loja_dezena1=format_money(venda_loja_dezena1),
                                venda_loja_dezena2=format_money(venda_loja_dezena2),
                                venda_loja_dezena3=format_money(venda_loja_dezena3),
                                total_venda_loja=format_money(total_venda_loja),
                                venda_individual_dezena1=format_money(venda_individual_dezena1),
                                venda_individual_dezena2=format_money(venda_individual_dezena2),
                                venda_individual_dezena3=format_money(venda_individual_dezena3),
                                total_venda_individual=format_money(total_venda_individual),
                                atingimento_meta_loja1=format_percent(atingimento_meta_loja1),
                                atingimento_meta_loja2=format_percent(atingimento_meta_loja2),
                                atingimento_meta_loja3=format_percent(atingimento_meta_loja3),
                                atingimento_meta_loja_mes=format_percent(atingimento_meta_loja_mes),
                                atingimento_meta_individual1=format_percent(atingimento_meta_individual1),
                                atingimento_meta_individual2=format_percent(atingimento_meta_individual2),
                                atingimento_meta_individual3=format_percent(atingimento_meta_individual3),
                                atingimento_meta_individual_mes=format_percent(atingimento_meta_individual_mes),
                                status_loja1=status_loja1,
                                status_loja2=status_loja2,
                                status_loja3=status_loja3,
                                status_loja_mes=status_loja_mes,
                                status_individual1=status_individual1,
                                status_individual2=status_individual2,
                                status_individual3=status_individual3,
                                bonificacao_individual1=format_percent(bonificacao_individual1),
                                bonificacao_individual2=format_percent(bonificacao_individual2),
                                bonificacao_individual3=format_percent(bonificacao_individual3),
                                rv1=format_money(rv1),
                                rv2=format_money(rv2),
                                rv3=format_money(rv3),
                                nps=nps,
                                rv_nps=format_money(rv_nps),
                                rv_sem_acelerador=format_money(rv_sem_acelerador),
                                acelerador=format_percent(acelerador),
                                rv_total=format_money(rv_total)
                            )
    return render_template('calculadora_subgerente.html')

def format_money(value):
    return f'R$ {value:.2f}'

def format_percent(value):
    return f'{value:.2%}'

def calcular_status_loja(atingimento):
    if atingimento >= 1.44:
        return 'Hiper'
    elif atingimento >= 1.2:
        return 'Super'
    elif atingimento >= 1.0:
        return 'Meta'
    else:
        return 'Na'

def calcular_status_individual(atingimento):
    if atingimento >= 1.55:
        return 'Hiper'
    elif atingimento >= 1.3:
        return 'Super'
    elif atingimento >= 1.0:
        return 'Meta'
    else:
        return 'Na'

def calcular_bonificacao_percentual(atingimento):
    if atingimento >= 1.55:
        return 0.03
    elif atingimento >= 1.3:
        return 0.02
    elif atingimento >= 1.0:
        return 0.015
    else:
        return 0

def calcular_rv_nps(nps, atingimento_meta_loja_mes):
    if nps >= 85 and atingimento_meta_loja_mes >= 1.0:
        return 100
    else:
        return 0

def calcular_acelerador(atingimento_meta_individual_mes):
    if atingimento_meta_individual_mes >= 1.44:
        return 0.6
    elif atingimento_meta_individual_mes >= 1.2:
        return 0.45
    elif atingimento_meta_individual_mes >= 1.0:
        return 0.3
    else:
        return 0
