>python3 -m venv tees => membuat environment
>cd tees
source /bin/activate
pip install django
django-admin startproject task / copy folder task ke dalam environment
cd task
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
	>username : dns
	>password: herlambang
./manage.py => menjalankan django

python3 test.py => menjalankan testing otomatis

http://127.0.0.1:8000/api/token/ => membuat token
http://127.0.0.1:8000/profil/api/ => GET
http://127.0.0.1:8000/profil/api/<str:pk> => PUT,DELETE
http://127.0.0.1:8000/customer/api/ => GET
http://127.0.0.1:8000/customer/api/<str:pk> => PUT,DELETE
