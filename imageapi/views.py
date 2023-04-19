from django.shortcuts import render, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from imageapi.models import UserResponse
from imageapi.serializers import ResponseSerializer
from django.views.decorators.csrf import csrf_exempt
import json
import io 
from django.http import JsonResponse
# Create your views here.
@csrf_exempt
def index(request):
    data = {'message':'index route works'}
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type = 'applications/json')
@csrf_exempt
def create_data(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serialized = ResponseSerializer(data = python_data)
        if serialized.is_valid():
            serialized.save()
            data = {'message':'Data created successfully'}
            json_response = json.dumps(data)
            return HttpResponse(json_response, content_type = 'application/json')
        json_response = JSONRenderer().render(serialized.errors)
        return HttpResponse(json_response, content_type = 'application/json')
    data = {'message':'Registered successfully!'}
    return JsonResponse(data)
    
@csrf_exempt
def get_data(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        user_name = python_data.get('user_name', None)
        if user_name is not None:
            print(user_name)
            user_response = UserResponse.objects.filter(user_name = user_name)
            if user_response.exists():  
                serialized = ResponseSerializer(user_response, many = True)
                json_response = JSONRenderer().render(serialized.data)
                return HttpResponse(json_response, content_type = 'application/json')
            else:
                data = {'message':'Username invalid'}
                json_data = json.dumps(data)
                return HttpResponse(json_data, content_type = 'application/json')
@csrf_exempt
def test(request):
    if request.method == 'POST':
        data = {'message':'Imageapi route works'}
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type = 'application/json')
