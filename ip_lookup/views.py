from rest_framework.response import Response
from rest_framework.decorators import api_view
from .ip import IP
from .serializers import IPSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status


@api_view(("GET",))
def full_ip_location_data_endpoint(request, ip):
    """
    returns a json file containing the full locational details of
    the ip address
    Arguments
    ---------
    ip - the ip address to be queried
    """
    try:
        ip_address = IP(ip)
    except ValueError as err:
        print(f"404 ERROR: {err}")
        return Response(status=status.HTTP_404_NOT_FOUND)
    except ObjectDoesNotExist as err:
        print(f"404 ERROR: {err}")
        return Response(status=status.HTTP_404_NOT_FOUND)

    serialized_ip = IPSerializer(ip_address)
    return Response(serialized_ip.data, status=status.HTTP_200_OK)


@api_view(("GET",))
def unique_ip_location_data_endpoint(request, ip, key):
    """
    returns unique detail per key for the ip address requested
    Arguments
    ----------
    ip - the ipaddress to be queried from the database
    key - the unique data to be returned
    """
    try:
        ip_address = IP(ip)
    except ValueError as err:
        print(f"404 ERROR: {err}")
        return Response(status=status.HTTP_404_NOT_FOUND)
    except ObjectDoesNotExist:
        print(f"404 ERROR: {err}")
        return Response(status=status.HTTP_404_NOT_FOUND)

    serialized_ip = IPSerializer(ip_address)
    try:
        res = serialized_ip.data[key]
    except KeyError as err:
        print(f"404 ERROR: {err}")
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(res, status=status.HTTP_200_OK)
