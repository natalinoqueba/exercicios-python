# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (
# 50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
# variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do
# limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens
# adequadas

ppeixe = float(input('Introduza o peso(em kg) de peixes: '))
excesso = ppeixe - 50
multa = excesso * 4.00
print(f'\nO peso de peixes e {ppeixe}kg; \nTem {excesso}kg de execesso; \nA multa a pagar sera de {multa}MT.')
print(
    '\n\nNB: Se obteve valores negativos no excesso e na multa entao o peso do peixe esta dentro do limite estabelecido')
