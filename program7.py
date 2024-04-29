from collections import namedtuple

Menu = namedtuple("Menu", ['makanan','minuman'])
foodcort= Menu(['ayam geprek','soto','batagor'],['es teh','kopi','es buah'])
print()
print('menu makanan: ',foodcort.makanan)
print('menu minuman: ',foodcort.minuman)
print()
print()
