

import requests
from googlesearch import search
from bs4 import BeautifulSoup
import re



#------------------declaracion de funciones y variables--------------------------
links=[]
lista_parrafos=[]

def selec_link(num_link):
	response = requests.get(links[num_link])
	soup=BeautifulSoup(response.content, 'html.parser')
	parrafos=soup.find_all("p")
	print("esta respuesta es de la pagina: " + links[num_link])
	for p in range(len(parrafos)):
		parrafo_limpio = parrafos[p].get_text()
		lista_parrafos.append(parrafo_limpio)
	print(lista_parrafos[0])


#------------------aqui busca y lista 5 links de cada pregunta-------

pregunta_google= input("ingresa tu pregunta: ")
for i in search(pregunta_google, num_results=5, lang="es"):
	links.append(i)




selec_link(0)
#---------------------------------------------------------------------


