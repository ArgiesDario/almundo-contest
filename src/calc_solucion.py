import calc_distancia
import obtener_archivos


def run(archivo_ciudades, archivo_solucion):

    # Busca en la lista de ciudades una ciudad especifica, y devuelve su informacion
    def obtener_ciudad(ciudad, lista):
        return lista[int(ciudad)]

    # Obtener todas las ciudades
    ciudades = obtener_archivos.get_archivo_ciudades(path=archivo_ciudades)
    # Obtener el viaje de la solucion
    travel = obtener_archivos.get_archivo_solucion(path=archivo_solucion)

    # --- Calculo el costo del viaje --- #

    # Contadores utilizados para obtener descuentos con secuencias de agencias o acumulacion de km en el caso de la agencia D
    cont_age_a = 0
    cont_age_bc = False
    cont_age_d = 0
    # Descuentos segun agencia
    desc_a = 0.65   # %
    desc_b = 0.85   # %
    desc_c = 0.80   # %
    desc_d = 15     # $
    acum_d = 0      # KM
    # Precio acumulado
    precio_acum = 0 # $

    # Recorro la lista de ciudades
    for item in travel:
        # Calcular distancia y precio
        ciudad_desde = obtener_ciudad(ciudad=item["desde"], lista=ciudades)
        ciudad_hasta = obtener_ciudad(ciudad=item["hasta"], lista=ciudades)
        distancia = calc_distancia.dist_ciudades(ciudad_desde=ciudad_desde, ciudad_hasta=ciudad_hasta)
        precio = distancia * 0.01

        # Armar secuencia: A-A-A y B-C
        if item["agencia"].upper() == "A":
            # Agregar A, reiniciar BC
            cont_age_a += 1
            cont_age_bc = False
        elif item["agencia"].upper() == "B":
            # Agregar BC, reiniciar A
            cont_age_bc = True
            cont_age_a = 0
        elif item["agencia"].upper() == "C":
            # Reiniciar contadores
            cont_age_a = 0
            # cont_age_bc no se reinicia aca ya que perderia la secuencia B-C
        elif item["agencia"].upper() == "D":
            # Agregar la distancia de viaje en agencia D. Reiniciar contadores
            cont_age_d += distancia
            cont_age_a = 0
            cont_age_bc = False

        # Armar descuentos
        if item["agencia"].upper() == "A" and cont_age_a == 3:
            # Si hubo 3 vuelos con agencia A seguidos, aplico el 35% de descuento al 3er vuelo
            precio = precio * desc_a
            cont_age_a = 0
        if item["agencia"].upper() == "B" and distancia > 200:
            # Si es agencia B y la distancia es mayor a 200, aplico el 15% de descuento
            precio = precio * desc_b
        if item["agencia"].upper() == "C" and cont_age_bc:
            # Si la agencia es C y la anterior es B, aplico 20% de descuento al vuelo C
            precio = precio * desc_c
            cont_age_bc = False # Aca se reinicia el contador
        if item["agencia"].upper() == "D":
            acum_d += distancia

        # Precio acumulado
        precio_acum += precio

    # Aplico descuento D, cada 10.000 KM, 15$ de descuento
    acum_agencia_d = acum_d / 10000
    descuento_d = int(str(acum_agencia_d).split(".")[0]) * 15

    # Calculo precio final
    precio_final = precio_acum - descuento_d

    return precio_final
