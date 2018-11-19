######################################################
##						     ##
## 	 A U T O R  >>>  L U I S  G U S T A V O      ##
##						     ##
##	 A L G O R I T M O  >>>  L Z W		     ##
##						     ##
######################################################

#NAO PRECISA IMPORTAR

#VARIAVEIS/LISTAS
string_consultada = 'string_consultada NULL'
lista_saida_codificada = []
count = 0
I = ''
C = ''
I_mais_C = ''
zz = 0
ver_tamanho_string = 0
dicionario = {}
z = 0 ## VARIAVEL DO I
lista_saida_codificada_aux = []  #list auxiliar so pra printar
a = ''
var_aux  = 'var_aux NULL'
lista_tabela_simbolos = []
#FIM DE VARIAVEIS/LISTAS
string_consultada = input('Digite sua String:\n')
ver_tamanho_string = int(len(string_consultada))


	
#REMOVENDO VALORES REPETIDOS E ORDENANDO OS PRIMEIROS VALORES NA LISTA :::  lista_tabela_simbolos
for x in range(len(string_consultada)):
    lista_tabela_simbolos.append(string_consultada[x])
	
def remove_repetidos_lista(lista_tabela_simbolos):
    l = []
    for i in lista_tabela_simbolos:
        if i not in l:
            l.append(i)
    l.sort()
    return l
	
lista_tabela_simbolos = remove_repetidos_lista(lista_tabela_simbolos)
	

#ATRIBUINDO A PRIMEIRA EXECUCAO	
I = ''
C = string_consultada[0]
I_mais_C = str(I + C)
print('1 execucao:')
print('I:  (vazio)')
print('C: ', C)
print('I_mais_C: ', I_mais_C)
print('\n\n')

#ATRIBUINDO OS VALORES I, C, I+C ...
for count in range(ver_tamanho_string - 1):
		
	if z == 0:
		I = C
		z = 0
	else:
		I = str(I + C)
		z = 0		
		
	C = string_consultada[count + 1]
	I_mais_C = str(I + C)
	

	if I_mais_C not in lista_tabela_simbolos:		
		lista_tabela_simbolos.append(I_mais_C)
		lista_saida_codificada.append(I)
	else:
		z = 1		
		
	print(count + 2,' execucao:')
	print('I: ', I)
	print('C: ', C)
	print('I_mais_C: ', I_mais_C)
	print('\n\n')
	#FIM DO FOR

	
#ATRIBUINDO A ULTIMA EXECUCAO, CONFORME A REGRINHA ^^
lista_saida_codificada.append(string_consultada[-1])
print(ver_tamanho_string + 1,' execucao:')
print('I: ', string_consultada[-1])
print('C:  (vazio)',)
print('I_mais_C:  (vazio)')
print('\n\n\n\n')
print('Tabela de Simbolos:')
for count_lista in range(len(lista_tabela_simbolos)):
	print(count_lista + 1 ,'  ',lista_tabela_simbolos[count_lista])

count = 0 #ZERAR O count SEMPRE EH BOM NEH  :D

#ATRIBUINDO PESOS, PARA lista_saida_codificada FICAR OKKK
def d(num):
	var_aux = lista_tabela_simbolos[num]	
	zz = 0        
	for x in range(len(lista_saida_codificada)):
		if lista_saida_codificada[x] == var_aux:
			if zz == 0:
				num += 1
				zz = 1
			lista_saida_codificada[x] = str(num)

			
#OBVIAMENTE A STRING VAI TER MENOS DE 999 CARACTERES, ENTAO ESTAMOS TODOS BEM			
for xx in range(999):
	try:
		d(xx)
	except:
		pass
	
print('\nSaida Codificada:')
print(lista_saida_codificada)
