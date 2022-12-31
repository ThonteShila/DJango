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
Git commands>
git add .
git commit -m "some message"
git push origin Develop