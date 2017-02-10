tictactoe = [['_', '_', '_'],['_', '_', '_'],['_', '_', '_']]
dic_tictactoe = {}

def dicio():
	global dic_tictactoe
	dic_tictactoe = {1:tictactoe[0][0], 2:tictactoe[0][1], 3: tictactoe[0][2], 4:tictactoe[1][0], 5:tictactoe[1][1], 
6:tictactoe[1][2], 7:tictactoe[2][0], 8:tictactoe[2][1], 9:tictactoe[2][2]}

def tela():
	'''
	Mostra a tela do jogo
	'''
	global tictactoe

	dicio()

	print('%s|%s|%s' %(dic_tictactoe[1], dic_tictactoe[2], dic_tictactoe[3]))
	print('%s|%s|%s' %(dic_tictactoe[4], dic_tictactoe[5], dic_tictactoe[6]))
	print('%s|%s|%s' %(dic_tictactoe[7], dic_tictactoe[8], dic_tictactoe[9]))
'''
def jogada1():
	
	Define a jogada do primeiro jogador (X) e a insere na variável tictactoe
	
	global tictactoe
	linha, coluna = -1, -1
	while linha not in range(0,3) or coluna not in range(0,3) or tictactoe[linha][coluna] != '_':
		linha, coluna = input('Jogador X: insira os valores da jogada: ').split()
		linha, coluna = int(linha), int(coluna)
		if linha not in range(0,3) or coluna not in range(0,3) or tictactoe[linha][coluna] != '_':
			print('Jogada inválida!')

	tictactoe[linha][coluna] = 'X'

	tela()
'''


def jogada1():
	'''
	Define a jogada do primeiro jogador (X) e a insere na variável tictactoe
	'''
	global tictactoe
	valor = 0
	x = 0
	while True:
		valor = int(input('Insira o local da jogada (1 a 9): '))
		if valor not in range(1,10) or dic_tictactoe[valor] != '_':
			print('Jogada inválida!')
		else:
			break

	for linha in range(0,3):
		for coluna in range(0,3):
			x += 1
			if x == valor:
				tictactoe[linha][coluna] = 'X'
	dicio()
	tela()

def jogada2():
	'''
	Define a jogada do primeiro jogador (X) e a insere na variável tictactoe
	'''
	global tictactoe
	valor = 0
	x = 0
	while True:
		valor = int(input('Insira o local da jogada (1 a 9): '))
		if valor not in range(1,10):
			print('Jogada inválida!')
		#elif dic_tictactoe[valor] != '_':
			#print('Jogada inválida 2!')
		else:
			break

	for linha in range(0,3):
		for coluna in range(0,3):
			x += 1
			if x == valor:
				tictactoe[linha][coluna] = 'O'
	dicio()
	tela()

'''
def jogada2():

	
	Define a jogada do segundo jogador (O) e a insere na variável tictactoe

	global tictactoe
	linha, coluna = -1, -1
	while linha not in range(0,3) or coluna not in range(0,3) or tictactoe[linha][coluna] != '_':
		linha, coluna = input('Jogador O: Insira os valores da jogada: ').split()
		linha, coluna = int(linha), int(coluna)
		if linha not in range(0,3) or coluna not in range(0,3) or tictactoe[linha][coluna] != '_':
			print('Jogada inválida!')	

	tictactoe[linha][coluna] = 'O'

	tela()
'''

def vencedor():
	'''Verifica se há um vencedor no jogo e retorna em caso positivo'''
	for x in range(0,3):
		#verifica coluna
		if tictactoe[0][x] != '_' and tictactoe[0][x] == tictactoe[1][x] == tictactoe[2][x]:
			print('Fim de jogo!\nO jogador %s é vencedor!' %tictactoe[0][x])
			return True
		#verifica linha
		if tictactoe[x][1] != '_' and tictactoe[x][0] == tictactoe[x][1] == tictactoe[x][2]:
			print('Fim de jogo!\nO jogador %s é vencedor!' %tictactoe[x][0])
			return True
	#verifica diagonal
	if tictactoe[1][1] != '_' and ((tictactoe[0][0] == tictactoe[1][1] == tictactoe[2][2]) or (tictactoe[2][0] == tictactoe[1][1] == tictactoe[0][2])):
		print('Fim de jogo!\nO jogador %s é vencedor!' %tictactoe[1][1])
		return True
	else:
		return False

def fim_de_jogo():
	'''Verifica se o jogo chegou ao fim'''
	fim = True
	if vencedor() == False:
		for x in range(0,3):
			for y in range(0,3):
				if tictactoe[x][y] == '_':
					fim = False
		empate = 0	
		for x in range(0, 3):
			for y in range(0, 3):
				if tictactoe[x][y] != '_':
					empate += 1
				if empate == 9:
					print("Empate!")
	return fim

dicio()
while True:
	jogada1()
	if fim_de_jogo() == True:
		break
	jogada2()
	if fim_de_jogo() == True: 	
		break
