funcionario=[]

matricula = int(input("Digite a matricula: "))
nome= input("Digite o nome: ")
cod_funcao = int(input("Informe o código da função: "))
num_falta = int(input("Informe as faltas no mês: "))
if cod_funcao == 101:
    vol_vendas = float(input("Informe o volume de vendas do mês: "))
    sal_bruto = 1500 + (vol_vendas*(9/100))
elif cod_funcao == 102:
    sal_admin = float(input("Informe o salário: "))
    for i in range(num_falta):
        sal_bruto = sal_admin - (sal_admin/30)
if sal_bruto <= 2259.20:
    print("Isento de impostos!")
elif sal_bruto >= 2259.21 and sal_bruto<= 2828.65:
    sal_bruto = sal_bruto- 75/100
    print("Imposto de 7,5%!")
