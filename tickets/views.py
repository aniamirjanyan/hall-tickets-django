from django.http import JsonResponse, HttpResponse
from rest_framework import generics, status
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Ticket
from .serializers import TicketSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class TicketsView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


@api_view(['GET', 'POST'])
def create_ticket(request):
    if request.method == 'POST':
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # ticket = Ticket.objects.filter(seat=serializer.validated_data.get("seat"))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)

    #     # serializer = TicketSerializer(ticket)
    #     # return JSONRenderer.render(serializer.data)
    # except:
    #     return JsonResponse({'message': 'The ticket does not exist'})


@api_view(['GET'])
def check_ticket(request):
    body_ = request.data
    # seat = body_['seat']
    # try:
    serializer = TicketSerializer(data=request.data)
    if serializer.is_valid():
        try:
            ticket = Ticket.objects.get(pk=serializer.validated_data.get('seat'))
        except (Ticket.DoesNotExist, Ticket.MultipleObjectsReturned) as e:
            return JsonResponse({'message': 'The ticket is sold'})
    else:
        return JsonResponse(serializer.errors)
    #     if serializer.data['state']:
    #         return JsonResponse({'message': 'The ticket is sold'})
    #     elif not serializer.data['state']:
    #         return JsonResponse({'message': 'The ticket is available'})
    # except:
    #     return JsonResponse({'message': 'The ticket does not exist'})


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def buy_ticket(request):
    seat = request.data['seat']
    ticket = Ticket.objects.get(pk=seat)
    if ticket.state is True:
        return JsonResponse({'message': 'The ticket is sold'})
    else:
        try:
            ticket.state = True
            ticket.save()
            return JsonResponse({'message': f'You bought the ticket {seat}'})
        except:
            return JsonResponse({'message': f'You failed to buy the ticket {seat}'})


    # ticket = {'state': True}
    # serializer.update()
    # if serializer.is_valid():
    #     return Response(serializer.data)
    # # if not serializer.data['state']:
    # else:
    #     return JsonResponse(serializer.errors)

            # serializer.validated_data['state'] = True
            # serializer.save()
        # return Response(serializer.data)
    # if not ticket.state:
    #     serializer = TicketSerializer(data=ticket)
    #     if serializer.is_valid():
    #         serializer.data['state'] = True
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return JsonResponse(serializer.errors)
    # else:
    #     return JsonResponse({'message': 'The ticket is sold'})

