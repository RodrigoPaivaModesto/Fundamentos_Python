#maiuscula, minuscula, titulo


nome = 'roDrIgo'


print(nome.upper())
print(nome.lower())
print(nome.title())



#eliminando espaços em branco

texto = '    olá mundo       '

print(texto + '.')
print(texto.strip() + '.')
print(texto.rstrip() + '.')
print(texto.lstrip() + '.')


#junção e centralização


menu = 'girafas'

print('####' + menu + '####')
print(menu.center(20))
print(menu.center(20, '#'))


print('-'.join(menu))
