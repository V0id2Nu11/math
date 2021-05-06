import math

def accelerate(tol: float) -> float:
    x0 = 0.5
    x1 = (1 - math.sin(x0) + 0.878 * x0) / 1.878
    k = 1
    while abs(x1 - x0) >= tol:
        x0 = x1
        x1 = (1 - math.sin(x0) + 0.878 * x0) / 1.878
        k = k + 1

    print("Result: {0}, k: {1}".format(x1, k))


if __name__ == "__main__":

    tol = float("1e-8")
    accelerate(tol)
