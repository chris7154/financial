from django.shortcuts import render

# Create your views here.

def home_view (request):
    data = [1,23,4]
    content = {
        'nav': data,
        'first_name':obinna
    }
    return render(request, 'home_view.html', content)