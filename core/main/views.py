from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    Header_list = Header.objects.all()
    showcase_list = showcase.objects.all()
    showcase2_list = showcase2.objects.all()
    services_list = services.objects.all()
    designers_list = designers.objects.all()
    designers_img_list = designers_img.objects.all()
    
    
    packages_list = packages.objects.all()
    pro_list = pro.objects.all()
    advantage_list = advantage.objects.all()
    proAdvantage_list = proAdvantage.objects.all()




    context = {
        'Header_list':Header_list,
        'showcase_list':showcase_list,
        'showcase2_list':showcase2_list,

        'services_list':services_list,

        'designers_list':designers_list,
        'designers_img_list':designers_img_list,

        'packages_list':packages_list,
        'pro_list':pro_list,
        'advantage_list':advantage_list,
        'proAdvantage_list':proAdvantage_list
    }
    return render(request , 'index.html' , context)