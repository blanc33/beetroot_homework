class Fraction:

    def __init__(self, a, b):
        if b == 0:
            raise ValueError
        if not (isinstance(a, int) and isinstance(b, int)):
            raise TypeError
        self.a = a
        self.b = b
        self.frac = (self.a, self.b)

    def __repr__(self):
        return f'{self.frac}'

    def __add__(self, other):
        if self.b % other.b == 0:
            a = other.a * self.b / other.b
            return (int(self.a + a), int(self.b))
        elif other.b % self.b == 0:
            a = self.a * other.b / self.b
            return (int(a + other.a), int(other.b))
        else:
            sa = self.a * other.b
            oa = other.a * self.b
            return (sa + oa, int(other.b*self.b))

    def __sub__(self, other):
        if self.b % other.b == 0:
            a = other.a * self.b / other.b
            return (int(self.a - a), int(self.b))
        elif other.b % self.b == 0:
            a = self.a * other.b / self.b
            return (int(a - other.a), int(other.b))
        else:
            sa = self.a * other.b
            oa = other.a * self.b
            return (sa - oa, int(other.b * self.b))

    def __mul__(self, other):
        return (self.a * other.a, self.b * other.b)

    def __truediv__(self, other):
        a = other.b
        b = other.a
        if self.a * a % (self.b * b) == 0:
            return (int(self.a * a / (self.b * b)), 1)
        else:
            if self.b*b % (self.a * a) == 0:
                return (1, int(self.b*b / (self.a * a)))
            else:
                return (self.a * a, self.b * b)

    def __eq__(self, other):
        if self.a == other.a and self.b == other.b:
            print(self.a == other.a)
            return True
        else:
            return False

x = Fraction(1, 2)
y = Fraction(1, 2)
print((x + y))
print(y - x)
print(x * y)
print(y / x)
x == y