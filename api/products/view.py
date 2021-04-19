from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def get_post_product(request):
    if(request.method =="POST"):
        data = {"id": "name"}
        return Response(data, status = status.HTTP_200_OK)
    if(request.method=="POST"):
        
        return Response(data = "post medho", status = status.HTTP_201_CREATED)
