from rest_framework.viewsets import ModelViewSet

from core.models import Product
from core.serializers.product import ProductSerializer, ProductDetailSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()  # pylint: disable=no-member
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ProductDetailSerializer
        return ProductSerializer
