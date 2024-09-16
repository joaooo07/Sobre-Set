#Criar um conjunto vazio:
my_set = set()
#Criar um conjunto a partir de uma lista:
my_list = [1, 2, 2, 3, 4, 4, 5]
my_set = set(my_list)
print(my_set)  # {1, 2, 3, 4, 5}

#Adicionar elementos a um conjunto:
my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(3)
print(my_set)  # {1, 2, 3}

#Remover elementos de um conjunto:
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
print(my_set)  # {1, 2, 4, 5}

#Verificar se um elemento está presente em um conjunto:
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)  # True
print(6 in my_set)  # False

#Unir dois conjuntos:
my_set1 = {1, 2, 3}
my_set2 = {3, 4, 5}
print(my_set1.union(my_set2))  # {1, 2, 3,4,5,}

#Interseção de dois conjuntos:
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)
print(intersection_set)  # {3}

#Diferença entre dois conjuntos:
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
print(difference_set)  # {1, 2}


