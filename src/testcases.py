import calc_solucion
import time

#Calcula que la validacion del resultado de la solucion ganadora del concurso sea: 63790.25
def calcular_solucion_optima(sol_ganadora, arch_ciudades):
    res_obtenido = calc_solucion.run(file=sol_ganadora, arch_ciudades=arch_ciudades)
    res_esperado = 63790.255168013944

    if res_obtenido != res_esperado:
        msg = 'El algoritmo para calcular la solucion optima NO esta funcionando correctamente'
        raise ValueError(msg, res_obtenido, res_esperado)
    else:
        print("TC - Calcular solucion optima validando algorimto - Funcionando corectamente")

def validar_calculo_resolucion(sol_ganadora, arch_ciudades):
    try:
        start = time.time()
        calcular_solucion_optima(sol_ganadora=sol_ganadora, arch_ciudades=arch_ciudades)
        end = time.time()
        print("Tiempo de ejecucion de solucion ganadora: %s" % str(end-start) + " segundos")
    except ValueError as err:
        print(err.args[0])
        print("Resultado obtenido del algoritmo: %s" % err.args[1])
        print("Resultado esperado solucion ganadora: %s" % err.args[2])