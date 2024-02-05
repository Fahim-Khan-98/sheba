from django.urls import path
from account import views

app_name='account'

urlpatterns = [
    # path('api/', include('account.urls'))
    path('register/',views.registerRequest,name="register"),
]
