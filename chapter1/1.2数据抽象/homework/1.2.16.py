"""
为有理数实现一个不可变数据类型Rational,支持加减乘除操作。
"""
class Rational():
    def __init__(self, numerator, denominator):
        if not (isinstance(numerator, int) or isinstance(denominator, int)):
            raise TypeError("elements in Rational must be an int")
        self.numerator = numerator
        self.denominator = denominator
    
    def __repr__(self):
        return "Rational(%r, %r)" % (self.numerator, self.denominator)

    def __add__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("other must be a Rational")
        min_lcm = self._lcm(self.denominator, other.denominator)
        new_numerator = self.numerator * min_lcm / self.denominator + other.numerator * min_lcm / other.denominator
        new_denominator = min_lcm
        max_gcd = self._gcd(new_numerator, new_denominator)
        new_numerator = int(new_numerator/ max_gcd)
        new_denominator = int(new_denominator/ max_gcd)
        return Rational(new_numerator, new_denominator)
    
    def __mul__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("other must be a Rational")
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        max_gcd = self._gcd(new_numerator, new_denominator)
        new_numerator = int(new_numerator/ max_gcd)
        new_denominator = int(new_denominator/ max_gcd)
        return Rational(new_numerator, new_denominator)
    
    def __sub__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("other must be a Rational")
        min_lcm = self._lcm(self.denominator, other.denominator)
        new_numerator = self.numerator * min_lcm / self.denominator - other.numerator * min_lcm / other.denominator
        if int(new_numerator) == 0:
            return 0
        new_denominator = min_lcm
        max_gcd = self._gcd(new_numerator, new_denominator)
        new_numerator = int(new_numerator/ max_gcd)
        new_denominator = int(new_denominator/ max_gcd)
        return Rational(new_numerator, new_denominator)
    
    def __truediv__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("other must be a Rational")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        max_gcd = self._gcd(new_numerator, new_denominator)
        new_numerator = int(new_numerator/ max_gcd)
        new_denominator = int(new_denominator/ max_gcd)
        return Rational(new_numerator, new_denominator)
    
    def __eq__(self, other):
        if self.denominator * other.numerator == self.numerator * other.denominator:
            return True
        return False
    
    def _gcd(self, a, b):
        if a < b:
            a, b = b, a
        while b != 0:
            a, b = b, a%b
        return a
        
    def _lcm(self, x, y):
        #  获取最大的数
        if x > y:
            greater = x
        else:
            greater = y
        while True:
            if(greater % x == 0) and (greater % y == 0):
                lcm = greater
                break
            greater += 1
        return lcm


if __name__ == "__main__":
    x = Rational(1, 2)
    y = Rational(2, 3)
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print(x == y)


