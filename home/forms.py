from django import forms
from blog.models import ContactUs

class ContactForm(forms.ModelForm):
       class Meta:
           model = ContactUs
           fields = "__all__"
           widgets = {
               "subject" : forms.TextInput(attrs={
                   "class" : "form-control",
                   "placeholder" : "type your subject ..."
               }),
               "text" : forms.Textarea(attrs={
                   "class" : "form-control",       
               })
            }