# Primos-circulares

Test ML, obtencion de numeros primos circulares bajo la cifra un millon

### ¿Que tenemos acá? ###

+ Un script en Python para la obtencion del listado de primos circulares, visto por consola
+ Un proyecto en Django para ejecutar el script a través de una web, con la descripcion del algoritmo empleado.

### Script en python ###

## Tecnología ##

Python 2.7 

`$ mkdir /home/data/primos-circulares`

`$ cd /home/data/primos-circulares/`

`$ virtualenv venv` (apt-get install virtualenv)

`$ https://github.com/antolinij/Primos-circulares.git`

`$ source venv/bin/activate`

`$ python thread.py`

Este script va a obtener un listado de los primos circulares, los mostrara en un arreglo. Para lograr este objetivo, se utilizaron Threads del modulo threading de Python,
por eleccion, elegi utilizar 5 hilos, los cuales son los encargados de eliminar primos no candidatos y primos no circulares. El funcionamiento del Script es asi:

Se ejecuta y se calculan los primos menores a un millón.
Luego se ejecutan 5 hilos para que eliminen a todos los primos que no son circulares.

### Pagina web  ###

 [Primos Circulares - Web en desarrollo](http://ardilla.com.ar:8989)

 ## Tecnología ##

 Python 2.7, Django 1.7, SQLite3, Bootstrap, Sweet Alert, Jquery

 ### Funcionamiento ###

    
    Cuando lleguen a la web, verán un listado de primos circulares, estos vienen de una base de datos, 
    los cuales fueron cargados en el inicio del servidor.

    Cuando se realiza un Migrate del modelo Prime, el cual tiene un atributo llamado number, 
    se le anexa el script antes detallado, entocnes al levantarse el 
    proyecto django y al sincronizar la base de datos, 
    se da cuenta que tiene informacion que cargar y la carga a la base de datos.

    Luego cuando se hace el request a la pagina, se consulta a la base de datos y 
    se genera esa tabla con primos circulares.

    Una vez ingresado un numero (o una letra) para calcular si es primo circular, 
    no es por base de datos, esto utiliza el modulo utils.py, el cual contiene funciones

    para chequear si es primo, si es primo circular, etc.

    Podran observar esta vista en primos-circulares/base/views.py, 
    ahi se encuentra la logica para verificar cada valor ingresado.

    Se uso Bootstrap para el maquetado y Sweet Alert para los mensajes.

    El servidor es mio de desarrollo, perdón por la informalidad del dominio.

 ### Contacto ###

 + jony.antolini@gmail.com
