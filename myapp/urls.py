
from django.urls import path
from . import views

urlpatterns = [


    path('', views.login),
    path('login_post/', views.login_post),
    path('logout/', views.logout),

    path('admin_home/', views.admin_home),

    path('add_teacher/', views.add_teacher),
    path('add_teacher_post/', views.add_teacher_post),

    path('view_teacher/', views.view_teacher),

    path('edit_teacher/<int:id>/', views.edit_teacher),
    path('edit_teacher_post/', views.edit_teacher_post),

    path('delete_teacher/<int:id>/', views.delete_teacher),

    path('student_register/', views.student_register),
    path('student_register_post/', views.student_register_post),

    path('student_home/', views.student_home),
    path('student_profile/', views.student_profile),

    path('send_complaint/', views.send_complaint),
    path('send_complaint_post/', views.send_complaint_post),

    path('complaint_history/', views.complaint_history),

    path('view_complaints/', views.view_complaints),

    path('reply/<int:id>/', views.reply),
    path('reply_post/', views.reply_post),
path('view_students/', views.view_students),
path('view_students/', views.view_students),

path('edit_student/<int:id>/', views.edit_student),
path('edit_student_post/', views.edit_student_post),

path('delete_student/<int:id>/', views.delete_student),

]
