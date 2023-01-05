py --version = dispalys python version
pip install virtualenvwrapper-win = create saperate envronment wrapper space
py -m venv myenv = create new virtual envronment
myenv\Scripts\activate = activate and gointo created envronment
pip install django = install django
django-admin --version = see version
python manage.py runserver = run the lightweight server

Create new folder 'projects' 
cmd cd to 'projects'> django-admin startproject telusko 
cd to 'telusko'> python manage.py runserver

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.    
Run 'python manage.py migrate' to apply them.


new app in this project>python manage.py startapp calc
Hello word>
create new urls.py
----------------
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
--------------
main urls.py
--------------------
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('calc.urls')),
    path('admin/', admin.site.urls),
]
-------------------------------
views.py
-------------------------------
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("hello world");
-------------------------
create template folder in telusko

created html file

done changes in setting.py added path
'DIRS': [os.path.join(BASE_DIR,'templates')],

do know view.py to render the html as below
def home(request):
    return render(request,'home.html');

Dynamic data>view.py>
    def home(request):
    return render(request,'home.html',{'fName':'Shila', 'lName':'Kamlapure'});
home.html>
    <h2>hello world from {{fName}} {{lName}}</h2>

cal app
adding two no
reult.html added in template.html
{% extends 'master.html' %}

{% block content %}
Result : {{result}}
{% endblock %}


---------------------------------
view.py
GET-to take no as response after request to from and adding no

def add(request):
    val1=int(request.GET['num1'])
    val2=int(request.GET['num2'])
    res=val1+val2
    return render(request,'result.html',{'result':res})

-----------------------------------
url.py of calc
urlpatterns = [
    path('', views.home, name='home'),path('add',views.add,name='add')]
---------------------------------


To add form in webapp

 
{% block content %}
<h1>Home Page by {{fName}} {{lName}}</h1>
<form action="add">
    Enter 1st number : <input type="text" name="num1"><br>
    Enter 2nd number : <input type="text" name="num2"><br>
    <input type="submit">

</form>
{% endblock %}

---------------------------------------------------------------
POST method instead GET

changes home.html
{% block content %}
<h1>Home Page by {{fName}} {{lName}}</h1>
<form action="add" method='POST'>
    
    {%csrf_token%}  #used from setting.py for ue of post
    Enter 1st number : <input type="text" name="num1"><br>
    Enter 2nd number : <input type="text" name="num2"><br>
    <input type="submit">

</form>

view.py

def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res=val1+val2
    return render(request,'result.html',{'result':res})

---------------------------------------------------------------------------------------------------
copied  template
travello.zip
do changes in files like calc
copy indx.html in template
copy first  four files of travello zip file in static folder crated in main telusko
created new app using python managr.py startapp travello  commands

------------------------------------------------------------------------------
passing static data in django

index.html
{%load static%}
{%status 'link of css,plugins,img,src'%}
----------------------------------------------------------------------------------------
passing dynamic data in django

index.html changes done for accesting dynamic data ie entered in py code in html page
</div>
							<div class="destination_content">
							<div class="destination_title"><a href="{%static 'destinations.html'%}">{{dest1.name}}</a></div>
								<div class="destination_subtitle"><p>{{dest1.desc}}</p></div>
								<div class="destination_price">From ${{dest1.price}}</div>
							</div>

create class in model.py
class Destination:
    id:int
    name:str
    img:str
    desc:str
    price:int
create changes in view created object
from .models import Destination
# Create your views here.
def index(request):

    dest1=Destination()
    dest1.name='mumbai'
    dest1.desc='The city never sleep'
    dest1.price=800
    return render(request,'index.html',{'dest1':dest1});
-----------------------------------------------------------------------------------

 use for loop
view.py
def index(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The city never sleep'
    dest1.img = 'destination_1.jpg'
    dest1.price = 800

    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.desc = 'Hyderabad biryanii is awaysome'
    dest2.img = 'destination_2.jpg'
    dest2.price = 400

    dest3 = Destination()
    dest3.name = 'Pune'
    dest3.desc = 'Nice city'
    dest3.img = 'destination_3.jpg'
    dest3.price = 1100

    dests =[dest1,dest2,dest3]
    return render(request, 'index.html', {'dests': dests})
----------------------------------------------------------------------------------------
	  index.html
      
      {%load static%}
      {% static "images" as baseUrl%}
      {  % for dest in dests %}
						<!-- Destination -->
						<div class="destination item">
							<div class="destination_image">
								<img src="{{baseUrl}}/{{dest.img}}" alt="">
								
							</div>
							<div class="destination_content">
							<div class="destination_title"><a href="{%static 'destinations.html'%}">{{dest.name}}</a></div>
								<div class="destination_subtitle"><p>{{dest.desc}}</p></div>
								<div class="destination_price">From ${{price}}</div>
							</div>
						</div>
						{% endfor %}

-------------------------------------------------------------------------------------------
install postgresql

postgresql
user:postgres
password:Thonte@1231
port:5432

for connection of our app with db need cordinator install
pip install psycopg2 
create connestion in setting.py


DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql',
        'NAME':'telusko',
        'user':'postgres',
        'password':'Thonte@1231',
        'Host':'localhost'
    }
}
models.py


# Create your models here.
class Destination(models.Model):

    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    price=models.IntegerField
    offer=models.BooleanField(default=False)
    ------------------------------------------------------------------------------------
Make migration

(myenv) G:\Job Search shila\Django\DJango\projects\telusko>pip install pillow
Collecting pillow
  Downloading Pillow-9.4.0-cp311-cp311-win_amd64.whl (2.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.5/2.5 MB 56.3 kB/s eta 0:00:00
Installing collected packages: pillow
Successfully installed pillow-9.4.0ackages (9.4.0)

(myenv) G:\Job Search shila\Django\DJango\projects\telusko>python manage.py makemigrations
G:\Job Search shila\Django\DJango\myenv\Lib\site-packages\django\core\management\commands\makemigrations.py:143: RuntimeWarning: Got an error checking a consistent migration history performed for database connection 'default': connection to server at "localhost" (::1), port 5432 failed: fe_sendauth: no password supplied

  warnings.warn(
Migrations for 'travello':
  travello\migrations\0001_initial.py
    - Create model Destination
---------------------------------------------------------------------------------------------------------------------------------

im migration folder after running 
(myenv) G:\Job Search shila\Django\DJango\projects\telusko>python manage.py makemigrations
=
0001_initial.py Generated
---------------------------------------------------------------------------------------
setting.py add

INSTALLED_APPS = [
    'travello.apps.TravelloConfig',
    -------------------------------------------------------------------------------
Database connectivity done use commands
>python manage.py makemigrations
>python manage.py sqlmigrate travello 0002 
>python manage.py migrate

if we add more column in tanle re_migrate using sane above three cmds

table created in pgadmin tool
---------------------------------------------------------------------------------------------
login page
(myenv) G:\Job Search shila\Django\DJango\projects\telusko>python manage.py createsuperuser
Username (leave blank to use 's'): shila
Email address: thonte.shila@gmail.com
Password: 
Password (again):
The password is too similar to the email address.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

(myenv) G:\Job Search shila\Django\DJango\projects\telusko>python manage.py runserver       
-----------------------------------------------------------------------------------------
adding destination:
model.py of telusko

from django.contrib import admin
from .models import Destination
# Register your models here.
admin.site.register(Destination)
=--------------------------------------------------------------------------------

in add destination from webpage
added destination goes in to table 
for accessing and displaying data on web page wue following  changes in
views.pydef index(request):
    dests=Destination.objects.all()
    return render(request, 'index.html', {'dests': dests})
-------------------------------------------------------------------------------
    in index.py:
    	<div class="destination item">
							<div class="destination_image">
								<img src="{{dest.img.url}}" alt="">
								{% if dest.offer %}
-------------------------------------------------------------------------------------------------
in setting .py

STATIC_URL = 'static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
]
STATIC_ROOT=os.path.join(BASE_DIR,'assets')
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
# Default primary key field type
-------------------------------------------------------------
image added in pic folder from google .jpg

#####################################################################################
new field register added in travello
first use cmd of 
python manage.py startapp accounts
then urls.py created
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register')]
------------------------------------------------------------------------------
view,py
from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request,'register.html')


-------------------------------------------------------------------------------
index.html
<li><a href="contact.html">Contact</a><
<li><a href="accounts/register">Register</a></li>
-----------------------------------------------------------------------------
addes register.html in template  enteries of field are from pgadmin 
from table auth_user
right click and see all rows
<!DOCTYPE html>

<html>
    <head>
        <title>Registeration</title>
    </head>
    <body bgcolor="cyan">
        <form action="register" method="post">
            {% csrf_token%}
            <input type="text" name="first_name" placeholder="First Name"><br>
            <input type="text" name="last_name" placeholder="LAST Name"><br>
            <input type="text" name="username" placeholder="UserName"><br>
            <input type="email" name="email" placeholder="email"><br>
            <input type="password" name="password1" placeholder="Password"><br>
            <input type="password" name="password2" placeholder="ConfirmPassword"><br>
            <input type="Submit">
        </form>

        
    </body>
</html>
-------------------------------------------------------------------------------
urls.py main telusko
urlpatterns = [
    path('', include('travello.urls')),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls'))



-----------------------------------------------------------------------------------------------
Git commands>
git add .
git commit -m "some message"
git push origin Develop
---------------------------------------------------------------