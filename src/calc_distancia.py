# Calcula la distancia euclidea entre 2 puntos
def dist_eucl(x1, x2, y1, y2):
    return ((float(x2) - float(x1)) ** 2 + (float(y2) - float(y1)) ** 2) ** (1 / 2)


# Calcula distancia entre 2 ciudades
def dist_ciudades(ciudad_desde, ciudad_hasta):
    return dist_eucl(x1=ciudad_desde["x"], x2=ciudad_hasta["x"], y1=ciudad_desde["y"], y2=ciudad_hasta["y"])
