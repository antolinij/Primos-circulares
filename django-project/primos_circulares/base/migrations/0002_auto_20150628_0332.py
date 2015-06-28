# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def load_numbers(apps, schema_editor):
    from base import utils
    #cargamos el modelo
    Prime = apps.get_model("base", "Prime")

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
        t = utils.BuscaPrimosCircularesThread(primos[start:end])
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
            
    for p in primos_circulares:
        aux= Prime(number=p)
        aux.save()

class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_numbers),
    ]
