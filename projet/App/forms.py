from django import forms
from django.forms import ModelForm
from crispy_forms.layout import Layout, Row, Column, Submit
from .models import Contact
from crispy_forms.helper import FormHelper

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django.forms import ModelForm
from .models import Contact  # adapte le chemin selon ton projet

class ContactForm(ModelForm):
    CHOIX_CONTACT = [
        (1, 'Email'),
        (0, 'Téléphone'),
    ]

    choix_contact = forms.ChoiceField(
        choices=CHOIX_CONTACT,
        widget=forms.RadioSelect,
        label="Méthode de contact"
    )

    nom = forms.CharField(  # permet de generer un imput de type text
        label = "Name",
        max_length = 100,
        required = True,
    )

    class Meta:
        model = Contact
        fields = ['nom', 'email', 'message', 'choix_contact']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # appeler le constructeur de base
        self.helper = FormHelper() # controle et personnalise le rendu du formulaire <form>
        self.helper.form_show_required = False # pour desactiver les asterisques
        self.helper.form_action='contact'
        self.helper.layout = Layout(
            Row(
                Column('nom',css_class='form-group col-md-12 mb-0'),
                Column('email', css_class='form-group col-md-12 mb-0'),
            ),
            'choix_contact',  # nom correct du champ radio
            'message',
           
            Submit('submit', 'Envoyer', css_class='btn btn-primary')
        )

    