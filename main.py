from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class Main:
    
    def __init__(self):
        options = Options()
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=options)

    def abrir_pagina(self):
        self.browser.get("https://www.amazon.com.mx")
    
    def iniciar_busqueda(self, busqueda):
        busqueda = self.browser.find_element(By.ID, 'twotabsearchtextbox')
        busqueda.send_keys("laptop")

        boton = self.browser.find_element(By.ID, 'nav-search-submit-button')
        boton.click()

        link = self.browser.find_element(By.CLASS_NAME, 'a-link-normal')
        link.click()

if __name__ == "__main__":
    clase = Main()
    clase.abrir_pagina()

    