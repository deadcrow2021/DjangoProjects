from django.shortcuts import redirect, render

from mainapp.forms import CreateEmail, SendToEmails

def home(request):
    a = 'Homepage'
    return render(request, 'mainapp/index.html', {'a': a})

def add_email(request):
    if request.method =='POST':
        form = CreateEmail(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateEmail
        return render(request, 'mainapp/add_email.html', {'form': form})
    
def send(request):
    if request.method =='POST':
        form = SendToEmails(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SendToEmails
        return render(request, 'mainapp/send.html', {'form': form})