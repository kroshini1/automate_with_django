from django.shortcuts import render
from django.http import HttpResponse
from dataentry.tasks import celery_test_task



def home(request):
    return render(request,'dataentry/home.html')

def celery_test(request):
    # i want to execute time consuming task here
    celery_test_task.delay()
    return HttpResponse('it was working successfully')
    
