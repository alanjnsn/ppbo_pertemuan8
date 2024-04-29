from collections import namedtuple

Koordinat= namedtuple('Koordinat',['x','y'])

titik1= Koordinat(x=2, y=4)
# menggunakan indeks dan nama
print()
print(f"absis: {titik1[0]}")
print(f"ordinat: {titik1.y}")
# menggunakan getattr
print(f"absis: {getattr(titik1,'x')}")
print(f"ordinat: {getattr(titik1,'y')}")