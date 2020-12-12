from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import Formulario

# Serializers define the API representation.
class FormularioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Formulario
        fields = ['id','nombre', 'apellido', 'rut', 'nserie', 'email', 'telefono']

# ViewSets define the view behavior.
class FormularioViewSet(viewsets.ModelViewSet):
    queryset = Formulario.objects.all()
    serializer_class = FormularioSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'', FormularioViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
   
]