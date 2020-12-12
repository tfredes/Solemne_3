from django.contrib import admin
from django.urls import path, include
from rest_framework import routers,serializers, viewsets
from .models import Article
# Clase serializadora de Usuarios
class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article 
        fields = ['id','title','description','publishedBy', 'views','comments', 'image']

# Clase de viewset que hace el puente entre bd - serealizacion
class ArticleViewSet(viewsets.ModelViewSet):
    # Query que ejecutara a la bd
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

router = routers.DefaultRouter()
router.register(r'', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
