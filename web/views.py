from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from web.models import Token, Expense, Income, User
import datetime


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