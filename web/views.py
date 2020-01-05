# -*- coding: utf 8 -*-
import requests
from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from web.models import Token, Expense, Income, User, passwordresetcodes
import datetime
import random
import string
# for genrating random_str
from random import choice
from string import ascii_letters
from django.contrib.auth.hashers import make_password
from postmark import PMMail
from django.conf import settings

# Function for generating a random string with a fixed length :
def random_str(stringLength):
    return ''.join(choice(ascii_letters) for i in range(stringLength))


@csrf_exempt
def submit_expense(request) :
    """user submits an expense"""
    this_token = request.POST ['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST : 
        date = datetime.datetime.now()
    Expense.objects.create(text=request.POST['text'], user=this_user, amount=request.POST['amount'], date=date)
    return JsonResponse({
        'status' : 'ok'
    }, encoder=json.JSONEncoder)


@csrf_exempt
def submit_income(request) :
    """user submits an income"""
    this_token = request.POST ['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST : 
        date = datetime.datetime.now()
    Income.objects.create(text=request.POST['text'], user=this_user, amount=request.POST['amount'], date=date)
    return JsonResponse({
        'status' : 'ok'
    }, encoder=json.JSONEncoder)


# def register(request) :
#     if request.POST.has_key('requestcode') :

#         if not grecaptcha_verfiy(request):
#             _context = {'message' : 'sorry, captcha is not verfied'}
#             return render(request, 'register.html', _context)

#         if User.objects.filter(email = request.POST['email']).exists():
#             _context = {'message' : 'this email is verfied in past'}
#             return render(request, 'register.html', _context)  
        
#         if not User.objects.filter(username = request.POST['username']).exists():
#             code = random_str(28)
#             now = datetime.datetime.now()
#             password = make_password(request.POST['password'])
#             username = request.POST['username']
#             email = request.POST['email']
#             temporarycode = passwordresetcodes (email = email, username = username, time = now, code = code, password = password)
#             temporarycode.save()
#             message = PMMail(api_key = settings.POSTMARK_API_TOKEN,
#                              subject = 'فعالسازی اکانت بستون',
#                              sender = 'm.rezaakarami@gmail.com',
#                              to = email,
#                              text_body = 'برای فعالسازی اکانت خود روی لینک مقابل کایک کنید: http://bestoon.ir/register/?email={}&code={}'.format(email, code),
#                              tag = 'account request')
#             message.send()
#             _context = {'message' : 'ایمیل فعالسازی برای شما ارسال شد'}
#             return render (request, 'login.html', _context)

#         else :
#             _context = {'message' : 'نام کاربری دیگری را امتحان کنید'}
#             return render(request, 'register.html', _context)

#     elif request.GET.has_key('code') :
#         email = request.GET['email']
#         code = request.GET['code']
#         if passwordresetcodes.objects.filter(code=code).exists() :
#             new_temp_user = passwordresetcodes.objects.filter(code=code).get()
#             newuser = User.objects.create (username=new_temp_user.username, password=new_temp_user.password, email=email)
#             this_token = random_str(48)
#             token = Token.objects.create(user=newuser, token=this_token)
#             passwordresetcodes.objects.filter(code=code).delete()
#             _context = {'message' : 'اکانت شما فعال شد. توکن شما {} است'.format(this_token)}
#             return render(request, 'login.html', _context)
#         else :
#             _context = {'message' : 'کد فعالسازی شما معتبر نیست'}
#             return render(request, 'login.html', _context)

#     else :
#         _context = {'message' : ''}
#         return render(request, 'register.html', _context)



# # cptcha :
# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip


# def grecaptcha_verfiy(request):
#     data = request.POST
#     captcha_rs = data.get('g-recaptcha-response')
#     url = 'https://www.google.com/recaptcha/api/siteverify'
#     params = {
#         'secret' : settings.RECAPTCHA_SECRET_KEY,
#         'response' : captcha_rs,
#         'remoteip' : get_client_ip(request)
#     }
#     verify_rs = requests.get(url, params=params, verify=True)
#     verify_rs = verify_rs.json()
#     return verify_rs.get("sucsess", False)
   




#sign_up API :
@csrf_exempt
def register_api(request) :
    
    if User.objects.filter(email=request.POST['email']).exists() :
        return render (request, 'register.html', {'message' : 'این ایمیل قبلا ثبت شده است!'})

    else :
        password = make_password(request.POST['password'])
        username = request.POST['username']
        email = request.POST['email']
        newuser = User.objects.create (username=username, password=password, email=email)
        this_token = random_str(48)
        token = Token.objects.create(user=newuser, token=this_token)
        return render (request, 'register.html', {'message' : 'اکانت شما فعال گردید! توکن خود را ذخیره کنید : \n {}'.format(this_token)})


@csrf_exempt
def index(request):
    return render (request, 'index.html', {})


@csrf_exempt
def register(request):
    context = {'message' : ''}
    return render (request, 'register.html', context)


@csrf_exempt
def log_in(request):
    context = {'message' : ''}
    return render (request, 'log_in.html', context)



@csrf_exempt
def log_in_api(request):
    if User.objects.filter(password=request.POST['password']).exists() :
        # if User.objects.filter(username=request.POST['username']) == User.objects.filter(password=request.POST['password']):
        return render (request, 'log_in.html', {'message' : 'هستی'})
    else :
        return render (request, 'log_in.html', {'message' : 'نیستی'})


