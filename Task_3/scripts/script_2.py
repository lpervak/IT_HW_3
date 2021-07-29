from math import sqrt

a = int(input("Enter side A: "))
b = int(input("Enter side B: "))
c = 0


def decor(pythagorean_theorem):
    def wrap(*args, **kwargs):
        result = pythagorean_theorem(*args, **kwargs)
        print("With sides", a, "and", b, "side C is:", result)
        return result
    return wrap


@decor
def pythagorean_theorem_():
    c = sqrt(a * a + b * b)
    return c


print(pythagorean_theorem_())
