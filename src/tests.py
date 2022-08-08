import calc_solucion


# Calcula que la validacion del resultado de la solucion ganadora del concurso sea: 63790.25
def validar_solucion_ganadora(ciudades, solucion):
    res_obtenido = calc_solucion.run(archivo_ciudades=ciudades, archivo_solucion=solucion)
    res_esperado = 63790.255168013944

    print("Resultado obtenido: " + str(res_obtenido))
    assert res_obtenido == res_esperado
