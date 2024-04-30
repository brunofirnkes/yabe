from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import *
from .serializers import *

class DetailOrSummarySerializer:
    list_serializer_class = None
    def get_serializer_class(self):
        if self.action == "list" and self.list_serializer_class is not None:
            return self.list_serializer_class
        return self.serializer_class

class CommonViewset(DetailOrSummarySerializer, viewsets.ReadOnlyModelViewSet):
    pass

class ProductView(CommonViewset):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    list_serializer_class = ProductSummarySerializer
    permission_classes = [AllowAny]