class Complex():
    def __init__(self, x, y):
        self.a = x
        self.b = y
        self.string = str(x) +" + "+str(y)+"i"

    def print(self):
        print(self.string)

    def __add__(self, other):
        self.newA = self.a + other.a
        self.newB = self.b + other.b
        h = Complex(self.newA, self.newB)
        return h.string
    def __sub__(self, other):
        self.newA = self.a - other.a
        self.newB = self.b - other.b
        h = Complex(self.newA, self.newB)
        return h.string 
    def __mul__(self, other):
        self.newA = self.a * other.a - self.b * other.b 
        self.newB = self.a * other.b + self.b * other.a
        h = Complex(self.newA, self.newB)
        return h.string  


if __name__ == "__main__":
    a = Complex(1,2)
    b = Complex(3,4)
    c = a * b
    print(c)
    