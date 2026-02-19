
nome = input( 'qual seu nome? ')
senha = input( 'qual a sua senha? ')
dominio = input( 'qual seu dominio? ') 
print( 'Ola ' ,nome, ', seja bem vindo ao meu mundo')
print( 'sua senha é: ',senha)
print( 'O seu dominio é: ', dominio)

email = nome + '@' + dominio 
print('Seu email é :', email) 

palavra = 'jaca'
#colocar a string como toda maiuscula
print('colocando o texto em maiuscula: ',palavra.upper())

PALAVRA = 'JACA'
#colocar a string como minuscula 
print('colocando o texto em minuscula: ', PALAVRA.lower())

#contar caracter da string 
palavra_contar = 'nathandosantos147@gmail.com'

print ( 'contar a letra n' , palavra_contar.count('n') )
print ( 'contar a letra a' , palavra_contar.count('a') )
print ( 'contar a letra t' , palavra_contar.count('t') )
print ( 'contar a letra h' , palavra_contar.count('h') )
print ( 'contar a letra a' , palavra_contar.count('a') )
print ( 'contar a letra n' , palavra_contar.count('n') )
print ( 'contar a letra d' , palavra_contar.count('d') )
print ( 'contar a letra o' , palavra_contar.count('o') )
print ( 'contar a letra s' , palavra_contar.count('s') )
print ( 'contar a letra a' , palavra_contar.count('a') )
print ( 'contar a letra n' , palavra_contar.count('n') )
print ( 'contar a letra t' , palavra_contar.count('t') )
print ( 'contar a letra o' , palavra_contar.count('o') )
print ( 'contar a letra s' , palavra_contar.count('s') )
print ( 'contar a letra 1' , palavra_contar.count('1') )
print ( 'contar a letra 4' , palavra_contar.count('4') )
print ( 'contar a letra 7' , palavra_contar.count('7') )
print ( 'contar a letra @' , palavra_contar.count('@') )
print ( 'contar a letra g' , palavra_contar.count('g') )
print ( 'contar a letra m' , palavra_contar.count('m') )
print ( 'contar a letra a' , palavra_contar.count('a') )
print ( 'contar a letra i' , palavra_contar.count('i') )
print ( 'contar a letra l' , palavra_contar.count('l') )
print ( 'contar a letra .' , palavra_contar.count('.') )
print ( 'contar a letra c' , palavra_contar.count('c') )
print ( 'contar a letra o' , palavra_contar.count('o') )
print ( 'contar a letra m' , palavra_contar.count('m') )

x = palavra_contar.count ('x')
print('A letra x foi contada', x)

print (email)
a_c = email.count('a')
e_c = email.count('e')
i_c = email.count('i')
o_c = email.count('o')
u_c = email.count('u')
nova_senha = 'a' + str(a_c) + 'e'+ 'e'+ str(e_c) + 'i'+ str(i_c)+ 'o' + str(o_c) +'U' + str(u_c)
print (nova_senha)



