from django.urls import path
from .views import SignIn, SignOut, MyPage, QueryEmail, PasswordReset
from .apps import AccountConfig

app_name = AccountConfig.name

urlpatterns = [
    path('sign_in/', SignIn.as_view(), name='sign_in'),
    path('sign_out/',SignOut.as_view(), name='sign_out'),
    path('mypage/', MyPage.as_view(), name='mypage'),
    path('sign_in/query_email/<str:email>/', QueryEmail.as_view(), name='query_email'),
    path('sign_in/password_reset/<str:user_id>/', PasswordReset.as_view(), name='password_reset'),
]