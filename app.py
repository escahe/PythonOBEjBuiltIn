from functools import reduce
paises = list(set(input('Digite paises separados por coma: ').split(',')))
paises.sort()
paises = reduce(lambda p1,p2: p1+', '+p2,paises)
print(f'Paises ordenados y sin repetir:{paises}')