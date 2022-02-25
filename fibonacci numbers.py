def fib(n, counter):
    if n ==0:
        return 0
    elif n ==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)



# print(fib(4))


def fiba(n):
    a = 0
    b = 1

    even = []
    counter = 0

    while counter<n:

        if a % 2 == 0:
            counter += 1
            even.append(a)

        a, b = b, a + b

    return even

print(fiba(14))
