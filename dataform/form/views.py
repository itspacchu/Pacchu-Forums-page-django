from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm,SnipperForm,AnimeForm
from django.contrib  import messages
from .models import Snippet
from .resources import SnippetResouce
from django.shortcuts import render,get_object_or_404,reverse,redirect
import socket,random
# Create your views here.

custom_form_sent_msgs = ["You already sent a form 😜","Matrix-duplication prevented 🤖","Welcome Back Nerd",f'"{socket.gethostbyname(socket.gethostname())}" seem to already exist .. You New?','Darklord has prevented your entry 👿','Quantum break has been nullified','Havent i met you before?']
custom_form_success_msgs = ["Thank You for Showing Interest","Welcome onboard the codin-team 😎","You got a nerd pass 🎂","Love you ❤","LegionCodex welcomes you","print('you\\'ve shown interest in legion codex')"]


def contact(request):
    if(request.method == 'POST'):
        form = ContactForm(request.POST)
        if(form.is_valid()):
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            print(name,email)
    form = ContactForm()      
    return render(request,'form.html',{'form':form ,'messages':messages})

def snippet_detail(request):
    if(Snippet.objects.filter(user_ip = request.META['REMOTE_ADDR']).first() == None):
        if(request.method == 'POST'):
            form = SnipperForm(request.POST)
            if(form.is_valid()):
                instance = form.save(commit=False)
                instance.user_ip = request.META['REMOTE_ADDR']
                instance.save()
                messages.success(request,random.choice(custom_form_success_msgs))
                return redirect('success')
            else:
                messages.warning(request,'Something isnt right? Check your phone no is it +91 {NUMBER}')
    else:
        messages.warning(request,random.choice(custom_form_sent_msgs))
        return redirect('success')
        

            

    form = SnipperForm()  
    return render(request,'index.html',{'form':form ,})

def sucess_form(request):
    count_users = len(Snippet.objects.all())
    return render(request,'success.html',{'count_users':count_users})
   

def export_data(request):
    if(request.method == 'POST'):
        file_format = request.POST['file-format']
        user_resource = SnippetResouce()
        dataset = user_resource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
            return response        
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="exported_data.json"'
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="exported_data.xls"'
            return response   
    try:
        username = (Snippet.objects.filter(user_ip=socket.gethostbyname(socket.gethostname())).first()).name.split(' ')[0]
    except:
        username=" "
    return render(request, 'export.html',{'username':username})

def crew_page(requests):
    return render(requests,'about.html')


def bantt(requests):
    return render(requests,'bantt.html')

def anime_page(request):
    return render(request,'anime.html')
