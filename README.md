# 10_DVP_ecommerce

## Alimama E-Commerce 
Adeeb Khan, John Chandler, Jeff Chen, Tyler Chan 

In this project, a basic e-commerce website will be developed with Vue on the front end and Django and PostgreSQL on the backend (DVP stack). Additionally, Pandas and Matplotlib Python libraries will be used to generate graphs to be displayed on the UI based on data received from a public API.  

***NOTE***
This project will be run off of Python and node virtual environments that have not been added to the repository. Additionally, connections to our PostgreSQL database are made locally via a gitignored secrets.json file. To get this project to run on your device, these modifications will have to be made. 

## Python Environment Set Up (MacOS)

*assuming pyenv versions are already installed 
*** indicate steps that are NOT needed if pyenv is already installed

```
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
pip install django_vite
pip install django_extensions
pip install requests #in case an error arises in a views.py about missing request
```

## **Django Environment Set Up**
```
mkdir requirements_env
touch main.in
touch dev.in
```
Inside dev.in: 
```
-c main.txt

nodeenv
django-extensions
jupyter
jupyterlab
```
Inside main.in:
```
django
django_vite
```
Build packages by running:
```
pip install --upgrade pip-tools pip setuptools wheel
pip-compile --upgrade --generate-hashes --output-file requirements_env/main.txt requirements_env/main.in
pip-compile --upgrade --generate-hashes --output-file requirements_env/dev.txt requirements_env/dev.in 
```
Install packages:

`pip-sync requirements_env/main.txt requirements_env/dev.txt`

## Node Environment Set Up

Activate python virtual environment
`source env_3.11.5/bin/activate`
Install nodejs 20.11.1 (the latest LTS(long-term) version at this time), anywhere you want.

`nodeenv --node=20.11.1 --prebuilt env_node_20.11.1`

Deactivate your python => `deactivate`

Activate your node env

`source env_node_20.11.1/bin/activate`

## API In Use
https://fakestoreapi.com/docs 
This is a public API and thus there will be no need to get a personal primary key. All fetch requests are done automatically with no need to configure anything on RapidAPI or make any payment plan.

## How to run
WE ARE ASSUMING THE USER HAS PGADMIN AND IS WILLING TO LINK THEIR OWN DATABASE TO TEST

As such, we have put a secrets_template.json file in the ecommerce inner project folder. Simply rename this file to be secrets.json and fill in the information for your own PostgreSQL database.

secrets.json Template
```
{
    "environment": "development", 
    "ecommerce_url": "http://localhost:8000", 
    "database_name": "YOURDATABASENAME", 
    "database_user": "YOURDATABASEUSER",
    "database_pwd": "YOURDATABASEPW", 
    "database_host": "localhost", 
    "database_port": "5432",
    "vite_dev_server_port": "5173",
    "PAYPAL_CLIENT_ID": "YOURCLIENTID",
}
```
## How to get your Paypal Client ID
In order to make this website work as intended, you MUST use a client ID. It is unique for every user, and is automatically generated for each paypal account.
In order to obtain your paypal client ID, navigate to the following link: https://developer.paypal.com/dashboard/applications/sandbox Once there, copy the Client ID and paste it inside of your secrets.json file. 

In one terminal window, the user should navigate to the vue_ecommerce folder and run
```
npm install
npm run dev
```


In another terminal window, the user should navigate to the first ecommerce folder in their directory and run 
```
python manage.py makemigrations
python manage.py migrate
```

In the folder notebooks, navigate to product_db.ipynb and run the notebook in order. If during the first cell any modules are missing when it is run, be sure to promptly pip install them into your python environment if you haven’t already. Running this notebook will populate your Products database. 

Now back in terminal:
```
python manage.py runserver
```


The user should go to the URL prompted by this which is likely to look something like http://localhost:8000. Do note that this url is determined by what was put in the secrets.json file so if the user puts a different specified URL in secrets.json, the URL will look different. 

## Working with Paypal Checkout

 There is a chance that the Paypal Checkout feature will be stuck loading infinitely. Rest assured, this is not an error on our end: Paypal is simply extremely buggy. In the case tha this happens, try to either refresh the page or click the 'x' button in the corner.

 In order to sucessfully check out on our website, you're going to need some type of credit/debit card. You can generate a fake one here: https://developer.paypal.com/api/rest/sandbox/card-testing/



