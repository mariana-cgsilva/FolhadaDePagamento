funcionarios = {}
abrir_menu = 'aberto'
def inicio(funcionarios,abrir_menu):
    while abrir_menu=='aberto':
        print('-' * 88)
        print(f"|{'MENU':^86}|")
        print('-' * 88)
        print(f"|{'1. Inserir Funcionários':^86}|")
        print('-' * 88)
        print(f"|{'2. Remover Funcionários':^86}|")
        print('-' * 88)
        print(f"|{'3. Determinar a folha de pagamento de um determinado funcionário':^86}|")
        print('-' * 88)
        print(f"|{'4. Determinar um relatório com o salário bruto e líquido de todos os funcionários':^86}|")
        print('-' * 88)
        print(f"|{'5. Imprimir as informações do funcionário com maior salário líquido':^86}|")
        print('-' * 88)
        print(f"|{'6. Imprimir as informações do funcionário com o maior número de faltas no mês':^86}|")
        print('-' * 88)
        print(f"|{'7. Sair':^86}|")
        print('-' * 88)
        print()

        opcao = input("Escolha uma opção: ")
        print()
        
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
            break
        else:
            print("Opção inválida. Tente novamente.")
    
        opcao2 = input('\nDeseja abrir o menu novamente? (s/n): ')
        if opcao2.lower() != 's':
            abrir_menu = 'fechado'


def inserir_funcionario(funcionarios):
    matricula = int(input("Digite a matrícula: "))
    while matricula in funcionarios.keys():
        print("Já existe um funcionário com essa matrícula. Por favor, insira uma matrícula diferente.")
        matricula = int(input("Digite a matrícula: "))
    if matricula not in funcionarios.keys():

        nome = input("Digite o nome: ")
        cod_funcao = int(input("Informe o código da função (101 ou 102): "))
        while cod_funcao != 101 and cod_funcao != 102:
            print("Código de função inválido. Por favor, insira novamente.")
            cod_funcao = int(input("Informe o código da função (101 ou 102): "))
        
        num_falta = int(input("Informe as faltas no mês: "))
    
        if cod_funcao == 101:
            vol_vendas = float(input("Informe o volume de vendas do mês: "))
            sal_fixo = 1500
            sal_bruto = sal_fixo - (1500/30) * num_falta + (vol_vendas * 0.09) 
        elif cod_funcao == 102:
            sal_fixo = float(input("Informe o salário fixo: "))
            sal_bruto = sal_fixo - (sal_fixo/30) * num_falta
    
        
        
    if sal_bruto <= 2259.20:
        percentual_imposto = 0
    elif sal_bruto >= 2259.65 and sal_bruto <= 2828.65:
        percentual_imposto = 7.5
    elif sal_bruto >= 2828.65 and sal_bruto <= 3751.05:
        percentual_imposto = 15
    elif sal_bruto >= 3751.05 and sal_bruto <= 4664.68:
        percentual_imposto = 22.5
    elif sal_bruto >= 4664.69:
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
    matricula = int(input("Matrícula do funcionário que deseja procurar: "))
    print()
    if matricula in funcionarios:
        funcionario = funcionarios[matricula]
        salario_liquido = calcular_imposto(funcionario)
        print("Folha de Pagamento do funcionário")
        print('-' * 40)
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
    
    print(f"{'Matrícula':<10} | {'Nome':<20} | {'Código da Função':<16} | {'Salário Bruto':<14} | {'Salário Líquido':<15}")
    print("-" * 80)
    for matricula in funcionarios:
        funcionario = funcionarios[matricula]
        salario_liquido = calcular_imposto(funcionario)
        print(f"{funcionario['matricula']:<10} | {funcionario['nome']:<20} | {funcionario['codigo_funcao']:<16} | {funcionario['salario_bruto']:<14.2f} | {salario_liquido:<15.2f}")


def funcionario_maior_salario(funcionarios):
    if len(funcionarios) == 0:
        print("Nenhum funcionário cadastrado.")
        return
    funcionario_maior_salario_liquido = None
    maior_salario_liquido = -1
    
    for matricula in funcionarios.keys():
        funcionario = funcionarios[matricula]
        salario_liquido = calcular_imposto(funcionario)
        if salario_liquido > maior_salario_liquido:
            funcionario_maior_salario_liquido = funcionario
            maior_salario_liquido = salario_liquido
    
    if funcionario_maior_salario_liquido!=None:
        print("Funcionário com maior salário")
        print('-' * 40)
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
    
    if funcionario_maior_numero_faltas!=None:
        desconto_faltas = funcionario_maior_numero_faltas["faltas"] * (funcionario_maior_numero_faltas["salario_bruto"] / 30)
        print("Funcionário com mais faltas")
        print('-' * 40)
        print(f"Matrícula: {funcionario_maior_numero_faltas['matricula']}")
        print(f"Nome: {funcionario_maior_numero_faltas['nome']}")
        print(f"Código da Função: {funcionario_maior_numero_faltas['codigo_funcao']}")
        print(f"Número de Faltas: {funcionario_maior_numero_faltas['faltas']}")
        print(f"Desconto no Salário: {desconto_faltas:.2f}")

def calcular_imposto(funcionario):
    imposto = funcionario["salario_bruto"] * (funcionario["percentual_imposto"] / 100)
    salario_liquido = funcionario["salario_bruto"] - imposto
    return round(salario_liquido, 2)

def imprimir_info_funcionario(funcionario, salario_liquido):
    print(f"Matrícula: {funcionario['matricula']}")
    print(f"Nome: {funcionario['nome']}")
    print(f"Código da Função: {funcionario['codigo_funcao']}")
    print(f"Salário Bruto: {funcionario['salario_bruto']:.2f}")
    print(f"Percentual de Imposto: {funcionario['percentual_imposto']}%")
    print(f"Salário Líquido: {salario_liquido}")
    
    
inicio(funcionarios,abrir_menu)
