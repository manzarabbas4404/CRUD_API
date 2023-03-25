from wsgiref.validate import validator
from xml.dom import ValidationErr
from rest_framework import serializers
from app.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields =['id','name','age','city']

# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=300,validators=[start_with_m])
#     age = serializers.IntegerField()
#     city = serializers.CharField(max_length=300)

#     def create(self,valiadted_data):
#         return Student.objects.create(**valiadted_data)

#     def update(self, instance, validated_data):
#         instance.name =validated_data.get('name', instance.name)
#         instance.age = validated_data.get('age', instance.age)
#         instance.city = validated_data.get('city',instance.city)
#         instance.save()
#         return instance




# Single field level validation
# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=300,read_only=True)


# field level validation
# def validate_age(self,value):
#     if value >= 50:
#         raise serializers.ValidationError('Age should be less than 50')
#     return value


# Object leval validations
# def validate(self, data):
#     age = data.get('age')
#     if age >= 5:
#         raise serializers.ValidationError('Data in appropriate..')
#     return data


# Function based validation
# def start_with_m(data):
#     if data[0].lower() != 'm':
#         raise serializers.ValidationError('Name should start with small m')
#     return data


# Python objects ---> {'name': 'manzar', 'age':23}
#Dumps [Convert Python object to json string]
# Json String ---> {"name": "manzar", "age":23}
#Loads [Convert json string to Python object]


# Serializer [TO convert complex data, objects, to Json data ]
# Complex Data ----> Python Native Data -----JSONrender (render)----> Json Data

# DeSerializer [TO convert Json Datato objects or complex data ]
# Json Data -----JSon Parser--> Python Native Data ----> Complex Data or objects


#BytesIO --->Json data streamer
#Parser ---> Json data to python native data

# The difference between function_based_api_view & class_based_api_view is like :

# for class based
# class StudentApi(APIView):
    # def get(self, request, pk=None, format=None):
    #     id = pk
    #     print('idididididididiidid',id)
    #     if id is not None:
    #         student_data = students.objects.get(id=id)  
    #         print('.................',student_data)
    #         serialized_data = studentsSerializer(student_data)
    #         return Response(serialized_data) 

# for function based
# from rest_framework.decorators import api_view
# @api_view(['GET','POST','PUT','PATCH','DELETE'])
# def StudentApi(request, pk=None):
    # if request.method == 'GET':
    #     id = pk
    #     print('idididididididiidid',id)
    #     if id is not None:
    #         student_data = students.objects.get(id=id)  
    #         print('.................',student_data)
    #         serialized_data = studentsSerializer(student_data)
    #         return Response(serialized_data)
