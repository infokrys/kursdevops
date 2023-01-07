def fibonacci(index):
    prev = 1
    fib = [1, 1]

    for x in range(2, index + 1):
        fib.append(fib[x-2] + fib[x-1])
    print(fib)
    return fib[index]

print(fibonacci(3))
#➞ 3

print(fibonacci(7))
#➞ 21

print(fibonacci(12))
#➞ 233