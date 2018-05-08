numbertypes = (int, float, complex)


class Calc:

    @staticmethod
    def args(x, y):
        if not isinstance(x, numbertypes) and not isinstance(y, numbertypes):
            raise ValueError

    def addition(self, x, y):
        self.args(x, y)
        return x + y
    def multiply(self, x, y):
        self.args(x, y)
        return x*y
    def division(self, x, y):
        self.args(x, y)
        return x/y
    def subtraction(self, x, y):
        self.args(x, y)
        return x-y
