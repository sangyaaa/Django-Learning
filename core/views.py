from django.http import JsonResponse
from django.shortcuts import render
from core.models import category



# Create your views here.
def home_api_view(request):
    fruits_price= [{"name":"apple","price":200},
                   {"name":"orange", "price":100}]
    response_data = [fruits_price]
    categories = category.objects.all().values("name") #ORM
    response_data = [
        {"name":category.get("name")} for category in categories
        ] #list comprenshion
    return JsonResponse(response_data, safe=False)


def about_api_view(request):
    book_price=[{"name":"science", "price":100},
                {"name":"math", "price":100}]
    response_data = [book_price]
    return JsonResponse(response_data, safe=False)
    
def about_view(request):
    return render (request,"about.html")

def product_view(request):
    data = request.POST
    queryset = category.objects.all() #select * from category
    if data:
        #select * from category where name = data.get("search")
        queryset = queryset.filter(name=data.get("search"))

    context = {"queryset":queryset}
    return render(request,"product.html", context)
