# lambda function
numbers = [23, 55, 6, 97, 49]
#filter
print(list(filter(lambda x:x>50,numbers)))

#map
print(list(map(lambda x:x*2,numbers)))

#reduce
from functools import reduce
print(reduce(lambda x, y:x+y,numbers))

#sorted
pokemons = [("Eevee", 55), ("pikachu", 36)]
print(sorted(pokemons, key = lambda pokemons: pokemons[1]))
