class Operasi:
    operator= 0
    def __init__(self,operan):
        Operasi.operator= operan

    @staticmethod
    def kali(bilangan):
        return f"{Operasi.operator} X {bilangan} = {Operasi.operator*bilangan}"
    
    @classmethod
    def kuadrat(cls):
        return f"{cls.operator}^2 = {cls.operator**2}"

    @property
    def kubik(self):
        return f"{self.operator}^3 = {self.operator**3}"
    

angka= Operasi(4)

print(angka.kali(2))
print(angka.kuadrat())
print(angka.kubik)





