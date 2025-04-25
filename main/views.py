from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def add(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    phone = request.GET.get('phone')
    address = request.GET.get('address')
    return render(request, 'main/result.html', {'name': name, 'email': email, 'phone': phone, 'address': address})