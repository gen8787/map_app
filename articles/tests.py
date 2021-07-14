from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from django.urls import reverse
from .models import Article


class ArticleTests(TestCase):
    print("*" * 60)

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@test.com",
            password="secret"
        )

        self.article = Article.objects.create(
            title="Test Title",
            body="Boooooooddddddyyyy",
            author=self.user
        )

    def test_string_representation(self):
        article = Article(title="Test Title")
        self.assertEqual(str(article), article.title)

    def test_article_content(self):
        self.assertEqual(f"{self.article.title}", "Test Title")
        self.assertEqual(f"{self.article.author}", "testuser")
        self.assertEqual(f"{self.article.body}", "Boooooooddddddyyyy")

    def test_article_list_view(self):
        response = self.client.get(reverse(""))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Boooooooddddddyyyy")
        self.assertTemplateUsed(response, "home.html")

    def test_article_detail_view(self):
        response = self.client.get("/articles/1/")
        no_response = self.client.get("/articles/10000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Test Title")
        self.assertTemplateUsed(response, "articles/one_article.html")

    def test_get_absolute_url(self):
        self.assertEqual(self.article.get_absolute_url(), '/articles/1/')

    def test_article_create_view(self):
        response = self.client.article(reverse('new_post'), {
            'title': 'New title',
            'body': 'New text',
            'author': self.user.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Article.objects.last().title, 'New title')
        self.assertEqual(Article.objects.last().body, 'New text')

    def test_article_update_view(self):
        response = self.client.article(reverse('edit_article', args='1'), {
            'title': 'Updated title',
            'body': 'Updated text'
        })
        self.assertEqual(response.status_code, 302)

    def test_article_delete_view(self):
        response = self.client.article(
            reverse('delete_article', args='1')
        )
        self.assertEqual(response.status_code, 302)
