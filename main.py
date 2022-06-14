import random
import json
from time import sleep

from selenium import webdriver
from selenium.webdriver import chrome, firefox
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.core.utils import ChromeType
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager

with open('configuracion_general.json') as configuracion:
    valor = json.loads(configuracion.read())
    
def obtener_valores_generales(llave, valores=valor):
    try:
        return valores[llave]
    except:
        msg = f"No se encontró la llave: {llave}"
        print(msg)
        raise Exception(msg)

def setup_driver_options(usar_chorme, usar_chromium, usar_brave, usar_firefox, usar_edge, usar_opera):
    """
        Configuración de los controladores
    """
    # Opciones
    chrome_options = chrome.options.Options()
    firefox_options = firefox.options.Options()

    # Servicios (descargar Administrador de Controladores)
    chrome_service = chrome.service.Service(ChromeDriverManager().install())
    chromium_service = chrome.service.Service(
        ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    brave_service = chrome.service.Service(
        ChromeDriverManager(chrome_type=ChromeType.BRAVE).install())
    firefox_service = firefox.service.Service(GeckoDriverManager().install())
    edge_service = EdgeChromiumDriverManager().install()
    opera_service = OperaDriverManager().install()

    lista_de_controladores = []

    # Configuracion de los drivers para Chrome, Chromium, Brave, Firefox, Edge y Opera
    if usar_chorme:
        chrome_driver = webdriver.Chrome(
            service=chrome_service, 
            options=chrome_options
        )
        lista_de_controladores.append(chrome_driver)

    if usar_chromium:
        chromium_driver = webdriver.Chrome(
            service=chromium_service, 
            options=chrome_options
        )
        lista_de_controladores.append(chromium_driver)

    if usar_brave:
        brave_driver = webdriver.Chrome(
            service=brave_service, 
            options=chrome_options
        )
        lista_de_controladores.append(brave_driver)

    if usar_firefox:
        firefox_driver = webdriver.Firefox(
            service=firefox_service, 
            options=firefox_options
        )
        lista_de_controladores.append(firefox_driver)

    if usar_edge:
        edge_driver = webdriver.Edge(service=edge_service)
        lista_de_controladores.append(edge_driver)

    if usar_opera:
        opera_driver = webdriver.Opera(executable_path=opera_service)
        lista_de_controladores.append(opera_driver)

    return lista_de_controladores

