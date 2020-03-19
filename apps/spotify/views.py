from django.shortcuts import render

# Create your views here.
def gato(request):
    return render(request, 'gato.html', {})