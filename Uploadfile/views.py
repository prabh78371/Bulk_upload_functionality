from dataclasses import dataclass
from django.shortcuts import render
import xlwt
from django.http import HttpResponse
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tablib import Dataset
import csv
from django.core.files.storage import FileSystemStorage
from .serilizers import Productserilizer
# Create your views here.


@api_view(['GET','POST'])
def upload_data(request):

    if request.method=='GET':
        prod = Product.objects.all()
        serilizer = Productserilizer(prod,many=True)
        return Response(serilizer.data)


    if request.method == 'POST':
        dataset = Dataset()
        myfile = request.FILES['myfile']
        # load excel file data
        import_data = dataset.load(myfile.read(),format='xlsx')
        # load data into django model
        for data in import_data:
            print(data)
            value= Product(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7])
            value.save()
        return Response("success")



































        # import_data = Dataset.load(file_data.read(),format='xlsx')
        # for data in import_data:
        #     print(data)
        #     value= Product(data[0],data[1],data[2],data[3],data[4])
        #     value.save()

        # return("sucess")

