from django.shortcuts import render, redirect
from .models import Article
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'articles/new_article.html'
    fields = ('title', 'body')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
# ---- C R E A T E   B L O G


# ---- A L L   A R T I C L E S
class ArticleListView(ListView):
    model = Article
    template_name = "articles/all_articles.html"
    context_object_name = "articles"


# ---- O N E   A R T I C L E
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/one_article.html'


# ---- U P D A T E   A R T I C L E
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = 'articles/edit_article.html'
    fields = ('title', 'body')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


# ---- D E L E T E   A R T I C L E
class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'articles/delete_article.html'
    success_url = reverse_lazy('all_articles')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
