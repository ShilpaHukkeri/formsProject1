from django.shortcuts import render
from myApp.forms import Feedback
def view(r):
    f=Feedback()
    if r.method=='POST':
        f=Feedback(r.POST)
        if f.is_valid():
            name=f.cleaned_data['name']
            roll=f.cleaned_data['roll']
            email=f.cleaned_data['email']
            comments=f.cleaned_data['comments']
            d={'name1':name,'roll1':roll,'email1':email,'comments1':comments}
            return render(r,'myApp/output.html',d)
    d={'form':f}
    return render(r,'myApp/input.html',d)
    
    
