#interpolação de strings (f string)

nome = 'Rodrigo'
idade = 25
Profissao = 'estagiário'
linguagem = 'fullstack'
saldo = 45.25600

print(f'nome: {nome} idade: {idade} profissão: {Profissao} linguagem: {linguagem} sado: {saldo}')


print(f'nome: {nome} idade: {idade} profissão: {Profissao} linguagem: {linguagem} sado: {saldo:.2f}')
print(f'nome: {nome} idade: {idade} profissão: {Profissao} linguagem: {linguagem} sado: {saldo:10.2f}')
print(f'nome: {nome} idade: {idade} profissão: {Profissao} linguagem: {linguagem} sado: {saldo:10.3f}')



print(f'Me chamo {nome}, tenho {idade} anos e sou {Profissao} aprendendo a ser um programador {linguagem} e tenho um saldo de {saldo:.3f}')