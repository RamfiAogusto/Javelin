


import requests
from googlesearch import search
from bs4 import BeautifulSoup

#------------------------------Libreria google o google search-------
lista_link=[]

pregunta_google= str(input("ingresa tu pregunta: "))

for i in search(pregunta_google, num_results=4, lang="es"):
	lista_link.append(i)
	

print(lista_link)






#---------------------------------------------------------------------
