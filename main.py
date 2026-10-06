from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.edge.options import Options
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait

USER = "standard_user"
PASSWORD = "secret_sauce"  

def main():
    options = Options()
    # options.add_argument("--headless")  # Ejecutar Chrome sin ventana
    options.add_argument("--window-size=1920,1080")  # Tamaño de ventana
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,  # Quitar el aviso de guardar contraseña
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False  # Quitar el aviso "Cambia tu contraseña"
    })
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)  # Pausa después de abrir la página



    #Login
    user_input=driver.find_element("id", "user-name")
    user_input.send_keys(USER)
    time.sleep(1)  # Pausa después de escribir el usuario

    password_input=driver.find_element("id", "password")
    password_input.send_keys(PASSWORD)
    time.sleep(1)  # Pausa después de escribir la contraseña

    button=driver.find_element("id", "login-button")
    button.click()
    time.sleep(2)  # Pausa después del login

    #Compras
    Wait(driver, 10).until(EC.element_to_be_clickable(("id", "add-to-cart-sauce-labs-bolt-t-shirt"))).click()
    time.sleep(1.5)  # Pausa después de agregar el producto 1
    Wait(driver, 10).until(EC.element_to_be_clickable(("id", "add-to-cart-sauce-labs-bike-light"))).click()
    time.sleep(1.5)  # Pausa después de agregar el producto 2
    Wait(driver, 10).until(EC.element_to_be_clickable(("id", "add-to-cart-sauce-labs-fleece-jacket"))).click()
    time.sleep(1.5)  # Pausa después de agregar el producto 3

    #boton de carrito
    driver.find_element("xpath", "//a[@class='shopping_cart_link']").click()
    time.sleep(2)  # Pausa después de abrir el carrito

    #boton de checkout
    driver.find_element("id", "checkout").click()
    time.sleep(2)  # Pausa después de abrir el formulario

    #llenar formulario
    driver.find_element("id", "first-name").send_keys("Juan")
    driver.find_element("id", "last-name").send_keys("Perez")
    driver.find_element("id", "postal-code").send_keys("12345")
    time.sleep(2)  # Pausa después de llenar el formulario

    driver.find_element("id", "continue").click()
    time.sleep(4)  # Pausa después de continuar al resumen de la compra
    driver.find_element("id", "finish").click()

    time.sleep(10)  # Esperar 10 segundos para ver el resumen de la compra
    driver.quit()  # Cerrar el navegador

if __name__ == "__main__":
    main()