import logging
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import CustomUser, Profile
from django.http import JsonResponse
# Create your views here.

logger = logging.getLogger(__name__)

class SignIn(View):
    def get(self,request):
        return render(request,'account/sign_in.html')

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)

        # 認証成功
        if user is not None:
            login(request,user)
            logger.info(f'User {user.username} signed in')

            if 'next' in request.GET:
                # 元居たリンクへ遷移
                prev_link = request.GET['next']
                return redirect(prev_link)
            else:
                # トップページへ遷移
                return redirect('/')

        else:
            logger.warning(f'User {username} failed to sign in with password {password}')
            return_data = {'auth_message':'アカウントが存在しないか、パスワードが間違っています'}
            return render(request,'account/sign_in.html',return_data)
    


class QueryEmail(View):
    def get(self,request, email):
        try:
            user = CustomUser.objects.get(email=email)
            return JsonResponse({'user_id': user.id, 'username': user.username})
        except:
            return JsonResponse({'user_id': 'notFound', 'username': 'notFound'})
        

class PasswordReset(View):
    def get(self,request, user_id):
        return render(request,'account/password_reset.html')
    
    def post(self,request, user_id):
        user = CustomUser.objects.get(id=user_id)
        
        new_password = request.POST['new_password']
        user.set_password(new_password)
        user.save()
        
        logger.info(f'User {user.username} reset password')
        return redirect('/account/sign_in')
    
class MyPage(View):
    def get(self,request):

        return_data = {
            'username':request.user.username,
            'email' : request.user.email,
        }
        return render(request,'account/MyPage.html',return_data)

    def post(self,request):
        logger.info(f'User {request.user.username} updated profile')

        username = request.POST['username']
        new_password = request.POST['password']
        email = request.POST['email']


        request.user.username = username
        request.user.set_password(new_password)
        request.user.email = email
        request.user.save()

        return_data = {
            'username' : request.user.username,
            'email' : request.user.email,
        }
        logger.debug(return_data)
        return redirect('/')
    
class SignOut(View):
    def get(self,request):
        logout(request)
        logger.info(f'User {request.user.username} signed out')
        return redirect('/account/sign_in')
