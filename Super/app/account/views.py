import logging
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import CustomUser, Profile
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
    

class SignOut(View):
    def get(self,request):
        logout(request)
        logger.info(f'User {request.user.username} signed out')
        return redirect('/account/sign_in')

class MyPage(View):
    def get(self,request):
        try:
            profile = Profile.objects.get(user=request.user)
        except:
            profile = Profile.objects.create(user=request.user,name='',class_id='')

        return_data = {
            'username':request.user.username,
            'class_id' : profile.class_id,
        }
        return render(request,'account/MyPage.html',return_data)

    def post(self,request):
        logger.info(f'User {request.user.username} updated profile')

        username = request.POST['username']
        class_id = request.POST['class_id']

        # profileを選択
        profile = Profile.objects.get(user=request.user)

        request.user.username = username
        request.user.save()
        profile.class_id = class_id
        profile.save()

        return_data = {
            'username' : username,
            'class_id' : profile.class_id,
        }
        logger.debug(return_data)
        return render(request,'account/MyPage.html',return_data)