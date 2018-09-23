def s1(x, y):
    return x*y

class A:

    @staticmethod
    def s1(x, y):
        return x + y

    def s2(self, x, y):
        return s1(x, y)

a = A()
print(a.s2(3, 7))
