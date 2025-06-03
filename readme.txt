Basado en Python 3.12

1. Instalar allure
    En Windows, dentro de PowerShell, correr los siguientes comandos:
    > Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    > Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
    > scoop install allure

2. Instalar dependencias de Python dentro del proyecto con:
> pip install -r requirements.txt

2. En el terminal correr los comandos para las pruebas
> pytest test_buy.py
> pytest test_api.py

3.


