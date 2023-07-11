import pandas as pd
import mysql.connector
import schedule
import time
from datetime import date

# Configurações do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Hinata@82',
    'database': 'cas_gss'
}

# Caminho para a planilha do Excel (Agendamentos)
agendamentos_excel_file = r'A:\SIS_CAS_GSS\elos\agendamentos.xlsx'

# Caminho para a planilha do Excel (Bonificações)
bonificacoes_excel_file = r'A:\SIS_CAS_GSS\elos\bonificacoes.xlsx'

# Caminho para a planilha do Excel (Calculo de Vendas)
calculo_vendas_excel_file = r'A:\SIS_CAS_GSS\elos\calculo_vendas.xlsx'

# Caminho para a planilha do Excel (Clientes)
clientes_excel_file = r'A:\SIS_CAS_GSS\elos\clientes.xlsx'

# Caminho para a planilha do Excel (Cluster e NPS)
cluster_nps_excel_file = r'A:\SIS_CAS_GSS\elos\cluster _ nps.xlsx'

# Caminho para a planilha do Excel (CPF Colaboradoras)
cpf_colaboradora_excel_file = r'A:\SIS_CAS_GSS\elos\cpf_colaboradora.xlsx'

# Caminho para a planilha do Excel (Intercorrências)
intercorrencias_excel_file = r'A:\SIS_CAS_GSS\elos\intercorrencias.xlsx'

# Caminho para a planilha do Excel (Itens)
itens_excel_file = r'A:\SIS_CAS_GSS\elos\itens.xlsx'

# Caminho para a planilha do Excel (Metas Colaboradoras)
metas_colaboradora_excel_file = r'A:\SIS_CAS_GSS\elos\metas_colaboradora.xlsx'

# Caminho para a planilha do Excel (Metas Unidades)
metas_unidade_excel_file = r'A:\SIS_CAS_GSS\elos\metas_unidade.xlsx'

# Caminho para a planilha do Excel (Orçamentos)
orcamentos_excel_file = r'A:\SIS_CAS_GSS\elos\orcamentos.xlsx'

# Caminho para a planilha do Excel (Procedimentos)
procedimentos_excel_file = r'A:\SIS_CAS_GSS\elos\procedimentos.xlsx'

# Caminho para a planilha do Excel (Recursos Humanos)
recursos_humanos_excel_file = r'A:\SIS_CAS_GSS\elos\recursos_humanos.xlsx'

# Caminho para a planilha do Excel (Vendas)
vendas_excel_file = r'A:\SIS_CAS_GSS\elos\vendas.xlsx'

# Nome da tabela no banco de dados (Agendamentos)
agendamentos_db_table = 'agendamentos'

# Nome da tabela no banco de dados (Bonificações)
bonificacoes_db_table = 'bonificacao'

# Nome da tabela no banco de dados (Calculo de Vendas)
calculo_vendas_db_table = 'calculo_vendas'

# Nome da tabela no banco de dados (Clientes)
clientes_db_table = 'clientes'

# Nome da tabela no banco de dados (Cluster e NPS)
cluster_nps_db_table = 'cluster_nps'

# Nome da tabela no banco de dados (CPF Colaboradoras)
cpf_colaboradora_db_table = 'cpf_colaboradora'

# Nome da tabela no banco de dados (Intercorrências)
intercorrencias_db_table = 'intercorrencias'

# Nome da tabela no banco de dados (Itens)
itens_db_table = 'itens'

# Nome da tabela no banco de dados (Metas Colaboradoras)
metas_colaboradora_db_table = 'metas_colaboradora'

# Nome da tabela no banco de dados (Metas Colaboradoras)
metas_unidade_db_table = 'metas_unidade'

# Nome da tabela no banco de dados (Orçamentos)
orcamentos_db_table = 'orcamentos'

# Nome da tabela no banco de dados (Procedimentos)
procedimentos_db_table = 'procedimentos'

# Nome da tabela no banco de dados (Recursos Humanos)
recursos_humanos_db_table = 'recursos_humanos'

# Nome da tabela no banco de dados (Vendas)
vendas_db_table = 'vendas'

# Leitura dos dados da planilha do Excel (Agendamentos)
df_agendamentos = pd.read_excel(agendamentos_excel_file)

# Adicione uma coluna com a data atual (Agendamentos)
df_agendamentos['data_atualizacao_bd'] = date.today()

# Leitura dos dados da planilha do Excel (Bonificações)
df_bonificacoes = pd.read_excel(bonificacoes_excel_file)

# Adicione uma coluna com a data atual (Bonificações)
df_bonificacoes['data_atualizacao_bd'] = date.today()

# Leitura dos dados da planilha do Excel (Calculo de Vendas)
df_calculo_vendas = pd.read_excel(calculo_vendas_excel_file)

# Adicione uma coluna com a data atual (Calculo de Vendas)
df_calculo_vendas['data_atualizacao_bd'] = date.today()

# Leitura dos dados da planilha do Excel (Clientes)
df_clientes = pd.read_excel(clientes_excel_file)

# Adicione uma coluna com a data atual (Clientes)
df_clientes['data_atualizacao_bd'] = date.today()

# Leitura dos dados da planilha do Excel (Cluster e NPS)
df_cluster_nps = pd.read_excel(cluster_nps_excel_file)

# Adicione uma coluna com a data atual (Cluster e NPS)
df_cluster_nps['data_atualizacao_bd'] = date.today()

# Leitura dos dados da planilha do Excel (CPF Colaboradoras)
df_cpf_colaboradora = pd.read_excel(cpf_colaboradora_excel_file)

# Adicione uma coluna com a data atual (CPF Colaboradoras)
df_cpf_colaboradora['data_atualizacao_bd'] = date.today()

# Leitura dos dados da planilha do Excel (Intercorrências)
df_intercorrencias = pd.read_excel(intercorrencias_excel_file)

# Adicione uma coluna com a data atual (Intercorrências)
df_intercorrencias['data_atualizacao_bd'] = date.today()

# Leitura dos dados da planilha do Excel (Itens)
df_itens = pd.read_excel(itens_excel_file)

# Adicione uma coluna com a data atual (Itens)
df_itens['data_atualizacao_bd'] = date.today()

# Leitura dos dados da planilha do Excel (Metas Colaboradoras)
df_metas_colaboradora = pd.read_excel(metas_colaboradora_excel_file)

# Adicione uma coluna com a data atual (Metas Colaboradoras)
df_metas_colaboradora['data_atualizacao_bd'] = date.today()

# Leitura dos dados da planilha do Excel (Metas Unidades)
df_metas_unidade = pd.read_excel(metas_unidade_excel_file)

# Adicione uma coluna com a data atual (Metas Unidades)
df_metas_unidade['data_atualizacao_bd'] = date.today()

# Leitura dos dados da planilha do Excel (Orçamentos)
df_orcamentos = pd.read_excel(orcamentos_excel_file)

# Adicione uma coluna com a data atual (Orçamentos)
df_orcamentos['data_atualizacao_bd'] = date.today()

# Leitura dos dados da planilha do Excel (Procedimentos)
df_procedimentos = pd.read_excel(procedimentos_excel_file)

# Adicione uma coluna com a data atual (Procedimentos)
df_procedimentos['data_atualizacao_bd'] = date.today()

# Leitura dos dados da planilha do Excel (Recursos Humanos)
df_recursos_humanos = pd.read_excel(recursos_humanos_excel_file)

# Adicione uma coluna com a data atual (Recursos Humanos)
df_recursos_humanos['data_atualizacao_bd'] = date.today()

# Leitura dos dados da planilha do Excel (Vendas)
df_vendas = pd.read_excel(vendas_excel_file)

# Adicione uma coluna com a data atual (Recursos Humanos)
df_vendas['data_atualizacao_bd'] = date.today()

# Conexão com o banco de dados
cnx = mysql.connector.connect(**db_config)
cursor = cnx.cursor()

# Substituir valores NaN por um valor padrão (por exemplo, uma string vazia)
df_agendamentos = df_agendamentos.fillna('')
df_bonificacoes = df_bonificacoes.fillna('')
df_calculo_vendas = df_calculo_vendas.fillna('')
df_clientes = df_clientes.fillna('')
df_cluster_nps = df_cluster_nps.fillna('')
df_cpf_colaboradora = df_cpf_colaboradora.fillna('')
df_intercorrencias = df_intercorrencias.fillna('')
df_itens = df_itens.fillna('')
df_metas_colaboradora = df_metas_colaboradora.fillna('')
df_metas_unidade = df_metas_unidade.fillna('')
df_orcamentos = df_orcamentos.fillna('')
df_procedimentos = df_procedimentos.fillna('')
df_recursos_humanos = df_recursos_humanos.fillna('')
df_vendas = df_vendas.fillna('')

# Ou substituir valores NaN por NULL
df_agendamentos = df_agendamentos.where(pd.notnull(df_agendamentos), None)
df_bonificacoes = df_bonificacoes.where(pd.notnull(df_bonificacoes), None)
df_calculo_vendas = df_calculo_vendas.where(pd.notnull(df_calculo_vendas), None)
df_clientes = df_clientes.where(pd.notnull(df_clientes), None)
df_cluster_nps = df_cluster_nps.where(pd.notnull(df_cluster_nps), None)
df_cpf_colaboradora = df_cpf_colaboradora.where(pd.notnull(df_cpf_colaboradora), None)
df_intercorrencias = df_intercorrencias.where(pd.notnull(df_intercorrencias), None)
df_itens = df_itens.where(pd.notnull(df_itens), None)
df_metas_colaboradora = df_metas_colaboradora.where(pd.notnull(df_metas_colaboradora), None)
df_metas_unidade = df_metas_unidade.where(pd.notnull(df_metas_unidade), None)
df_orcamentos = df_orcamentos.where(pd.notnull(df_orcamentos), None)
df_procedimentos = df_procedimentos.where(pd.notnull(df_procedimentos), None)
df_recursos_humanos = df_recursos_humanos.where(pd.notnull(df_recursos_humanos), None)
df_vendas = df_vendas.where(pd.notnull(df_vendas), None)

# Inserção dos dados na tabela do banco de dados (Agendamentos)
for _, row in df_agendamentos.iterrows():
    columns = ['data_agendada', 'hora_agendada', 'data_criacao', 'hora_criacao', 'unidade', 'localidade',
               'status', 'cliente', 'colaboradora', 'cpf_colaboradora', 'perfil', 'item', 'origem_contrato',
               'origem_cliente', 'origem_agendamento', 'quantidade', 'data_atualizacao_bd']
    placeholders = ', '.join(['%s'] * len(columns))
    query = f"INSERT INTO {agendamentos_db_table} ({', '.join(columns)}) VALUES ({placeholders})"
    values = tuple(row[column] for column in columns)
    cursor.execute(query, values)

# Inserção dos dados na tabela do banco de dados (Bonificações)
for _, row in df_bonificacoes.iterrows():
    columns = ['unidade', 'colaboradora', 'cpf_colaboradora', 'mes', 'total_bonificacao', 'data_atualizacao_bd']
    placeholders = ', '.join(['%s'] * len(columns))
    values = []
    for column in columns:
        value = row[column]
        if pd.isnull(value) or value == '':
            value = None  # Substitui valor vazio por NULL
        values.append(value)
    query = f"INSERT INTO {bonificacoes_db_table} ({', '.join(columns)}) VALUES ({placeholders})"
    cursor.execute(query, values)

# Inserção dos dados na tabela do banco de dados (Calculo de Vendas)
for _, row in df_calculo_vendas.iterrows():
    columns = ['id_orc', 'orcamento', 'tipo_de_orcamento', 'contrato', 'tipo', 'mes', 'unidade', 'cliente',
               'gerente_de_campo', 'regional', 'item', 'colaboradora', 'perfil', 'cpf_colaboradora',
               'valor_da_taxa', 'v_bruto', 'v_desconto_1', 'v_liquido', 'dia', 'forma_de_pagamento',
               'condicao_de_pagamento', 'ano', 'data_venda', 'data_avaliacao', 'data_1_compra',
               'diferenca_avaliacao_venda', 'diferenca_1_venda_venda', 'classificacao_venda',
               'data_atualizacao_bd']
    placeholders = ', '.join(['%s'] * len(columns))
    values = []
    for column in columns:
        value = row[column]
        if pd.isnull(value) or value == '':
            value = None  # Substitui valor vazio por NULL
        values.append(value)
    query = f"INSERT INTO {calculo_vendas_db_table} ({', '.join(columns)}) VALUES ({placeholders})"
    cursor.execute(query, values)

# Inserção dos dados na tabela do banco de dados (Clientes)
for _, row in df_clientes.iterrows():
    columns = ['id_cliente', 'nome', 'apelido', 'cpfcnpj', 'genero', 'telefone', 'email', 'unidade', 'cep', 'endereco',
               'bairro', 'numero', 'cidade', 'estado', 'inativo', 'midia', 'sistema_proprietario', 'data_cadastro',
               'hora_cadastro', 'ultima_alteracao_data', 'ultima_alteracao_hora', 'data_atualizacao_bd']
    placeholders = ', '.join(['%s'] * len(columns))
    values = []
    for column in columns:
        value = row[column]
        if pd.isnull(value) or value == '':
            value = None  # Substitui valor vazio por NULL
        values.append(value)
    query = f"INSERT INTO {clientes_db_table} ({', '.join(columns)}) VALUES ({placeholders})"
    cursor.execute(query, values)

# Inserção dos dados na tabela do banco de dados (Cluster e NPS)
for _, row in df_cluster_nps.iterrows():
    columns = ['mes', 'unidade', 'numero_lojas', 'posicao', 'calculo', 'nota_cluster', 'nota_nps', 'data_atualizacao_bd']
    placeholders = ', '.join(['%s'] * len(columns))
    values = []
    for column in columns:
        value = row[column]
        if pd.isnull(value) or value == '':
            value = None  # Substitui valor vazio por NULL
        values.append(value)
    query = f"INSERT INTO {cluster_nps_db_table} ({', '.join(columns)}) VALUES ({placeholders})"
    cursor.execute(query, values)

# Inserção dos dados na tabela do banco de dados (CPF Colaboradoras)
for _, row in df_cpf_colaboradora.iterrows():
    columns = ['colaboradora', 'cpf_colaboradora', 'data_atualizacao_bd']
    placeholders = ', '.join(['%s'] * len(columns))
    values = []
    for column in columns:
        value = row[column]
        if pd.isnull(value) or value == '':
            value = None  # Substitui valor vazio por NULL
        values.append(value)
    query = f"INSERT INTO {cpf_colaboradora_db_table} ({', '.join(columns)}) VALUES ({placeholders})"
    cursor.execute(query, values)

# Inserção dos dados na tabela do banco de dados (Intercorrências)
for _, row in df_intercorrencias.iterrows():
    columns = ['data_da_intercorrencia', 'hora_da_intercorrencia','unidade_registro', 'unidade_seessao', 'cliente',
               'documento', 'tipo_intercorrencia', 'grau', 'area', 'sessao', 'data_sessao', 'profissional_sessao',
               'cpf_colaboradora', 'potencia', 'recurso_utilizado', 'data_alta', 'area_bloqueada',
               'usuario_registro', 'descricao_1_registro', 'situacao_intercorrencia',
               'profissional_alta', 'data_alta_efetiva', 'data_atualizacao_bd']
    placeholders = ', '.join(['%s'] * len(columns))
    values = []
    for column in columns:
        value = row[column]
        if pd.isnull(value) or value == '':
            value = None  # Substitui valor vazio por NULL
        values.append(value)
    query = f"INSERT INTO {intercorrencias_db_table} ({', '.join(columns)}) VALUES ({placeholders})"
    cursor.execute(query, values)

# Inserção dos dados na tabela do banco de dados (Itens)
for _, row in df_itens.iterrows():
    columns = ['itens', 'indice', 'sexo', 'area', 'regiao', 'p_m_g', 'intervalo_entre_sessoes', 'duracao_sessao_minutos',
               'tempo_medio_preparo', 'data_atualizacao_bd']
    placeholders = ', '.join(['%s'] * len(columns))
    values = []
    for column in columns:
        value = row[column]
        if pd.isnull(value) or value == '':
            value = None  # Substitui valor vazio por NULL
        values.append(value)
    query = f"INSERT INTO {itens_db_table} ({', '.join(columns)}) VALUES ({placeholders})"
    cursor.execute(query, values)

# Inserção dos dados na tabela do banco de dados (Metas Colaboradoras)
for _, row in df_metas_colaboradora.iterrows():
    columns = ['unidade', 'colaboradora', 'cpf_colaboradora', 'cargo', 'mes', 'meta_1_dezena', 'super_1_dezena',
               'hiper_1_dezena', 'meta_2_dezena', 'super_2_dezena', 'hiper_2_dezena', 'meta_3_dezena',
                'super_3_dezena', 'hiper_3_dezena', 'total_meta', 'total_super', 'total_hiper', 'data_atualizacao_bd']
    placeholders = ', '.join(['%s'] * len(columns))
    values = []
    for column in columns:
        value = row[column]
        if pd.isnull(value) or value == '':
            value = None  # Substitui valor vazio por NULL
        values.append(value)
    query = f"INSERT INTO {metas_colaboradora_db_table} ({', '.join(columns)}) VALUES ({placeholders})"
    cursor.execute(query, values)

# Inserção dos dados na tabela do banco de dados (Metas Unidades)
for _, row in df_metas_unidade.iterrows():
    columns = ['mes', 'unidade', 'meta_loja', 'super_loja', 'hiper_loja', 'meta_1_dezena', 'super_1_dezena',
               'hiper_1_dezena', 'meta_2_dezena', 'super_2_dezena', 'hiper_2_dezena', 'meta_3_dezena',
               'super_3_dezena', 'hiper_3_dezena', 'data_atualizacao_bd']
    placeholders = ', '.join(['%s'] * len(columns))
    values = []
    for column in columns:
        value = row[column]
        if pd.isnull(value) or value == '':
            value = None  # Substitui valor vazio por NULL
        values.append(value)
    query = f"INSERT INTO {metas_unidade_db_table} ({', '.join(columns)}) VALUES ({placeholders})"
    cursor.execute(query, values)

# Inserção dos dados na tabela do banco de dados (Orçamentos)
for _, row in df_orcamentos.iterrows():
    columns = ['unidade', 'cnpj', 'tipo', 'data_criacao', 'hora_criacao', 'data_cancelamento', 'contrato', 'codigo',
               'item', 'colaboradora', 'cpf_colaboradora', 'genero', 'cliente', 'cpf_cliente', 'midia_cliente',
               'data_cadastro_cliente', 'hora_cadastro_cliente', 'midia_contrato', 'quantidade', 'quantidade_itens',
               'status_orcamento', 'valor_bruto_item', 'valor_liquido_item', 'valor_bruto_contrato',
               'valor_liquido_contrato', 'data_pagamento', 'hora_pagamento', 'sistema_proprietario',
               'data_atualizacao_bd']
    placeholders = ', '.join(['%s'] * len(columns))
    values = []
    for column in columns:
        value = row[column]
        if pd.isnull(value) or value == '':
            value = None  # Substitui valor vazio por NULL
        values.append(value)
    query = f"INSERT INTO {orcamentos_db_table} ({', '.join(columns)}) VALUES ({placeholders})"
    cursor.execute(query, values)

# Inserção dos dados na tabela do banco de dados (Procedimentos)
for _, row in df_procedimentos.iterrows():
    columns = ['unidade', 'data', 'hora', 'colaboradora', 'duracao_procedimento', 'cpf_colaboradora', 'cliente',
               'item', 'localidade', 'tempo', 'informacoes', 'observaoces_tecnicas', 'observacoes_gerais', 'status',
               'data_atualizacao_bd']
    placeholders = ', '.join(['%s'] * len(columns))
    values = []
    for column in columns:
        value = row[column]
        if pd.isnull(value) or value == '':
            value = None  # Substitui valor vazio por NULL
        values.append(value)
    query = f"INSERT INTO {procedimentos_db_table} ({', '.join(columns)}) VALUES ({placeholders})"
    cursor.execute(query, values)

# Inserção dos dados na tabela do banco de dados (Recursos Humanos)
for _, row in df_recursos_humanos.iterrows():
    columns = ['unidade', 'colaboradora', 'cpf_colaboradora', 'cargo', 'mes', 'data_atualizacao_bd']
    placeholders = ', '.join(['%s'] * len(columns))
    values = []
    for column in columns:
        value = row[column]
        if pd.isnull(value) or value == '':
            value = None  # Substitui valor vazio por NULL
        values.append(value)
    query = f"INSERT INTO {recursos_humanos_db_table} ({', '.join(columns)}) VALUES ({placeholders})"
    cursor.execute(query, values)

# Inserção dos dados na tabela do banco de dados (Vendas)
for _, row in df_vendas.iterrows():
    columns = ['id_orc', 'cod_externo', 'orcamento', 'tipo_orcamento', 'contrato', 'tipo', 'origem_midia', 'mes',
               'data', 'unidade', 'gerente_de_campo', 'regional', 'cliente', 'item', 'estabelecimento_origem',
               'ecommerce', 'valor_gift_card', 'utilizacao_gift_card', 'colaboradora', 'perfil', 'cpf_colabodora',
               'precisa_aprovacao', 'cortesia', 'nome_campanha', 'codigo_voucher', 'descricao_voucher',
               'valor_desconto', 'motor_promocoes', 'valor_taxa', 'valor_bruto','valor_desconto_1', 'valor_liquido',
               'forma_pagamento', 'condicao_pagamento', 'data_atualizacao_bd']
    placeholders = ', '.join(['%s'] * len(columns))
    values = []
    for column in columns:
        value = row[column]
        if pd.isnull(value) or value == '':
            value = None  # Substitui valor vazio por NULL
        values.append(value)
    query = f"INSERT INTO {vendas_db_table} ({', '.join(columns)}) VALUES ({placeholders})"
    cursor.execute(query, values)

# Commit das alterações e fechamento da conexão
cnx.commit()
cursor.close()
cnx.close()

# Função para ser executada diariamente
def tarefa_diaria():
    print("Executando tarefa diária...")
    # Coloque aqui a lógica da função para atualizar os dados, se necessário

# Agendar tarefa diária
schedule.every().day.at('11:39').do(tarefa_diaria)

# Loop para executar tarefas agendadas
while True:
    schedule.run_pending()
    time.sleep(1)
