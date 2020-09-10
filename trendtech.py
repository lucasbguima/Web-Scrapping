# Web Scrapping com Python + Selenium

import time
import requests
import pandas as pd
import numpy as np
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

# 1.1 Garantir que o servidor esteja carregado em 2 segundos
time.sleep(2)

# 1.2 Pegar o elemento que a gente quer
rota_table = "//span[@ng-repeat='titlePart in titleArray']"
element = driver.find_elements_by_xpath(rota_table)
html_content = []
for span in element:
    html_content.append(span.get_attribute('textContent').strip())

# 3. Estruturar o conteúdo em um Dataframe - Pandas
data = pd.DataFrame(np.array(html_content), columns=['Trends'])

# 3.1 Printar dados da tabela

print(data)

driver.quit()