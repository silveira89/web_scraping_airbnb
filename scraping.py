from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep
import pandas

options = Options()
# Define o tamanho da janela do navegador que será aberta.
# O comando usado na vídeo aula só funciona no chrome.

# Comando usado para não abrir o navegador.
# Normalmente usado quando o código já foi testado e está funcionando perfeitamente.
options.add_argument("--headless")

navegador = webdriver.Firefox(options=options)

navegador.get("https://www.airbnb.com.br")

sleep(2)

aceitar_cookies = navegador.find_element_by_css_selector('button[data-testid="accept-btn"]')
aceitar_cookies.click()

sleep(1)

local = navegador.find_element_by_id('bigsearch-query-detached-query-input')
local.send_keys('São Paulo')

sleep(2)

hospedes = navegador.find_element_by_css_selector('div[data-testid="structured-search-input-field-guests-button"]')
hospedes.click()

sleep(1)

numero_hospedes = navegador.find_element_by_css_selector('button[data-testid="stepper-adults-increase-button"]')
numero_hospedes.click()
numero_hospedes.click()

sleep(2)

buscar = navegador.find_element_by_css_selector('button[data-testid="structured-search-input-search-button"]')
buscar.click()

sleep(4)

site = BeautifulSoup(navegador.page_source, 'html.parser')

aparts = site.findAll('div', attrs={'itemprop':'itemListElement'})

lista_aparts = []

for apart in aparts:

    titulo = apart.find('meta', attrs={'itemprop':'name'})['content']
    descricao = apart.find('div', attrs={'class':'_1olmjjs6'}).text
    url = apart.find('meta', attrs={'itemprop':'url'})['content']
    preco = apart.find('span', attrs={'class':'_krjbj'}).text
    
    # print('Título:', titulo)
    # print('Descrição:', descricao)
    # print('URL:', url)
    # print('Preço:', preco)
    # print()
    lista_aparts.append([titulo, descricao, url, preco])

dados = pandas.DataFrame(lista_aparts, columns=['Título', 'URL', 'Descrição', 'Preço'])
# print(dados)

dados.to_csv('apartamentos.csv', index=False)

# print(apart.prettify())