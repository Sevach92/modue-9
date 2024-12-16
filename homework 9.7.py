def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        n = 0
        for i in range(1, result + 1):
            if result % i == 0:
                n += 1
        if n == 2:
            print('Простое число')
        else:
            print('Составное число')
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)