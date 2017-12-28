import os

#Obtiene el archivo de solucion pasado como parametro, y devuelve una lista de diccionarios con esa informacion
def get_archivo_solucion(path):
    my_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(my_path, path)
    my_dict_list = []
    f = open(file_path, "r")
    vec = f.readlines()
    for item in vec:
        item = item.replace("\n", "")
        item_splited = item.split(",")
        #Diccionario
        item_dict = {"desde": item_splited[0], "agencia": item_splited[1], "hasta": item_splited[2]}
        my_dict_list.append(item_dict)
    return my_dict_list


#Obtiene el archivo de ciudades pasado como parametro, y devuelve una lista de diccionarios con esa informacion
def get_archivo_ciudades(path):
    my_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(my_path, path)
    my_dict_list = []
    f = open(file_path, "r")
    vec = f.readlines()
    for item in vec:
        item = item.replace("\n", "")
        item_splited = item.split(",")
        #Diccionario
        item_dict = {"ciudad": item_splited[0], "x": item_splited[1], "y": item_splited[2]}
        my_dict_list.append(item_dict)
    return my_dict_list