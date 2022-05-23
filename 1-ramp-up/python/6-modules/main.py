from clases import Estacion, ComunidadMadrid
from funciones import dist_estaciones

import pandas as pd

df = pd.read_excel("2018_Julio_Bases_Bicimad_EMT.xlsx")


tot_est = []

for index, row in df.iterrows():
    estacion = Estacion(row[0], row[3], row[1], row[6], row[4], row[5])
    tot_est.append(estacion)


comunidad = ComunidadMadrid(tot_est)


while True:

    user = input("Escoge una opción: \n1. Busca Estación\
        \n2. Calcula distancia \n3. Salir del programa\n")

    try:
        user = int(user)
    except:
        print("Respuesta no válida. Por favor introduce 1, 2 ó 3")
        continue

    if user == 1:
        resp_usu2 = input("Muy bien, introduce el nombre de la estacion")
        busqueda = comunidad.busca_estacion(resp_usu2, "name")
        if busqueda == None:
            print("Esta estacion no está en la base de datos")
        else:
            print("¡Estacion encontrada! La estación es",busqueda.name,"\n\n\n¿Qué más deseas hacer?")
            
    elif user == 2:
        resp_usu3_1 = int(input("Introduce el identificador de la primera estacion "))
        resp_usu3_2 = int(input("Introduce el identificador de la segunda estacion "))
        
        distancia = dist_estaciones(resp_usu3_1, resp_usu3_2, comunidad)
        
        if type(distancia) == str:
            print(distancia)
        else:
            print("Las estacines introducidas están a una distancia de", round(distancia, 2), "km")
        
    elif user == 3:
        print("¡Hasta la próxima!")
        break
    
    else:
        print("Respuesta no valida. Por favor introduce 1, 2 o 3")