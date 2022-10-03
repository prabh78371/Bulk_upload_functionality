from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serilizers import Productserilizer
import pandas as pd
# Create your views here.


@api_view(['GET','POST'])
def upload_data(request):

    if request.method=='GET':
        prod = Product.objects.all()
        serilizer = Productserilizer(prod,many=True)
        return Response(serilizer.data)

    if request.method == 'POST' :          
            myfile = request.FILES['myfile']     
            uploaded_file = pd.read_excel(myfile)
            dbframe = uploaded_file
            header = list(dbframe.columns)
            if header == ['id', 'Name', 'price', 'image', 'imgs', 'gst','amount', 'brand']:   
                        for dbframe in dbframe.itertuples():
                            obj = Product.objects.create(name=dbframe.Name,price = dbframe.price,image = dbframe.image,img = dbframe.imgs,gst=dbframe.gst,amount=dbframe.amount,brand = dbframe.brand)
                            print(type(obj))
                            obj.save()
            else:
                    return Response("file doesn't have required fields")
            return Response("created Product Data")            