First, install python3 and make sure your pip program is the one that comes with your python3 setup. Then, install a virtual environment like this:

python3 -m venv ~/.venv/django
Update pip by running:

pip install -U pip

setup venv

python3 -m venv ~/.venv/django
for specific python version ,(make sure you have the perfect python version installed)

python -m venv ~/.venv/django
pip install -U pip
source ~/.venv/django/bin/activate
pip install -r requirements.txt


Updating Django
If you need to udpate Django later, use:

pip install -U Django

django-admin --version

Activating The Django Virtual Environment
To activate the environment, run the following command before you start working in your shell:

source ~/.venv/django/bin/activate

Install the python dependencies from requirements.txt using pip install -r requirements.txt
