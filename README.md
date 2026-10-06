# Selenium Simple

## Descripción del proyecto

Script simple de automatización con Selenium en Python sobre [https://www.saucedemo.com/](https://www.saucedemo.com/) (una tienda de demostración). Hace login, agrega 3 productos al carrito, entra al checkout, llena el formulario, continúa al resumen y finaliza la compra.

## Herramientas utilizadas

- Python 3.10+
- Selenium 4 (con Selenium Manager, que descarga el driver de Chrome automáticamente, sin webdriver-manager)
- Google Chrome
- Visual Studio Code
- Git

## Estructura de carpetas

```
Selenium_Simple/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Requisitos previos

- Python 3.10 o superior
- Google Chrome
- Conexión a internet

## Instalación (PowerShell, Windows)

```powershell
git clone https://github.com/yersi123/Selenium_Simple.git   # Clona el repositorio
cd Selenium_Simple                                          # Entra a la carpeta del proyecto
python -m venv venv                                         # Crea el entorno virtual
.\venv\Scripts\Activate.ps1                                 # Activa el entorno virtual
pip install -r requirements.txt                             # Instala Selenium
```

Si PowerShell bloquea la activación, se ejecuta:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Ejecución

```powershell
python main.py   # Abre Chrome y recorre la compra completa
```

## Qué hace el script paso a paso

1. Abre la página `https://www.saucedemo.com/`.
2. Hace login con el usuario y la contraseña de prueba.
3. Agrega 3 productos al carrito: **Sauce Labs Bolt T-Shirt**, **Sauce Labs Bike Light** y **Sauce Labs Fleece Jacket**.
4. Abre el carrito.
5. Entra al checkout.
6. Llena el formulario (**Juan**, **Perez**, **12345**).
7. Continúa al resumen de la compra.
8. Finaliza la compra.

## Datos de prueba

- Usuario: `standard_user`
- Contraseña: `secret_sauce`

Son credenciales públicas de SauceDemo. La compra es solo de práctica y no se cobra nada.

## Configuración

- Los `time.sleep()` controlan la velocidad: se suben para ir más lento y se bajan para ir más rápido.
- La línea comentada `--headless` ejecuta Chrome sin ventana.
- Para usar Edge en lugar de Chrome: cambiar la importación de `Options` (`from selenium.webdriver.edge.options import Options`) y usar `webdriver.Edge`.

## Problemas frecuentes

- **`source ./venv/bin/activate` no funciona**: ese comando es de Linux/Mac. En Windows se usa `.\venv\Scripts\Activate.ps1`.
- **`ModuleNotFoundError`**: el entorno virtual no está activo o falta ejecutar `pip install -r requirements.txt`.
- **El script se queda esperando**: probablemente Selenium Manager está descargando el driver; revisar la conexión a internet.
- **Solo se agregan 2 productos**: era un aviso de contraseñas de Chrome y ya está desactivado en las opciones del script.
