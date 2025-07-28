from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import HttpResponse

# Create your views here.

def contact_view(request):
    form = ContactForm() # on crée une instance form de la classe ContactForm
    if request.method == 'POST':
        print(request.POST['nom'])
        form = ContactForm(request.POST) # on cree une nouvelle instance avec les donnes du formulaires envoyé par user sous forme de JSON (dictionnaire)
        if form.is_valid():# verification de la validite de tous les champs du formulaire
            form.save() # save les donnees dans la BDD automatiquement.
            return redirect('success')
    return render(request, 'contact.html', {'form': form})





def success_view(request):
    return HttpResponse("<h1>Merci ! Votre message a été envoyé avec succès.</h1>")



