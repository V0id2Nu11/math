import math

def half(a: float, b: float, tol: float) -> float:
    c = (a + b) / 2
    # 计算迭代次数
    k = 1 + round((math.log(b-a) - math.log(2 * tol)) / math.log(2))
    print("k: ", k)
    for i in range(1,k+1):
        print("round:", i)
        if fn(c) == 0:
            return c
        elif fn(a) * fn(c) < 0:
            b = (a + b) / 2
        else:
            a = (a + b) / 2
        c = (a + b) / 2
    print("Result: {0}, k: {1}".format(c, k + 1))


if __name__ == "__main__":
    def fn(c: float) -> float:
        # res = math.pow(c, 3) - c - 1 
        res = math.pow(2, -c) - c
        print("res:", res)
        return res

    a = float(input("a:"))
    b = float(input("b:"))
    tol = float(input("tol:"))
    print("a: {0}\tb: {1}\ttol: {2}".format(a, b, tol))
    half(a, b, tol)
