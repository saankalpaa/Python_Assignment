def factorial(n):
    temp = 1
    if n < 0:
        n = -n
    for i in range(2, n+1):
        temp *= i
    return temp


def main():
    n = int(input())
    print(factorial(n))


if __name__ == "__main__":
    main()