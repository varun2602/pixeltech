from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
import requests
import random
import json
from imageapp.models import CustomUser

# Create your views here.
otp = []
username_store= []
password_store = []
@login_required(login_url = '/login')
def index(request):
    context = {'user':request.user}
    return render(request, 'index.html',context)
@csrf_exempt
def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        try:
            user = CustomUser.objects.get(username = username)
            username_store.append(username)
            password_store.append(password)
            otp.append(random.randint(1000, 9999))
            otp_temp = otp[0]
            phone_number = int(user.phone_number)
            print('Phone', phone_number)
            url = "https://www.fast2sms.com/dev/bulkV2"
            payload = f"sender_id=TXTIND&message=Your otp is:{otp_temp}&route=v3&numbers={phone_number}"
            headers = {
                'authorization': "ejtXSpaqEFKmzcNvx9duwQkYrZgof5nHbGAR1W8CIBs4hyOU7TQ6pW04KC1z5dwa9HNjsDOLnABqefG2",
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache",
                }
            response = requests.request("POST", url = url, data=payload, headers=headers)
            print(response)
     
            return HttpResponseRedirect(reverse('verify_otp'))
        except CustomUser.DoesNotExist:
            return render(request, 'login.html', {'message':'Invalid username'})
        

@csrf_exempt
def verify_otp(request):
    if request.method == 'GET':
        return render(request, 'otp.html')
    if request.method == 'POST':
        otp_entered = int(request.POST.get('otp'))
        
        # return HttpResponse(f'{otp_entered}')
       
        if otp_entered == otp[0]:

            username1 = username_store[0]
            password1 = password_store[0]
            print(password1)
            user =  CustomUser.objects.get(username = username1)
            user_check = authenticate(username = username1, password = password1)
            print(user_check)
            
            if user_check is not None:
                login(request, user_check)
                print('logged in')
                
                return redirect('index')
        #     else:
        #         context = {'message':'Invalid credentials'}
             
        #         return render(request, 'login.html', context)
                
        # else:
            
        #     return render(request, 'otp.html', {'message':'OTP invalid'})


@csrf_exempt
def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        phone = str(request.POST.get('phone'))

        if password != cpassword:
            context = {'message':'Confirm password properly!'}
            return JsonResponse(context)

        try:
            user_check = CustomUser.objects.get(username = username)
            context = {'message':'Username is taken !'}
            return JsonResponse(context)
        except CustomUser.DoesNotExist:
            user_create = CustomUser.objects.create_user(username = username, password = password, phone_number = phone)
            user_create.save()
            data = {'message':'Registered successfully!'}
            return JsonResponse(data)
@csrf_exempt
def validate_name(request):
    username = request.POST.get('username')
    try:
        valid = CustomUser.objects.get(username = username)
        data = {'r':200}
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type = 'application/json')
    except CustomUser.DoesNotExist:
        data = {'r':20}
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type = 'application/json')

    return HttpResponse('successful')

def logout_view(request):
    print('logout called')
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@csrf_exempt
def image_slider(request):
        if request.method == 'GET':
            return render(request, 'image.html')
        if request.method == 'POST':
            print("image route successful")
            buttonid = request.POST.get('buttonid')
            imageid = request.POST.get('imageid')
            user = request.user.username
            # print(type(buttonid), type(imageid), type(user)) 
            # print(user)
            
            data = {
                'user_name':user,
                'user_response':buttonid,
                'response_image':imageid
            }
            json_data = json.dumps(data)
            print(json_data)
            r = requests.post(url = 'https://pixeltech.onrender.com/img/create_data/', data = json_data)

            print(r.json())
            
            return HttpResponse('Success!')
@csrf_exempt
def test(request):
    data = {'message':'This is test'}
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type = 'application/json')

@csrf_exempt
def result(request):
    if request.method == 'GET':
        user = request.user.username
        print(user)
        data = {
            'user_name':user
        }
        json_data = json.dumps(data)
        # r = requests.get(url = 'https://pixeltech.onrender.com/img/get_data/', data = json_data)
        r = requests.post(url = 'https://pixeltech.onrender.com/img/test')
       
        response = r.json()
        context = {'response':response}
        return render(request, 'test.html', context)

        context = {'response':response}
        return render(request, 'results.html', context)
    
@csrf_exempt
def test_route(request):
    otp_entered = request.POST.get('otp')
    print(otp_entered)
    return HttpResponse(f'{otp_entered}')



