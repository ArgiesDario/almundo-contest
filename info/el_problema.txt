Un turista esta planificando sus próximas vacaciones y tiene el deseo de visitar una serie ciudades.

Para esto cuenta con un solo medio de transporte disponible (avión) y diferentes agencias turísticas. Todas las agencias manejan la misma tarifa, cobrando $ 0.01 por km recorrido. La diferencia está en que cada agencia nos ofrece una oferta diferente.

Nuestro turista debe:

Partiendo de cualquier cuidad, viajar por única vez a todas las ciudades y volver a la ciudad de origen.
Determinar la agencia turística a utilizar para cada viaje.
¡El recorrido de menor costo total será el ganador!

## Agencias
Para viajar a cualquier destino se puede elegir cualquiera de las siguientes agencias:

Agencia A
La agencia A tiene un descuento para viajero frecuente. Si un cliente vuela tres veces consecutivas con esta agencia, recibe un descuento del 35% en el costo del tercer vuelo.

Agencia B
La agencia B tiene un descuento para vuelos de larga distancia. Si un cliente compra un vuelo de más de 200 kilómetros, recibe un descuento del 15% en el costo de ese vuelo.

Agencia C
La agencia C tiene un convenio con la agencia B. Si un cliente compra un vuelo con la agencia C, y en su vuelo anterior optó por la agencia B, recibe un descuento del 20% en el costo del vuelo con la agencia C.

Agencia D
La agencia D te permite acumular kilómetros. Cada 10000 kilómetros recorridos con la agencia, reintegra al cliente un monto fijo de $ 15.


## Ciudades
El archivo de ciudades contiene todas las ciudades que debe recorrer el turista, en formato csv, con los siguientes campos:

id_ciudad,coordenada_x,coordenada_y
Campo	Tipo
id_ciudad	entero
coordenada_x	float
coordenada_y	float

Ejemplo:
0,8223.16,4811.63
1,3413.67,2929.25
2,1589.17,54.62
3,3427.14,6830.64
4,1000.39,4352.62
5,3705.33,7913.99
...
Las coordenadas de las ciudades petenecen a un punto en un espacio euclídeo, y la distancia que hay que recorrer para viajar entre dos ciudades se mide con la distancia euclidiana. La unidad de medida para esta distancia es el kilómetro.


## Respuesta

El recorrido que nos envíes debe ser un archivo csv que contenga los siguientes campos:

id_ciudad_origen,agencia,id_ciudad_destino
Campo	Tipo	Valores
id_ciudad_origen	entero	Sólo se pueden usar los ids del archivo de ciudades
agencia	char	'A' para la agencia A, 'B' para la agencia B, 'C' para la agencia C o 'D' para la agencia D
id_ciudad_destino	entero	Sólo se pueden usar los ids del archivo de ciudades
Ejemplo:

1,A,7
7,A,9
9,A,23
23,B,678
678,C,43
...
87,B,1


## Aclaraciones y recomendaciones

El problema se puede caracterizar como un problema del viajante (TSP).
Muy probablemente no puedas encontrar la respuesta óptima, por lo que recomendamos la utilización de alguna heurística.
Ante un empate en el costo del viaje, el ganador será el primero en haber enviado la respuesta.
