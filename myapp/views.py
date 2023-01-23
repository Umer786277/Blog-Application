from django.shortcuts import render
from .models import Post,ContactUs



from django.shortcuts import get_object_or_404,redirect
from .forms import CommentForm,ImageUploadForm,ContactForm

# Create your views here.

def index(request):
    return render(request,'home.html')


def services(request):
    return render(request,'services.html')



def contact(request):
    
    if request.method == 'POST':
        name=request.POST.get('Name')
        email=request.POST.get('Email')
       
        subject=request.POST.get('text')
        show=ContactUs(name=name,email=email,messsage=subject)
        show.save()
        return redirect('/')
    return render(request, 'contact.html')
    


def blog(request):
    posts=Post.objects.all()
  #  posts = Post.objects.filter(id=post_id).first()

    return render(request,'blog.html',{'posts':posts})





def about(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ImageUploadForm()
    return render(request, 'add_blog.html', {'form': form})





def detail(request):
    #It will provide us only one object at once 
    post =Post.objects.first()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('detail')
    else:
        form = CommentForm()



    return render(request, 'detail.html', {'post': post,'form': form})



