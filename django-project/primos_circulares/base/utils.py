import threading

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
        print num
        if not is_prime(int(num)):
            return False
    return True

class BuscaPrimosCircularesThread(threading.Thread):
    def __init__(self, primes):
        super(BuscaPrimosCircularesThread, self).__init__()
        self.primes=primes

    def run(self):
        #los primos con estos numeros no pueden ser circulares, lo lamento chicos...
        no_circulares= [2, 4, 5, 6, 8, 0]
        for item in self.primes[:]:
            for i in range(len(str(item))):
                if (int(str(item)[i:i+1]) in no_circulares) and (not item in [2, 5]):
                    self.primes.remove(item)
                    break
        #una vez limpiada, enviamos los valores que quedan para ver si tienen o no primos circulares, si no tiene
        #se eliminan de la lista.
        for item in self.primes[:]:
            if not is_circular(item):
                self.primes.remove(item)
