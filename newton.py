import math

def newton(x0: float, tol: float) -> float:
    k = 1
    x1 = x0 - fn(x0) / fn1(x0)

    while abs(x1 - x0) >= tol:
        x0 = x1
        x1 = x0 - fn(x0) / fn1(x0)
        k = k + 1

    print("Result: {0}, k: {1}".format(x1, k))


if __name__ == "__main__":
    def fn(c: float) -> float:
        res = 2 * math.sin(c + math.pi / 3) - c
        print("res:", res)
        return res

    def fn1(c: float) -> float:
        res = 2 * math.cos(c + math.pi / 3) - 1
        print("res 导数:", res)
        return res

    # x0 = float(1)
    x0 = float(0)
    tol = float("1e-8")
    print("x0: {0}\ttol: {1}".format(x0, tol))
    newton(x0, tol)
