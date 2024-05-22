funcionarios = {}
def inicio(funcionarios):
    opcao = None
    while opcao != "7":
        print("\nMenu:")
        print("1. Inserir Funcionários")
        print("2. Remover Funcionários")
        print("3. Determinar a folha de pagamento de um determinado funcionário")
        print("4. Determinar um relatório com o salário bruto e líquido de todos os funcionários")
        print("5. Imprimir as informações do funcionário com maior salário líquido")
        print("6. Imprimir as informações do funcionário com o maior número de faltas no mês")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            inserir_funcionario(funcionarios)
        elif opcao == "2":
            remover_funcionario(funcionarios)
        elif opcao == "3":
            folha_pagamento(funcionarios)
        elif opcao == "4":
            relatorio(funcionarios)
        elif opcao == "5":
            funcionario_maior_salario(funcionarios)
        elif opcao == "6":
            funcionario_mais_faltas(funcionarios)
        elif opcao == "7":
            print("Saindo...")
        else:
            print("Opção inválida. Tente novamente.")


def inserir_funcionario(funcionarios):
    matricula = int(input("Digite a matrícula: "))
    nome = input("Digite o nome: ")
    cod_funcao = int(input("Informe o código da função: "))
    num_falta = int(input("Informe as faltas no mês: "))
    
    if cod_funcao == 101:
        vol_vendas = float(input("Informe o volume de vendas do mês: "))
        sal_fixo = 1500
        sal_bruto = sal_fixo + (vol_vendas * 0.09)
    elif cod_funcao == 102:
        sal_fixo = float(input("Informe o salário fixo: "))
        sal_bruto = sal_fixo
    else: 
        print("Código de função inválido. Funcionário não inserido.")
        return
    
    if sal_bruto <= 2259.20:
        percentual_imposto = 0
    elif sal_bruto >= 2828.65 and sal_bruto <= 2828.65:
        percentual_imposto = 7.5
    elif sal_bruto >= 2828.65 and sal_bruto <= 3751.05:
        percentual_imposto = 15
    elif sal_bruto >= 3751.05 and sal_bruto <= 4664.68:
        percentual_imposto = 22.5
    else:
        percentual_imposto = 27.5
    
    funcionario = {
    "matricula": matricula,
    "nome": nome,
    "codigo_funcao": cod_funcao,
    "salario_fixo": sal_fixo,
    "salario_bruto": sal_bruto,
    "faltas": num_falta,
    "percentual_imposto": percentual_imposto
    }
    
    funcionarios[matricula] = funcionario

def remover_funcionario(funcionarios):
    matricula = int(input("Matrícula do funcionário que deseja remover: "))
    if matricula in funcionarios:
        del funcionarios[matricula]
        print("Funcionário removido.")
    else:
        print("Funcionário não encontrado.")

def folha_pagamento(funcionarios):
    matricula = int(input("Matrícula do funcionário: "))
    if matricula in funcionarios:
        funcionario = funcionarios[matricula]
        salario_liquido = calcular_salario_liquido(funcionario)
        print(f"Matrícula: {funcionario['matricula']}")
        print(f"Nome: {funcionario['nome']}")
        print(f"Código da Função: {funcionario['codigo_funcao']}")
        print(f"Salário Bruto: {funcionario['salario_bruto']}")
        print(f"Percentual de Imposto: {funcionario['percentual_imposto']}%")
        print(f"Salário Líquido: {salario_liquido}")
    else:
        print("Funcionário não encontrado.")

def relatorio(funcionarios):
    if len(funcionarios) == 0:
        print("Nenhum funcionário cadastrado.")
        return
    print("Matrícula | Nome | Código da Função | Salário Bruto | Salário Líquido")
    for matricula in funcionarios.keys():
        funcionario = funcionarios[matricula]
        salario_liquido = calcular_salario_liquido(funcionario)
        print(f"{funcionario['matricula']} | {funcionario['nome']} | {funcionario['codigo_funcao']} | {funcionario['salario_bruto']} | {salario_liquido}")

def funcionario_maior_salario(funcionarios):
    if len(funcionarios) == 0:
        print("Nenhum funcionário cadastrado.")
        return
    funcionario_maior_salario_liquido = None
    maior_salario_liquido = -1
    
    for matricula in funcionarios.keys():
        funcionario = funcionarios[matricula]
        salario_liquido = calcular_salario_liquido(funcionario)
        if salario_liquido > maior_salario_liquido:
            funcionario_maior_salario_liquido = funcionario
            maior_salario_liquido = salario_liquido
    
    if funcionario_maior_salario_liquido:
        imprimir_info_funcionario(funcionario_maior_salario_liquido, maior_salario_liquido)

def funcionario_mais_faltas(funcionarios):
    if len(funcionarios) == 0:
        print("Nenhum funcionário cadastrado.")
        return
    funcionario_maior_numero_faltas = None
    maior_numero_faltas = -1
    
    for matricula in funcionarios.keys():
        funcionario = funcionarios[matricula]
        if funcionario["faltas"] > maior_numero_faltas:
            funcionario_maior_numero_faltas = funcionario
            maior_numero_faltas = funcionario["faltas"]
    
    if funcionario_maior_numero_faltas:
        desconto_faltas = funcionario_maior_numero_faltas["faltas"] * (funcionario_maior_numero_faltas["salario_bruto"] / 30)
        print(f"Matrícula: {funcionario_maior_numero_faltas['matricula']}")
        print(f"Nome: {funcionario_maior_numero_faltas['nome']}")
        print(f"Código da Função: {funcionario_maior_numero_faltas['codigo_funcao']}")
        print(f"Número de Faltas: {funcionario_maior_numero_faltas['faltas']}")
        print(f"Desconto no Salário: {desconto_faltas}")

def calcular_salario_liquido(funcionario):
    desconto_faltas = (funcionario["salario_bruto"] / 30) * funcionario["faltas"]
    imposto = funcionario["salario_bruto"] * (funcionario["percentual_imposto"] / 100)
    return funcionario["salario_bruto"] - imposto - desconto_faltas

def imprimir_info_funcionario(funcionario, salario_liquido):
    print(f"Matrícula: {funcionario['matricula']}")
    print(f"Nome: {funcionario['nome']}")
    print(f"Código da Função: {funcionario['codigo_funcao']}")
    print(f"Salário Bruto: {funcionario['salario_bruto']}")
    print(f"Percentual de Imposto: {funcionario['percentual_imposto']}%")
    print(f"Salário Líquido: {salario_liquido}")

inicio(funcionarios)
