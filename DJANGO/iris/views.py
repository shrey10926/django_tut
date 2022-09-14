from django.shortcuts import render, redirect
from iris.forms import IrisForm
from django.contrib import messages
from iris.models import PostModel, IrisModel
from django.contrib.auth.decorators import login_required
import joblib
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


model = joblib.load('final_model.joblib')
# Create your views here.

@login_required
def home(request):
    
    if request.method == 'POST':
        form = IrisForm(request.POST)
        
        if form.is_valid():
            
            fs = form.save()
            fs.user = request.user
            fs.save()
            
            sepal_length = form.cleaned_data.get('sepal_length')
            sepal_width = form.cleaned_data.get('sepal_width')
            petal_length = form.cleaned_data.get('petal_length')
            petal_width = form.cleaned_data.get('petal_width')
            messages.success(request, f'Data Submitted!')
            
            y_pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
            
            if y_pred[0] == 0:
                y_pred = 'Setosa'
            elif y_pred[0] == 1:
                y_pred = 'Virginica'
            else:
                y_pred = 'Versicolor'
            
            return render(request, 'iris/home.html', {'results' : y_pred})
    
    else:
        form = IrisForm()
        
    return render(request, 'iris/home.html', {'form' : form, 'posts' : PostModel.objects.all()})


class PostListView(ListView):
     model = PostModel
     template_name = 'iris/home.html'
     context_object_name = 'posts'
     # form_class = 'IrisForm'
     ordering = ['-date']
     paginate_by = 2
     
class PostDetailView(DetailView):
    model = PostModel
    

class PostCreateView(LoginRequiredMixin, CreateView):
    model = PostModel
    fields = ['title', 'content']
    
    def form_valid(self, form):
        
        form.instance.author = self.request.user
        
        return super().form_valid(form)
    
    


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PostModel
    fields = ['title', 'content']
    
    def form_valid(self, form):
        
        form.instance.author = self.request.user
        
        return super().form_valid(form)
    
    def test_func(self):
        
        post = self.get_object()
        
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PostModel
    success_url = '/'
    
    
    def test_func(self):
        
        post = self.get_object()
        
        if self.request.user == post.author:
            return True
        return False
    
    








@login_required
def about(request):
    
    return render(request, 'iris/about.html')







