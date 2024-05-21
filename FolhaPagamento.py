funcionarios = []

while True: 
    matricula = int(input("Digite a matricula: "))
    nome= input("Digite o nome: ")
    cod_funcao = int(input("Informe o código da função (101 - Vendedor; 102 - Administrativo): "))
    num_faltas = int(input("Informe as faltas no mês: "))


    #101 - Vendedor
    if cod_funcao == 101: 
        vol_vendas = float(input("Informe o volume de vendas do mês: "))
        sal_fixo = 1500
        sal_bruto = sal_fixo + (vol_vendas * 0.09)
    #102 - Administrativo
    elif cod_funcao == 102:
        sal_fixo = float(input("Informe o salário fixo: "))
        sal_bruto = sal_fixo

    desconto = (sal_fixo / 30) * num_faltas
    sal_liquido = sal_bruto - desconto

    funcionario = {
        "matricula": matricula,
        "nome": nome,
        "cod_funcao": cod_funcao,
        "num_faltas": num_faltas,
        "sal_bruto": sal_bruto,
        "desconto": desconto,
        "sal_liquido": sal_liquido
    }
        
    funcionarios.append(funcionario)

    continuar = input("Deseja adicionar outro funcionário? (s/n): ")
    if continuar.lower() != 's':
        break

print("\nFolha de Pagamento:")
for f in funcionarios:
    print(f"\nMatrícula: {f['matricula']}")
    print(f"Nome: {f['nome']}")
    print(f"Código da Função: {f['cod_funcao']}")
    print(f"Número de Faltas: {f['num_faltas']}")
    print(f"Salário Bruto: R${f['sal_bruto']:.2f}")
    print(f"Desconto: R${f['desconto']:.2f}")
    print(f"Salário Líquido: R${f['sal_liquido']:.2f}")



'''
if sal_bruto <= 2259.20:
    print("Isento de impostos!")
elif sal_bruto >= 2259.21 and sal_bruto<= 2828.65:
    sal_bruto = sal_bruto- 75/100
    print("Imposto de 7,5%!")
'''


'''
salario mensal ate 2259.20: Isento de impostos
salario mensal de 2259.21 ate 2828.65: Imposto de 7,5%
salario mensal de 2828,66 ate 3751.05: Imposto de 15%
salario mensal de 3751,06 ate 4664,68: Imposto de 22,5%
salario mensal acima de 4664,68: Imposto de 27,5%
'''