from django.shortcuts import render

def home(request):
    return render(request, "core/home.html", {
        'title': 'Welcome to My Site',  # Example variable
        'message': 'It works! 🎉'
    })
