from django.shortcuts import render

# Create your views here.

## Index Render
def home(request):
    return render(request, 'my_app/index.html')