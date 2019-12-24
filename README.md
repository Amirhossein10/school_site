# سایت مدرسه ای
ایجاد شده با django, html, css, js, sqlite3
--------------------------------------------------------------
برای آپلود روی سیستم ابتدا جنگو را نصب کنید:

pip install django==2.2.7

سپس در پوشه سایت رفته و مراحل زیر را انجام دهید:

python manage.py migrate

python manage.py makemigrations

python manage.py migrate

برای ایجاد یوزر از دستور زیر استفاده کنید:

python manage.py createsuperuser

سپس به ترتیب نام یوزر، ایمیل و رمز عبور خود را وارد کنید.

برای اجرا از دستور زیر استفاده کنید:

python manage.py runserver

و در مرورگر خود آدرس زیر را وارد کنید:

127.0.0.1:8000
