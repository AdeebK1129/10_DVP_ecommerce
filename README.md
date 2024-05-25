# 10_DVP_ecommerce
Adeeb Khan, John Chandler, Jeff Chen, Tyler Chan 

In this project, a basic e-commerce website will be developed with Vue on the front end and Django and PostgreSQL on the backend (DVP stack). Additionally, Pandas and Matplotlib Python libraries will be used to generate graphs to be displayed on the UI based on data received from a public API.  

***NOTE***
This project is going to be run off of python and node virtual environments that have not been added to the repository. Additionally, connections to our PostgreSQL database are made locally via a gitignored secrets.json file. To get this project to run on your own device, these modifications will have to be made. 

## Python Environment Set Up (MacOS)

*assuming pyenv versions are already installed 
*** indicate steps that are NOT needed if pyenv already installed

curl https://pyenv.run | bash

export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"

pyenv update

pyenv install 3.11.5    ***
pyenv versions

pyenv local 3.11.5

python -m venv env_3.11.5

source env_3.11.5/bin/activate

pip install django
pip install psycopg2-binary
pip install jupyter 
pip install pandas
pip install matplotlib
pip install nodeenv

## **Django Environment Set Up**
mkdir requirements_env
touch main.in
touch dev.in

Inside dev.in: 

-c main.txt

nodeenv
django-extensions
jupyter
jupyterlab

Inside main.in:

django==4.2

Build packages by running:

pip install --upgrade pip-tools pip setuptools wheel
pip-compile --upgrade --generate-hashes --output-file requirements_env/main.txt requirements_env/main.in
pip-compile --upgrade --generate-hashes --output-file requirements_env/dev.txt requirements_env/dev.in 

Install packages:

pip-sync requirements_env/main.txt requirements_env/dev.txt

## Node Environment Set Up

Activate python virtual environment
Install nodejs 20.11.1 (the latest LTS(long-term) version at this time), anywhere you want.

nodeenv --node=20.11.1 --prebuilt env_node_20.11.1

Deactivate your python => deactivate

Activate your node env

source env_node_20.11.1/bin/activate

