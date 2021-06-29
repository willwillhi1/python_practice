# lambda function
numbers = [23, 55, 6, 97, 49]

#filter
print(list(filter(lambda x:x>50,numbers)))
# >>> [55, 97]

#map
print(list(map(lambda x:x*2,numbers)))
# >>> [46, 110, 12, 194, 98]

#reduce
from functools import reduce
print(reduce(lambda x, y:x+y,numbers))
# >>> 230

#sorted
pokemons = [("Eevee", 55), ("pikachu", 36)]
print(sorted(pokemons, key = lambda pokemons: pokemons[1]))
# >>> [('pikachu', 36), ('Eevee', 55)]
