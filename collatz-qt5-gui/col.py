def check(n):
    global counter
    print(n)
    if n == 1:
        raise Exception(f'Lost after {counter} iterations')
    else:
        counter += 1
        if n % 2 == 0:
            check(int(n / 2))
        else:
            check(int(3 * n + 1))


if __name__ == '__main__':
    while (True):
        try:
            n = int(input('Provide a number: '))
            if n == 0:
                break
            counter = 0
            check(n)
        except Exception as ex:
            print(ex.args[0])
