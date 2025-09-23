"""
6.能被1 和本身整除的整数叫素数；如一个素数从左向右和从右向左是相同的数，则该素数为回文素数。编程求出2-1000内的所有回文素数。
"""
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def huiwen(n):
    for i in range(2, n):
        if isPrime(i) and str(i) == str(i)[::-1]:
            print(i,end=" ")

huiwen(1000)