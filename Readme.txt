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

Git commands>
git add .
git commit -m "some message"
git push origin Develop
---------------------------------------------------------------