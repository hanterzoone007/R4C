from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,'robots/html/index.html')

def get_json_data(request):
    if request == 'POST':
        print('post')
    return 12312

