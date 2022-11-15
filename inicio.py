


import requests
from googlesearch import search
from bs4 import BeautifulSoup

#------------------------------Libreria google o google search-------
lista_link=[""]

pregunta_google= str(input("ingresa tu pregunta: "))

for i in search(pregunta_google, num_results=4, lang="es"):
	lista_link.append(i)

def buscar(num):
	response = requests.get(lista_link[num])
	print(response)
	print(lista_link[num])
	soup=BeautifulSoup(response.content, 'html.parser')
	content = response.content  
	content_html = soup.find_all("p")
	print(content_html)



buscar(2)


#---------------------------------------------------------------------
