def buscaBinaria(lista, alvo):
	min = 0
	max = len(lista) - 1
	palpite = None
	while max > min:
		palpite = (max + min) // 2
		if lista[palpite] == alvo :
			print("Numero encontrado")
			return lista[palpite]
		elif lista[palpite] < alvo:
			min = palpite - 1
		else:
			max = palpite + 1
	print("Seu numero nao esta na lista")
	
x = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

z = [1,2,3,4,5,6,7,8,9,10]

print(buscaBinaria(x, 97))
