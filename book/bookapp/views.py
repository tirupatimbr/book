            # Python
import coreapi,coreschema
import base64
from io import StringIO

# Rest Framework
from rest_framework.decorators import api_view,APIView,renderer_classes,schema,parser_classes
from rest_framework_swagger.renderers import OpenAPIRenderer,SwaggerUIRenderer
from rest_framework import response,schemas
from rest_framework.schemas import AutoSchema,ManualSchema
from rest_framework import serializers
# Django
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import DefaultStorage
# project app
from bookapp.models import Books,Author,Products,Cart,Mobile,Profile,BaseImage
from bookapp.custom_schema import mobile_schema,register_schema,login_schema,reset_password_schema,mobile_get_schema,mobile_delete_schema

# other


# Create your views here.
@api_view(['POST'])
def book_details(request):
    if request.method == "POST":
        Name = request.data.get('Name')
        Author = request.data.get('Author')
        data = Books.objects.create(Name=Name,Author=Author)
        return JsonResponse({'success':True,'data':'successfully created'})


@api_view(['POST'])
def author_details(request):
    if request.method == "POST":
        Name = request.data.get('Name')
        Age = request.data.get('Age')
        Place =request.data.get('Place')
        data = Author.objects.create(Name=Name,Age=Age,Place=Place)
        return JsonResponse({'success':True,'data':'successfully created'})
    else:
        return JsonResponse({'success':False,'data':'provided post method'})

@api_view(['POST'])
def product_details(request):
    if request.method == "POST":
        Book_name = request.data.get('Book_name')
        Stock = request.data.get('Stock')
        Price = request.data.get('Price')
        # Book_details =request.data.get('Book_details')
        # Author_details = request.data.get('Author_details')
        data = Products.objects.create(Book_name=Book_name,
                                        Stock=Stock,
                                        Price=Price,
                                        )
        return JsonResponse({'success':True,'data':'successfully created'}) 

@api_view(['POST','GET','PUT','DELETE'])
def add_cart(request):
    if request.method == "POST":
        username = request.data.get('username')
        password = request.data.get('password')
        print(password,"password")
        user = authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            title = request.data.get('title')
            book_quantity = request.data.get('book_quantity')
            book_price = Products.objects.get(Price)
            # for i in book_quantity:
            if book_quantity:
                book_price *= book_quantity
                return book_price 
            book_name =request.data.get('book_name')          
            data = Cart.objects.create(title=title,
                            quantity=quantity,
                            user=request.user,
                            book=Products.objects.get(Book_name__icontains=book_name),
                            book_price = book_price)
            return JsonResponse({'success':True,'data':'item added to cart'})
        return JsonResponse({'success':False,'data':'username/password is invalid'})
        
    elif request.method == "GET":
        if request.data.get('title'):
            title = request.data.get('title')
            data = Cart.objects.filter(title=title).order_by('title','user','quantity')    
            get = list(data.values())
            return JsonResponse(get,safe=False)
        
        elif request.data.get('user_id'):
            user_id = request.data.get('user_id')
            data = Cart.objects.filter(user_id=user_id).order_by('title','user','quantity')    
            get = list(data.values())
            return JsonResponse(get,safe=False)
        else:
            data = Cart.objects.all()
            get = list(data.values())
            return JsonResponse(get,safe=False)
    
    elif request.method == "PUT":
        if request.data.get('user_id'):
            user_id = request.data.get('user_id')
            if request.data.get('quantity'):
                quantity = request.data.get('quantity')
                data = Cart.objects.filter(user_id=user_id).update(quantity=quantity)
                return JsonResponse({'success':True,'data':'quantity updated'})
            return JsonResponse({'success':True,'data':'success'})

    elif request.method == "DELETE":
        if request.data.get('user_id'):
            data = Cart.objects.filter(user_id=user_id).delete()
            return JsonResponse({'success':True,'data':'cart deleted'})
        else:
            return JsonResponse({'success':False,'data':'Cart is deleted with user_id only'})


        


@api_view(['POST'])
@schema(register_schema)
def registration(request):
    if request.method == "POST":
        username = request.data.get('username')
        email = request.data.get('email')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return JsonResponse({'success':False,'data':'Username already exists'})
            elif User.objects.filter(email=email).exists():
                return JsonResponse({'success':False,'data':'Email already exists'})
            else:
                data = User.objects.create_user(username=username,
                                                email=email,
                                                password=password1)
                return JsonResponse({'success':True,'data':'Successfully registered'})

        else:
            return JsonResponse({'success':False,'data':'password is not matched'})
    else:
        return JsonResponse({'success':False,'data':'Method is in valid'}) 
  

@api_view(['POST'])
@schema(login_schema)
def login_user(request):
    if request.method == "POST":
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return JsonResponse({'success':True,'data':'Successfully logged in'})
        else:
            return JsonResponse({'success':False,'data':'Username/password is incorrect'})

@api_view(['GET'])
def logout_user(request):
    if request.method == "GET":
        auth.logout(request)
        return JsonResponse({'success':True,'data':'your logged out'})


@api_view(['POST'])
@schema(reset_password_schema)
def password_reset(request):
    if request.method == "POST":
        email = request.data.get('email')
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            send_mail(
                    'password reset',
                    'you requested for password reset\n your OTP is 789456',
                    'naniprashanth145@gmail.com',
                    [email],
                    fail_silently=False,
                )
            return JsonResponse({'success':True,'data':'email sent'})
        return JsonResponse({'success':False,'data':'username/password is invalid'})

@api_view(['POST'])
@schema(mobile_schema)
def mobile(request):
    # success = False
    # response = {}
    if request.method == "POST":
        brand = request.data.get('brand')
        mobile_model = request.data.get('mobile_model')
        price = request.data.get('price')
        stock = request.data.get('stock')
        data = Mobile.objects.create(brand=brand,mobile_model=mobile_model,price=price,stock=stock)
        return JsonResponse({'success':True,'data':'mobile posted'})

@api_view(['GET'])
@schema(mobile_get_schema)
def mobile_get(request):
    if request.method =="GET":
        ID = request.GET.get('id')
        print(ID,"ID")
        data = Mobile.objects.filter(id=ID).order_by('brand','mobile_model','price','stock','available')
        get = tuple(data.values())
        return JsonResponse(get,safe=False)
@api_view(['DELETE'])
@schema(mobile_delete_schema)
def mobile_delete(request):
    print(request.method,"method")
    if request.method == "DELETE":
        print(request.GET,"request")
        ID= request.GET.get('id')
        print(ID,"ID")
        data = Mobile.objects.filter(id=ID).delete()
        return JsonResponse({'success':True,'data':'deleted'})
    

@api_view(['GET'])
def all_list(request):
    if request.method =="GET":
        name = request.GET.get("name")
        age = request.GET.get("age")
        place = request.GET.get("place")
        book = request.GET.get("book")
        
        if (request.GET.get("name") or request.GET.get("age") or request.GET.get("place") or request.GET.get("book")):
            
            if (name and age and place):
                author_qs = Author.objects.filter(Q(Name__icontains=name)&Q(Age__gte=age)&Q(Place__icontains=place))
                print("name and age and place")
                return JsonResponse(list(author_qs.values()),safe=False)
            elif (name and age and book):
                author_qs =Author.objects.filter(Q(Name__icontains=name)&Q(Age__gte=age)&Q(Book__Name__icontains=book))
                print("name and age and book")
                return JsonResponse(list(author_qs.values()),safe=False)
            elif (name and place and book):
                author_qs =Author.objects.filter(Q(Name__icontains=name)&Q(Place__icontains=place)&Q(Book__Name__icontains=book))
                print("name and place and book")
                return JsonResponse(list(author_qs.values()),safe=False)
            elif (name and age):
                author_qs = Author.objects.filter(Q(Name__icontains=name)&Q(Age__gte=age))
                print("name and age")
                return JsonResponse(list(author_qs.values()),safe=False)
            elif (name and place):
                author_qs = Author.objects.filter(Q(Name__icontains=name)&Q(Place__icontains=place))
                print("name and place")
                return JsonResponse(list(author_qs.values()),safe=False)
            elif (name and book):
                author_qs = Author.objects.filter(Q(Name__icontains=name)&Q(Book__Name__icontains=book))
                print("name and book")
                return JsonResponse(list(author_qs.values()),safe=False)
            elif (age and book):
                author_qs = Author.objects.filter(Q(Age__gte=age)&Q(Book__Name__icontains=book))
                print("age and book")
                return JsonResponse(list(author_qs.values()),safe=False)
            elif (age and place):
                author_qs = Author.objects.filter(Q(Age__gte=age)&Q(Place__icontains=place))
                print("age and place")
                return JsonResponse(list(author_qs.values()),safe=False)
            elif (place and book):
                author_qs = Author.objects.filter(Q(Place__icontains=place)&Q(Book__Name__icontains=book))
                print("place and book")
                return JsonResponse(list(author_qs.values()),safe=False)
            elif (name):
                author_qs =Author.objects.filter(Name__icontains=name)
                print("name")
                return JsonResponse(list(author_qs.values()),safe=False)
            elif (age):
                author_qs =Author.objects.filter(Age__gte=age)
                print("age")
                return JsonResponse(list(author_qs.values()),safe=False)
            elif (book):
                author_qs =Author.objects.filter(Book__Name__icontains=book)
                print("book")
                return JsonResponse(list(author_qs.values()),safe=False)
            elif (place):
                author_qs =Author.objects.filter(Place__icontains=place)
                print("place")
                return JsonResponse(list(author_qs.values()),safe=False)
            else:

                author_qs = Author.objects.filter(Q(Name=name)&Q(Age__gte=age)&Q(Place=place)&Q(Book__Name=book))
                print("all fileds")
                return JsonResponse(list(author_qs.values()),safe=False)
        
            return JsonResponse({'success':False,'data':'method is invalid'})



@api_view(['GET'])
def profile_image(request):
    if request.method == "GET":
        username = request.GET.get('username')
        password = request.GET.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            ID = user.id
            image_qs = Profile.objects.all().exclude(id=ID)
            return JsonResponse(list(image_qs.values()),safe=False)


@api_view(['POST'])
def base_64_post(request):
    if request.method == "POST":
        file_qs = request.FILES['image']
        imgdata = base64.b64decode(file_qs)
        filename = 'some_image3.jpeg'
        if file_qs:
            img = BaseImage.objects.create(user=request.user,base_image=filename)
            img.save()
        return JsonResponse({'success':True,'data':'image posted'})


@api_view(['POST'])
def base_post(request):
    if request.method == "POST":
        file_qs = request.FILES['file']
        if file_qs:
            img = BaseImage.objects.create(user=request.user,base_image=file_qs)
        return JsonResponse({'success':True,'data':file_qs})






    