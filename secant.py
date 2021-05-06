import math

def secant(a: float, b: float, tol: float) -> float:
    x0 = a
    x1 = b
    x2 = x1 - ((x1 - x0) * fn(x1)) / (fn(x1) - fn(x0))
    k = 1
    print("k: {3}: x0 = {0}, x1 = {1}, x2 ={2}".format(x0, x1, x2, k))

    while abs(x2 - x1) >= tol:
        x0 = x1
        x1 = x2
        x2 = x1 - ((x1 - x0) * fn(x1)) / (fn(x1) - fn(x0))
        k = k + 1
        print("k: {3}: x0 = {0}, x1 = {1}, x2 ={2}".format(x0, x1, x2, k))

    print("Result: {0}, k: {1}".format(x2, k))


if __name__ == "__main__":
    def fn(c: float) -> float:
        # res = math.pow(c, 3) - c - 1 
        # res = math.pow(2, -c) - c
        res = 1.0 + math.sin(c) - 2 * math.cos(c)
        print("res:", res)
        return res

    # a = float(input("a:"))
    # b = float(input("b:"))
    # tol = float(input("tol:"))
    a = float(0)
    b = float(math.pi / 4)
    tol = float("1e-8")
    print("a: {0}\tb: {1}\ttol: {2}".format(a, b, tol))
    secant(a, b, tol)
