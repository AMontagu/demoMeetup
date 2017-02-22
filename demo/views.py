import time
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from demo.term import SerialCom

def home(request):
	return render(request, 'index.html')

@api_view(['GET'])
def turnOn(request):
	print("turnOn")
	#print(request.data)
	#command = request.POST.get("command", "error")
	serialCom = SerialCom(1, "serialThread")

	serialCom.daemon = True
	serialCom.start()

	time.sleep(3)

	serialCom.write(bytes("o", "utf-8"))

	time.sleep(1)

	serialCom.closeSerial()

	return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def turnOff(request):
	print("turnOff")
	#print(request.data)
	#command = request.POST.get("command", "error")
	serialCom = SerialCom(1, "serialThread")

	serialCom.daemon = True
	serialCom.start()

	time.sleep(3)

	serialCom.write(bytes("f", "utf-8"))

	time.sleep(1)

	serialCom.closeSerial()

	return Response(status=status.HTTP_200_OK)
