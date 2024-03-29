# Almundo Challenge

## Que es?
Durante 1 semana en Julio del 2017 (del 24/07/2017 al 31/07/2017) se realizo el "Almundo Contest" o "Almundo Challenge". El cual consiste en resolver un [problema del viajero](https://es.wikipedia.org/wiki/Problema_del_viajante) complejo de la forma mas optima posible. Quien pueda obtener el mejor resultado en ese lapso de tiempo, sera ganador de 2 viajes a Europa.


## Objetivo
Si bien el concurso ya se encuentra finalizado, este repositorio provee la calculadora de costo de viaje para quien quiera intentar resolverlo. El objetivo es resolver el problema del viajero, obteniendo el menor costo posible de viaje.


## Partes del enunciado
- [El problema](https://github.com/ArgiesDario/almundo-contest/blob/master/info/El%20problema.md)
- [Archivo de ciudades](https://github.com/ArgiesDario/almundo-contest/blob/master/info/archivo%20de%20ciudades.csv)
- [FAQ](https://github.com/ArgiesDario/almundo-contest/blob/master/info/FAQ.md)

## Solución ganadora
- [Ranking de soluciones](https://github.com/ArgiesDario/almundo-contest/blob/master/info/Ganadores.jpg)
- [Solución ganadora presentada por Melanie](https://github.com/ArgiesDario/almundo-contest/blob/master/info/solucion_ganadora.csv)
- [Blog de Melanie Sclar y Gabriel Poesia explicando la solución planteada](https://gpoesia.com/posts/almundo-challenge/)

## Como utilizar este repo
Este repositorio provee la [Calculadora de costo de viaje](https://github.com/ArgiesDario/almundo-contest/blob/master/src/calc_solucion.py), necesitando como parámetros el archivo de ciudades (parte del enunciado), y la solución provista por el usuario

```python
res_obtenido = calc_solucion.run(archivo_ciudades=ciudades, archivo_solucion=solucion)
print("Resultado obtenido: " + str(res_obtenido))
```

En [test.py](https://github.com/ArgiesDario/almundo-contest/blob/master/src/tests.py) hay un ejemplo de su uso, validando el resultado de la solucion ganadora
