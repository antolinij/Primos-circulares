#encuentra primos con limit como cota superior
def find_primes(limit):
    primes = [2]
    i = 3
    while i <= limit:
        is_prime = True
        sqrt_limit = int(i**(0.5) + 1)
        for prime in primes:
            if i % prime == 0:
                is_prime = False
                break
            if prime >= sqrt_limit: 
                break
        if is_prime:
            primes.append(i)
        i += 2
    return primes

def is_prime(num):
    #calculo la division de num hasta la raiz cuadrada de num redondeada al siguiente entero.
    #en base a una regla matematica
    limit = int(num**(0.5) + 1)
    primes= find_primes(limit)

    while True:
        is_prime = True
        if num == 2:
            return is_prime
        if num < 2:
            is_prime = False
            return is_prime
        for prime in primes:
            #no es primo
            if num % prime == 0:
                is_prime = False
                break
            #es primo
            if prime >= limit:
                break
        return is_prime

def is_circular(num):
    #recorremos las variantes circulares
    for i in range(len(str(num))):
        num= str(num)[len(str(num)) -1:]+str(num)[:-1]
        if not is_prime(int(num)):
            return False
    return True


