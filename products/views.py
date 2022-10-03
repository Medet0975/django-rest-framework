from rest_framework.viewsets import ModelViewSet

from .models import Products
from .serializers import ProductSerializer


# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
