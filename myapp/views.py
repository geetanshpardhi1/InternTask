from django.shortcuts import render
import requests
from .models import *
from .forms import *


#view for landing page
def index(request):
    
    #used api for dynamic quotes funtionality on landing page
    category = 'happiness'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': 'I4VU3pM/rM7OQsg8HSZLnQ==oLfdWl6wydU4sdl3'})
    
    if response.status_code == requests.codes.ok:
            quotes_data = response.json()
            quote = quotes_data[0]['quote']
            author = quotes_data[0]['author']
    
    #code to hadle post data from client 
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = TestForm()
    
    return render(request,'myapp/index.html',{'form':form,'quote':quote,'author':author})

#creating view to display the name and emails saved in database
def data_view(request):
    obj = TestModel.objects.all()
    return render(request,'myapp/dataview.html',{'data':obj})
    

