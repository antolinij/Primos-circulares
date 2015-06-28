from django.shortcuts import render
from base.models import Prime
from django.http import HttpResponse
import json

def index(request):
    #creamos un diccionario para pasar al template
    context_dict = {'variable': "Vengo de la vista y soy una variable"}
    numbers = Prime.objects.all()

    return render(request, 'base/home.html', {'numbers': numbers })

def is_circular(request):
    if request.method == 'GET':
        from base import utils

        number = request.GET['number']
        if not number.isdigit():
            response_data = {}
            response_data['result'] = 'failed'
            response_data['message'] = 'El numero ingresado no es un entero...'
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        
        number= int(number)
        
        if not utils.is_prime(number):
            response_data = {}
            response_data['result'] = 'failed'
            response_data['message'] = 'El numero ingresado no es primo, mucho menos circular...'
            return HttpResponse(json.dumps(response_data), content_type="application/json") 
        
        if not utils.is_circular(number):
            response_data = {}
            response_data['result'] = 'failed'
            response_data['message'] = 'El numero ingresado no es un circular primo...'
            return HttpResponse(json.dumps(response_data), content_type="application/json")

        circulares= []
        num= number
        for i in range(len(str(num))):
            num= str(num)[len(str(num)) -1:]+str(num)[:-1]
            circulares.append(num)
        circulares.remove(str(number))
        response_data = {}
        response_data['result'] = 'success'
        response_data['number'] = number
        response_data['message'] = 'El numero ingresado es un circular primo...'
        response_data['data']= circulares
        return HttpResponse(json.dumps(response_data), content_type="application/json")
        


