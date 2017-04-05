#!/usr/bin/python

from suds.client import Client

def Long_lat(a):

    url = 'http://www.webservicex.com/airport.asmx?wsdl'
    client = Client(url, timeout=600)
    results = client.service.getAirportInformationByCityOrAirportName(a)

    return results


a = "paris"

results = Long_lat(a)
print results