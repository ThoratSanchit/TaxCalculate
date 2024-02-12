from decimal import Decimal
from django.shortcuts import render
from .serializers import incometaxSerializers
from .models import incometax
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class Calculate_tax(APIView):
    def post(self,request,*args, **kwargs):
        serializer=incometaxSerializers(data=request.data)
        if serializer.is_valid():
            amount=serializer.validated_data['income']
            age=serializer.validated_data['age']
           
            if amount<=250000 and age<=60:
          
                return Response({"You have no tax."})
            elif amount>250001 and amount<1000000 and age<60:
                 tax=amount*Decimal(20/100) 
                 return Response({"Amount age  ":amount, "Total Tax is":tax,})
            elif amount>1000000 and age<60:
                tax=amount*Decimal(30/100) 
                return Response({"Amount age  ":amount, "Total Tax is":tax,})
            elif age>60 and age<80 and amount>300000:
                return Response({"You have no tax."})
            elif age>60 and age<80 and amount>300001 and amount< 500000:
                tax=amount*Decimal(5/100) 
                return Response({"Amount age  ":amount, "Total Tax is":tax,})
            elif age>60 and age<80 and amount>500001 and amount<1000000:
                tax=amount*Decimal(20/100) 
                return Response({"Amount age  ":amount, "Total Tax is":tax,})
            elif age>60 and age<80 and amount>1000000:
                tax=amount*Decimal(30/100) 
                return Response({"Amount age  ":amount, "Total Tax is":tax,})
            elif age>80 and amount<500000:
                return Response({"You have no tax"})
            elif age>80 and amount>500001 and amount<1000000:
                tax=amount*Decimal(20/100) 
                return Response({"Amount age  ":amount, "Total Tax is":tax,})
            elif age>80 and amount>1000000:
                tax=amount*Decimal(30/100) 
                return Response({"Amount age  ":amount, "Total Tax is":tax,})
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
                
                
                
                
                
                
                
                
                
                
          
                
       
        

# For Individuals below the age of 60 years:

# Income up to ₹2,50,000: No tax=
# Income from ₹2,50,001 to ₹5,00,000: 5%
# Income from ₹5,00,001 to ₹10,00,000: 20%
# Income above ₹10,00,000: 30%

# For Individuals between 60 and 80 years of age (Senior Citizens):

# Income up to ₹3,00,000: No tax
# Income from ₹3,00,001 to ₹5,00,000: 5%
# Income from ₹5,00,001 to ₹10,00,000: 20%
# Income above ₹10,00,000: 30%


# For Individuals above 80 years of age (Very Senior Citizens):

# Income up to ₹5,00,000: No tax
# Income from ₹5,00,001 to ₹10,00,000: 20%
# Income above ₹10,00,000: 30%