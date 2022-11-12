from googlesearch import search
from io import open
import requests
import re
import os
from bs4 import BeautifulSoup 
from tkinter import *

"""


raiz=Tk()
raiz.title("Javelyn")
raiz.config(bg="Red")
raiz.geometry("900x600")
frame_preguntas=Frame()
frame_preguntas.pack( fill="y")
frame_preguntas.pack(side="left", anchor="n")
frame_preguntas.config(bg="Blue")
frame_preguntas.config(width="400", height="500")






frame_respuestas=Frame()
frame_respuestas.pack(side="left", anchor="n")
frame_respuestas.config(bg="Green")
frame_respuestas.config(width="800", height="500")
frame_respuestas.pack(fill="y")




cuadro_texto_preguntas=Entry(frame_preguntas)

cuadro_texto_preguntas.place(x=0, y=50, width=390, height=400)




raiz.mainloop()

"""
lista_preguntas=[]
numero_de_preguntas=()
pregunta=("")
pregunta_para_google=("")

def buscar_3 ():
    intentos = 0

    for url in search(pregunta_para_google, start = 0, pause = 1):
        response = requests.get(url)
        soup=BeautifulSoup(response.content, 'html.parser')
        print(response)
        print(url)

        if response.status_code == 200: 
            content = response.content  
            parrafos = soup.find_all("p")

            for p in range(len(parrafos)):
                parrafo_limpio = parrafos[p].get_text()
                caracteres_en_los_parrafos=len(parrafo_limpio)

            if caracteres_en_los_parrafos>400:
                ubicacion_del_punto = parrafo_limpio.find(".", 400)
                print(ubicacion_del_punto)
                parrafo_final = parrafo_limpio[0:ubicacion_del_punto]
                print(parrafo_final+ ".")
                print("/n")
                print("/n")
                print("/n")
                print("/n")

                if ubicacion_del_punto == -1:
                    print(parrafo_limpio)
                    print("/n")
                    print("/n")
                    print("/n")
                    print("/n")
            else:
                print(parrafo_limpio)
        else:
            print("la pagina no respode, intentelo mas tarde")

        intentos = intentos + 1
        if intentos == 1:
            break

def leer_archivo_y_asignar_variable():
    global lista_preguntas
    global numero_de_preguntas
    global pregunta
    global pregunta_para_google
    desicion=(1)

    while desicion==1:
        pregunta=input("Tu pregunta es: ")
        lista_preguntas.append(pregunta)
        tienes_mas_preguntas=input("¿tienes mas preguntas? responde con 'si' o 'no' ")

        if tienes_mas_preguntas=="no":
            break

    print(lista_preguntas)
    numero_de_preguntas = len(lista_preguntas)
    j=(numero_de_preguntas)

    for x in range(0,len(lista_preguntas)):
        print(lista_preguntas[x])
        pregunta_para_google=lista_preguntas[x]
        buscar_3()

        
leer_archivo_y_asignar_variable()
buscar_3()