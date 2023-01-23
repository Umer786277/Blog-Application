from django import forms

from .models import Comment,Post,ContactUs

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')





#class ImageForm(forms.ModelForm):
 #   """Form for the image model"""
  #  class Meta:
   #     model = Post
    #    fields = ('image','body')





class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image','body',)

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('name','email','message')