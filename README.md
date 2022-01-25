# ShopFloor_fastapi

Python version : 3.10.2

Run Folowing commands to setup your project :

To activate venv : 

- cd venv/Scripts
- activate.bat

return to the main folder and install the required dependencies :

- pip install -r requirements.txt


run the project:

- uvicorn app.main:app --reload


if the project wont start or if your on macos / linux please unistall the venv and install your own using :

- windows : python -m venv venv
And then repeat from step one.

- macos/linux : python3 -m venv venv

PS : to activate venv on macos / linux run :
- . /venv/bin/activate
