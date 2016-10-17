Atributos da lista
- list.append(x)
- list.extend(L)
- list.insert(i, x)
- list.remove(x)
- list.pop([i])
- list.clear()
- list.index(x)
- list.count(x)
- list.sort(key=None, reverse=False)
- list.reverse()
- list.copy()

Pode-se usar listas como pilhas:
- list.append(x)
- list.pop()

Pode-se usar listas como filas:
- from collections import deque
- fila = deque([1,2,3])
- fila.append(4)
- fila.popleft(1)

Criação de listas:
- squares = list(map(lambda x: x**2, range(10)))
- squares = [x**2 for x in range(10)]

Listas aninhadas
- matrix = [ [1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12] ]
