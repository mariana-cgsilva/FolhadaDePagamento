# Projeto: A FOLHA DE PAGAMENTO

## IDEIA

Construir um programa simplificado que simule a elaboração da folha de pagamento de uma determinada empresa. O projeto será construído com telas para que se possa atender as necessidades do usuário.

## PROJETO

A empresa “Marketing é Tudo” possui uma quantidade cíclica de funcionários, ou seja, o número varia conforme a época do ano e a quantidade de trabalho.

Cada funcionário possui um número de identificação (matrícula) que é ÚNICO. A empresa “Marketing é Tudo” procurou a sua startup para construir um sistema para a elaboração da folha de pagamento dos seus funcionários.

Para cada funcionário existem as seguintes informações:
- Matrícula
- Nome
- Código da função:
  - 101 – Vendedor
  - 102 – Administrativo
- Número de faltas no mês
- Salário Bruto

O salário BRUTO depende do tipo da função do funcionário.
- Se o funcionário é Vendedor ele possui um salário fixo mais uma comissão de 9% pelo volume de vendas no mês. O salário fixo do vendedor é sempre de R$1500,00
- Se o funcionário é da Área Administrativa o salário é fixo e varia entre R$2150,00 até R$6950,00

Se o funcionário falta o seu salário sofre um desconto em função do número de faltas. Considere que para cada falta o valor do desconto é de (salario fixo)/30. As faltas são descontadas do Salário Bruto.

Percentual do Imposto – para determinar o Salário Líquido descontar o valor do imposto é obtido pela tabela abaixo:
![image](https://github.com/mariana-cgsilva/FolhadaDePagamento/assets/142249220/242e583f-eb2d-481f-8448-ff6439fe6a02)

Deseja-se um sistema que a empresa possa efetuar as seguintes operações:
1. Inserir Funcionários
2. Remover Funcionários
3. Determinar a folha de pagamento de um determinado funcionário:
   - Esta opção deverá imprimir todas as informações sobre o funcionário incluindo o valor do percentual do imposto.
4. Determinar um relatório com o salário bruto e líquido de todos os funcionários:
   - Esta opção deverá imprimir uma tabela contendo a Matrícula, Nome, Código da Função, Salário Bruto e Salário Líquido de cada funcionário.
5. Imprimir as informações do funcionário com maior salário líquido:
   - Esta opção deverá imprimir Matrícula, Nome, Código da Função, salário bruto, percentual de imposto e salário líquido.
6. Imprimir as informações do funcionário com o maior número de faltas no mês:
   - Esta opção deverá imprimir a Matrícula, Nome, Código da Função, Número de Faltas e desconto no salário do funcionário.



