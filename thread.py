import threading
import utils 

class RemoveSomePrimesThread(threading.Thread):
    def __init__(self, primes):
        super(RemoveSomePrimesThread, self).__init__()
        self.primes=primes
    
    def run(self):
        #los primos con estos numeros no pueden ser circulares, lo lamento chicos...
        no_circulares= [2, 4, 5, 6, 8, 0]
        for item in self.primes[:]:
            for i in range(len(str(item))):
                if (int(str(item)[i:i+1]) in no_circulares) and item is not (2 or 5):
                    self.primes.remove(item)
                    break    
        #una vez limpiada, enviamos los valores que quedan para ver si tienen o no primos circulares, si no tiene
        #se eliminan de la lista.
        for item in self.primes[:]:
            if not utils.is_circular(item):
                self.primes.remove(item)


#generamos la cantidad de primos que se encuentran bajo la cota, pasada por args
#find_primes(limit)
primos= utils.find_primes(1000000)

#cantidad de primos encontrados
size_primos= len(primos)

#lanzamos 5 hilos para que cada hilo busque y los almacenamos en threads
threads= []
start= 0
end= 0

#eliminamos de los numeros primos los que no pueden ser primos, por comprension, ejemplo los q poseen un nro par.
for i in range(5):
    end= (size_primos/5)* (i+ 1) 
    t = RemoveSomePrimesThread(primos[start:end])
    start= (size_primos/5)* (i+ 1)
    #agregamos a la lista cada hilo para referencia
    threads.append(t)
    
    #iniciamos el hilo
    t.start()
    #esperamos hasta que termine
    t.join()

primos_circulares= []

for t in threads:
    primos_circulares += t.primes

print primos_circulares, len(primos_circulares)

