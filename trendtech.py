# Web Scrapping com Python + Selenium

import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import json

# 1. Pegar conteúdo HTML a partir da URL
url = "https://trends.google.com.br/trends/trendingsearches/daily?geo=BR"

options = Options()
options.headless = True
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get(url)

# 1.1 Garantir que o servidor esteja carregado em 10 segundos
time.sleep(2)

# 1.2 Simular Cliques na Plataforma


# 1.3 Após o clique pegar o elemento que a gente quer
rota_table = "/html/body/div[2]/div[2]/div/div[2]/div/div[1]/ng-include/div/div/div/div"
element = driver.find_element_by_xpath(rota_table)
html_content = element.get_attribute('outerHTML')
print(html_content)

""" # 2. Parsear o conteúdo HTML - BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

# 3. Estruturar o conteúdo em um Dataframe - Pandas
data = pd.read_html(str(table))[0]

# 3.1 Tratar dados da tabela

print(data)

# Opcional. Transformar os dados em um dicionário próprio
# Opcional. Converter e salvar em um arquivo JSON """

driver.quit()