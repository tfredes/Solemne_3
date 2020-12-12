from django.test import TestCase
from .models import Article
from django.contrib.auth.models import User


class ArticleTestCase(TestCase):
    def setUp(self):
        userCreate = User.objects.create(
            username='admin',
            password='admin',
            email='admin@admin.cl'
        )
        Article.objects.create(
            title="Conectividad",
            description="Tenemos la mejor conectividad del país.  La red 4 y 5 G funcionan en todo el territorio nacional.",
            views=25576,
            publishedBy=userCreate,
            comments=12561)
        Article.objects.create(
            title="Precios",
            description="Tenemos los mejores precios en planes móviles como planes hogar, una buena relación calidad-precio.",
            views=67000,
            publishedBy=userCreate,
            comments=25789)

    def test_count_views(self):
        retiro10 = Article.objects.get(title="Conectividad")
        self.assertEqual(retiro10.views, 10)

    def test_count_comments(self):
        retiro10 = Article.objects.get(title="Conectividad")
        self.assertEqual(retiro10.comments, 30)

    def test_add_comment(self):
        conectividad = Article.objects.get(title="Conectividad")
        conectividad = conectividad.addComment()
        self.assertEqual(conectividad.comments, 31)

    def test_add_count_comments(self):
        conectividad = Article.objects.get(title="Conectividad")
        conectividad = conectividad.addCountComment(50)
        self.assertEqual(conectividad.comments, 80)

    def test_count1_views(self):
        precios = Article.objects.get(title="Precios")
        self.assertEqual(precios.views, 67000)
    
    def test_count1_comments(self):
        precios = Article.objects.get(title="precios")
        self.assertEqual(precios.comments, 5)