from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import HttpResponse

# Create your views here.

def contact_view(request):
    form = ContactForm() # on crée un instance form de la classe ContactForm
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    return render(request, 'contact.html', {'form': form})





def success_view(request):
    return HttpResponse("<h1>Merci ! Votre message a été envoyé avec succès.</h1>")



