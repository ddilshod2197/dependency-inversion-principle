class InterfaceSegregationPrinciple:
    def __init__(self):
        pass

    def isp(self):
        return "Interface Segregation Principle"

class Klient:
    def __init__(self, isp):
        self.isp = isp

    def ishlat(self):
        print(self.isp.isp())

class Arxitektor:
    def __init__(self, isp):
        self.isp = isp

    def loyihalash(self):
        print(self.isp.isp())

isp = InterfaceSegregationPrinciple()
klient = Klient(isp)
arxitektor = Arxitektor(isp)

klient.ishlat()
arxitektor.loyihalash()
```

```python
# Interface Segregation Principle (ISP) ni amalga oshirish uchun quyidagi kodni yozing:
class ISP:
    def __init__(self):
        pass

    def metod1(self):
        pass

    def metod2(self):
        pass

class Klient(ISP):
    def __init__(self):
        super().__init__()

    def ishlat(self):
        self.metod1()
        self.metod2()

class Arxitektor(ISP):
    def __init__(self):
        super().__init__()

    def loyihalash(self):
        self.metod1()
        # self.metod2()  # metod2 mavjud emas, lekin bizga kerak bo'lsa, uni qo'shish mumkin

isp = ISP()
klient = Klient()
arxitektor = Arxitektor()

klient.ishlat()
arxitektor.loyihalash()
