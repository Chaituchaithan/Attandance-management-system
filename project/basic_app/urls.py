from django.conf.urls import url
from basic_app import views

# SET THE NAMESPACE!


# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url('employee/',views.employee,name='employee'),
    url('employeeview/',views.employeeview,name='employeeview'),
    url('attandance/',views.attandance,name='attandance'),
    url('attandanceview/',views.attandanceview,name='attandanceview'),
    url('dashboard/',views.dashboard,name='dashboard'),
    url('user_login/',views.user_login,name='user_login'),
    url('about/',views.about,name='about'),
    url('contact/',views.contact,name='contact'),

]
