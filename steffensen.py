import math

def steffensen(x0: float, tol: float) -> float:
    k = 1
    y0 = fn(x0)
    x1 = x0 - (y0 ** 2) / (y0 - fn(x0 - y0))
    while abs(x1 - x0) >= tol:
        x0 = x1
        y0 = fn(x0)
        x1 = x0 - (y0 ** 2) / (y0 - fn(x0 - y0))
        k = k + 1

    print("Result: {0}, k: {1}".format(x1, k))


if __name__ == "__main__":
    def fn(c: float) -> float:
        # res = math.pow(c, 3) - c - 1 
        # res = math.pow(2, -c) - c
        res = 1.0 + math.sin(c) - 2 * math.cos(c)
        print("res:", res)
        return res

    # x0 = float(1)
    x0 = float(math.pi / 8)
    tol = float("1e-8")
    print("x0: {0}\ttol: {1}".format(x0, tol))
    steffensen(x0, tol)
