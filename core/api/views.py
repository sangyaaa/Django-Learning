from rest_framework.views import  APIView
from rest_framework.response import Response
from core.models import product
from core.api.serializers import ProductSerializer


class BookListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        products = product.objects.all()
        print(type(product))
        serializers = ProductSerializer(products, many=True)
        '''response =[
            {"name": "Think and grow rich", 
             "author":"Nepolean", "products": product}]
        return Response(response)'''
        
     
        response = {"products": serializers.data}
        return Response(response)
    def post(self, request, *args, **kwargs):
         print(request.query_params)
         print(request.data)
         search=request.query_params.get("search")
         product_ = product.objects.filter(title__icontains=search)
         serializer = ProductSerializer(product_, many=True)
         return Response(serializer.data)