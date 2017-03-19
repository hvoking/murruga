from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import Article

# Create your views here.
class ArticlesView(ListView):
    model = Article
    paginate_by = 5
    context_object_name = 'articles'
    template_name = 'articles.html'


def generate_fake_data(request):
    from model_mommy import mommy
    mommy.make('infiniti.Article', _quantity=20)
    return redirect('infiniti')
