from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def add(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST['phone']
    address = request.POST.get('address')
    return render(request, 'main/result.html', {'name': name, 'email': email, 'phone': phone, 'address': address})