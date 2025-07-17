

def fib(n, memo):
    if memo[n] != None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n - 1, memo) + fib(n - 2, memo)
    memo[n] = result
    return result

n = 100
memo = [None] * (n + 1)
r = fib(n, memo)
# print(r)


def fibTwo(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fibTwo(n - 1) + fibTwo(n - 2)
    return result

n = 10
rW = fibTwo(n)
print(rW)