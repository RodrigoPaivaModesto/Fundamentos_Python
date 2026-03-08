opção = int(input('informe uma opção: [1] sacar \n[2] extrato: '))

if opção ==1:
    valor = float(input('informe a quantia para o saque: '))
    #...
elif opção ==2:
    print('exibindo o extrato...')
else:
    exit('opção inválida')