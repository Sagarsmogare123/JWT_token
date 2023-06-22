from rest_framework import viewsets
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




# class CategoryViewSet(viewsets.ViewSet):
#     def list(self, request):
#         # Logic to retrieve a list of category
#         queryset = Category.objects.all()
#         serializer = CategorySerializer(queryset, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         # Logic to create a new category
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

#     def retrieve(self, request, pk=None):
#         # Logic to retrieve a single category by its identifier (pk)
#         try:
#             category = Category.objects.get(pk=pk)
#         except category.DoesNotExist:
#             return Response(status=404)

#         serializer = CategorySerializer(category)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         # Logic to update an existing category
#         try:
#             category = Category.objects.get(pk=pk)
#         except category.DoesNotExist:
#             return Response(status=404)

#         serializer = CategorySerializer(category, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     def destroy(self, request, pk=None):
#         # Logic to delete an existing category
#         try:
#             category = Category.objects.get(pk=pk)
#         except Category.DoesNotExist:
#             return Response(status=404)

#         category.delete()
#         return Response(status=204)




# class ProductViewSet(viewsets.ViewSet):
#     def list(self, request):
#         # Logic to retrieve a list of category
#         queryset = Product.objects.all()
#         serializer = ProductSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         # Logic to create a new category
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

#     def retrieve(self, request, pk=None):
#         # Logic to retrieve a single category by its identifier (pk)
#         try:
#             product = Product.objects.get(pk=pk)
#         except product.DoesNotExist:
#             return Response(status=404)

#         serializer = ProductSerializer(product)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         # Logic to update an existing category
#         try:
#             product = Product.objects.get(pk=pk)
#         except product.DoesNotExist:
#             return Response(status=404)

#         serializer = CategorySerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     def destroy(self, request, pk=None):
#         # Logic to delete an existing category
#         try:
#             product = Product.objects.get(pk=pk)
#         except product.DoesNotExist:
#             return Response(status=404)

#         product.delete()
#         return Response(status=204)
