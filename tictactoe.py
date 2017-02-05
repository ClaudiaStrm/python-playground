tictactoe = [['_', '_', '_'],['_', '_', '_'],['_', '_', '_']]

def tela():
	'''
	Mostra a tela do jogo
	'''
	print('%s|%s|%s' %(tictactoe[0][0], tictactoe[0][1], tictactoe[0][2]))
	print('%s|%s|%s' %(tictactoe[1][0], tictactoe[1][1], tictactoe[1][2]))
	print('%s|%s|%s' %(tictactoe[2][0], tictactoe[2][1], tictactoe[2][2]))

def jogada1():
	'''
	Define a jogada do primeiro jogador (X) e a insere na variável tictactoe
	'''
	global tictactoe
	linha, coluna = -1, -1
	while linha not in range(0,3) or coluna not in range(0,3) or tictactoe[linha][coluna] != '_':
		linha, coluna = input('Jogador X: insira os valores da jogada: ').split()
		linha, coluna = int(linha), int(coluna)
		if linha not in range(0,3) or coluna not in range(0,3) or tictactoe[linha][coluna] != '_':
			print('Jogada inválida!')

	tictactoe[linha][coluna] = 'X'

	tela()

def jogada2():

	'''
	Define a jogada do segundo jogador (O) e a insere na variável tictactoe
	'''
	global tictactoe
	linha, coluna = -1, -1
	while linha not in range(0,3) or coluna not in range(0,3) or tictactoe[linha][coluna] != '_':
		linha, coluna = input('Jogador O: Insira os valores da jogada: ').split()
		linha, coluna = int(linha), int(coluna)
		if linha not in range(0,3) or coluna not in range(0,3) or tictactoe[linha][coluna] != '_':
			print('Jogada inválida!')	

	tictactoe[linha][coluna] = 'O'

	tela()

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
	return fim

while True:
	jogada1()
	if fim_de_jogo() == True:
		break
	jogada2()
	if fim_de_jogo() == True:
		break
empate = 0
for x in range(0, 3):
	for y in range(0, 3):
		if tictactoe[x][y] != '_':
			empate += 1
		if empate == 9:
			print("Empate!")