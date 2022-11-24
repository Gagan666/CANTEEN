
# Create your views here.
from rest_framework import status
from django.db import IntegrityError
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view,permission_classes
from .models import NewUser,Foods,Categories
from django.core.exceptions import ObjectDoesNotExist
from .serializers import FoodsSerialier


class Index(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request):
        return Response("Working...")


class CreateUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print(request.data)
        myDict = request.data
        #convert Querydict to python dictionary
        # myDict = data.dict()
        try:
            user = NewUser.objects.get(phone=myDict['phone'])
            return Response({"message": "Phone number already present"})
        except ObjectDoesNotExist:
            user = NewUser.objects.create_user(user_name=myDict['user_name'], password=myDict['password'],phone=myDict['phone'])
            return Response({"message":"Successfully created"})

class BlackListToken(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])

def createFood(request):
    print(request.user)
    name=request.data["name"]
    price = request.data["price"]
    category = request.data["category"]
    image = request.data['image']
    c=Categories.objects.get(category_name=category)
    food = Foods.objects.create(food_name=name,price=price,category=c,image = image)
    f = FoodsSerialier(food,many=False)
    return Response(f.data)

@api_view(['GET'])
def dispFoodOnCat(request,category):
    category=category.lower()
    if category!="all":
        c=Categories.objects.get(category_name=category)
        foods = Foods.objects.filter(category=c)
    else:
        foods = Foods.objects.all()
    serializer = FoodsSerialier(foods,many=True)
    return Response(serializer.data)



