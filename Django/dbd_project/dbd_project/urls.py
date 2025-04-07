from django.contrib import admin
from django.urls import path
from blog import views
urlpatterns = [
    path('admin/',admin.site.urls),
    path('value', views.login, name='login'),
    path('vis/', views.dashboard_view, name='Visitor'),
    path('doc/', views.doctor, name='Doctor'),
    path('pat/', views.patient, name='Patient'),
    path('ad', views.admin, name='Admin'),
    path('signup/', views.signup2, name='signup2'),
    path('signin/', views.signin, name='signin'),
    path('patient_dashboard/<str:email>/', views.patient_dashboard, name='patient_dashboard'),  # Include email in the URL pattern
    # Other paths here...

    path('', views.signin, name='signin'),  # Sign-in URL
    #path('patr/',views.patient_registration,name='patient_registration')
  # Signup URL
  # Corrected the reference to the login view
]
