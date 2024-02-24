from django.urls import path
from .views import SignIn, SignOut, MyPage
from .apps import AccountConfig

app_name = AccountConfig.name

urlpatterns = [
    path('sign_in/', SignIn.as_view(), name='sign_in'),
    path('sign_out/',SignOut.as_view(), name='sign_out'),
    path('mypage/', MyPage.as_view(), name='mypage')
]