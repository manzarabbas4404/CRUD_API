
from asyncio import streams
from functools import partial
from operator import imod
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View


@method_decorator(csrf_exempt,name='dispatch')
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            id = python_data.get('id', None)
            if id is not None:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                json_res = JSONRenderer().render(serializer.data)
                return HttpResponse(json_res, content_type = 'application/json')  
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type= 'application/json')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            json_data = request.body
            stream = io.BytesIO(json_data)
            json_data = JSONParser().parse(stream)
            serializer = StudentSerializer(data = json_data)
            if serializer.is_valid():
                serializer.save()
                res ={'msg':'Data created successfully'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type='application/json')
            json_data = JSONRenderer.render(serializer.error_messages)
            return HttpResponse(json_data, content_type='application/json')
        
    def put(self, request, *args, **kwargs):
        if request.method =='PUT':
            json_data = request.body
            stream = io.BytesIO(json_data)
            json_data = JSONParser().parse(stream)
            id = json_data.get('id')
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu, data = json_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                res = {'res':'Data Updated'}
                json_data = JSONRenderer().render(res)
                return HttpResponse (json_data, content_type = 'application/json')
            json_data= JSONRenderer().render(serializer.errors)
            return HttpResponse (json_data, content_type ='application/json')

    def delete(self, request, *args, **kwargs):    
        if request.method == 'DELETE':
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            id = pythondata.get('id')
            stu = Student.objects.get(id=id)
            stu.delete()
            res ={ 'res': ' Deleted Successfully'}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse (json_data, content_type= 'application/json')
            return JsonResponse(res, safe = True)


# Create your views here.
# @csrf_exempt
# def getfunction(request):
#     if request.method == 'GET':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         id = python_data.get('id', None)
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             json_res = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_res, content_type = 'application/json')  
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type= 'application/json')

#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         json_data = JSONParser().parse(stream)
#         serializer = StudentSerializer(data = json_data)
#         if serializer.is_valid():
#             serializer.save()
#             res ={'msg':'Data created successfully'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         json_data = JSONRenderer.render(serializer.error_messages)
#         return HttpResponse(json_data, content_type='application/json')
    

#     if request.method =='PUT':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         json_data = JSONParser().parse(stream)
#         id = json_data.get('id')
#         stu = Student.objects.get(id=id)
#         serializer = StudentSerializer(stu, data = json_data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'res':'Data Updated'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse (json_data, content_type = 'application/json')
#         json_data= JSONRenderer().render(serializer.errors)
#         return HttpResponse (json_data, content_type ='application/json')

    
#     if request.method == 'DELETE':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         stu = Student.objects.get(id=id)
#         stu.delete()
#         res ={ 'res': ' Deleted Successfully'}
#         # json_data = JSONRenderer().render(res)
#         # return HttpResponse (json_data, content_type= 'application/json')
#         return JsonResponse(res, safe = True)




