import numpy as np

def kahan_sum(x):

        s = x[0]
        c = 0
        for xi in x[1:]:
                t = s + xi
                if abs(s) > abs(xi):
                        c += (s - t) + xi
                else:
                        c += (xi - t) + s
                s = t
        return s + c


if __name__ == '__main__':

        arr = [1.0, 10e100, 1.0, -10e100]
        print(sum(arr))
        print(np.sum(arr))
        print(kahan_sum(arr))
