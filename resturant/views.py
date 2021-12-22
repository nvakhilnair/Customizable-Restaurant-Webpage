from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Resturant,Reviews,Subscriber,Contact_forum,Reservation_forum
from django.core.mail import send_mail

# Create your views here.

def homepage(request):
    data = Resturant.objects.all()
    Review = Reviews.objects.all()
    Review = Review.values()
    try:
        data  = data.values()[0]
        ##### tagline spliting the sentence into 2 ##########
        if(len(data['tagline'])>70):
            data['tagline1'],data['tagline1'] = data['tagline'][:data['tagline'][:len(data['tagline'])//2].rfind(' ')],data['tagline'][data['tagline'][:len(data['tagline'])//2].rfind(' ')+1:]
        else:
            data['tagline1'],data['tagline1'] = data['tagline'],''

        #### story spliting into paragraph ##########
        cnt = data['story'].count('.')
        index = [index for index, char in enumerate(data['story']) if char == '.']
        if(len(data['story'])>250 and cnt>3):
            data['story1'],data['story2'] = data['story'][:index[cnt//2-1]+1],data['story'][index[cnt//2-1]+2:]
        else:
            data['story1'],data['story2'] = data['story'],''
    except:
        pass
    
    return render(request, "index.html",{'data': data,'Review':Review})

def add_subcriber(request):
    if request.method == 'POST':
        email=request.POST.get('task')
        print(email)
        push_to_DB = Subscriber.objects.create(email=email)
        push_to_DB.save()
    return HttpResponse('Added')

def contact_forums(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        push_to_DB = Contact_forum.objects.create(name=name,email=email,subject=subject,message=message)
        push_to_DB.save()
        send_mail(subject, message, email, ['admin@example.com'])
    return HttpResponse('Submitted')

def reservation_forums(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        person=request.POST.get('person')
        date=request.POST.get('date')
        time=request.POST.get('time')
        phone=request.POST.get('phone')
        push_to_DB = Reservation_forum.objects.create(name=name,email=email,person=person,date=date,time=time,phone=phone)
        push_to_DB.save()
    return HttpResponse('Booked')


def contact(request):
    return render(request, "contact.html")

def gallery(request):
    return render(request, "gallery.html")

def menu(request):
    return render(request, "menu.html")

def reservation(request):
    return render(request, "reservation.html")
