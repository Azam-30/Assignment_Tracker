# myapp/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('load_data/', views.load_data, name='load_data'),
    path('login/', views.login_view, name='login'),
    path("validate_login/", views.validate_login, name="validate_login"),
    path("logout/", views.LogoutPage, name="logout"),
    path('subject-selection/', views.subject_selection_view, name='subject_selection'),
    path('python-assignments/', views.python_assignments_view, name='python_assignments'),
    path('data-structures-assignments/', views.data_structures_student_list, name='data_structures_assignments'),
    


    path('python/students/', views.python_student_list, name='python_student_list'),
    path('python/students/create/', views.python_student_create, name='python_student_create'),
    path('python/students/<str:roll_no>/update/', views.python_student_update, name='python_student_update'),
    path('python/students/<str:roll_no>/delete/', views.python_student_delete, name='python_student_delete'),
    path('python/search/', views.python_student_search, name='python_student_search'),

    path('data-structures/students/', views.data_structures_student_list, name='data_structures_student_list'),
    path('data-structures/students/create/', views.data_structures_student_create, name='data_structures_student_create'),
    path('data-structures/students/<str:roll_no>/update/', views.data_structures_student_update, name='data_structures_student_update'),
    path('data-structures/students/<str:roll_no>/delete/', views.data_structures_student_delete, name='data_structures_student_delete'),
    path('data-structures/search/', views.data_structures_student_search, name='data_structures_student_search'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
