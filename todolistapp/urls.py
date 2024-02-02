from django.urls import path
from todolistapp import views
# from .views import custom_404
# from django.conf.urls import handler404

# handler404 = custom_404
urlpatterns = [
    path('login',views.loginUser,name="login"),
    path('',views.index,name="index"),
    path('signup',views.signup,name="signup"),
    path('contact',views.contact,name="contact"),
    path('how_to_use',views.howtouse,name="how_to_use"),
    path('team',views.teamdet,name="team"),
    path('logout',views.logout,name="logout"),
    path('add_task',views.addtask,name="add_task"),
    path('delete/<id>/',views.delete,name="delete"),
    path('taskdone/<id>/',views.taskdone,name="taskdone")
    
]
