

import requests
from googlesearch import search
from bs4 import BeautifulSoup
import re



#------------------declaracion de funciones--------------------------

def selec_link(num_link):
	response = requests.get(links[num_link])
	soup=BeautifulSoup(response.content, 'html.parser')
	parrafos=soup.find_all("p")
	print("esta respuesta es de la pagina \n\n " + links[num_link])
	print(parrafos)
	


#------------------aqui busca y lista 5 links de cada pregunta-------



links=[]

pregunta_google= input("ingresa tu pregunta: ")
for i in search(pregunta_google, num_results=5, lang="es"):
	
	links.append(i)




selec_link(0)
#---------------------------------------------------------------------


