Desarrollado en Python 3.12 dentro del IDE de Jetbrains Pycharm

1. Instalar allure
    En Windows, dentro de PowerShell, correr los siguientes comandos:
    > Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    > Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
    > scoop install allure

2. Instalar dependencias de Python dentro del proyecto con:
> pip install -r requirements.txt

3. En el terminal correr el comando para las pruebas
> pytest

4. En un CMD con la ruta dentro del proyecto correr para visualizar el dashboard:
> allure serve allure

