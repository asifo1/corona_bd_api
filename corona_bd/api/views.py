from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from rest_framework.renderers import (
    JSONRenderer,
    BrowsableAPIRenderer,
)


from lxml import html


class Home(APIView):
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer)

    def get(self, request):
        # try:
        if True:
            response = requests.get('http://corona.gov.bd')
            tree = html.fromstring(response.content)

            new_infected = tree.xpath(
                '/html/body/section[3]/div/div[1]/div[1]/div/div[1]/div[1]/h3/b')[0].text
                
            total_infected = tree.xpath(
                '/html/body/section[3]/div/div[1]/div[1]/div/div[1]/div[2]/h3/b')[0].text

            new_death = tree.xpath(
                '/html/body/section[3]/div/div[1]/div[2]/div/div[1]/div[1]/h1/b')[0].text
            total_death = tree.xpath(
                '/html/body/section[3]/div/div[1]/div[2]/div/div[1]/div[2]/h1/b')[0].text

            new_cured = tree.xpath(
                '/html/body/section[3]/div/div[1]/div[3]/div/div[1]/div[1]/h3/b')[0].text
            total_cured = tree.xpath(
                '/html/body/section[3]/div/div[1]/div[3]/div/div[1]/div[2]/h3/b')[0].text

            new_test = tree.xpath(
                '/html/body/section[3]/div/div[1]/div[4]/div/div[1]/div[1]/h3/b')[0].text
            total_test = tree.xpath(
                '/html/body/section[3]/div/div[1]/div[4]/div/div[1]/div[2]/h3/b')[0].text

            data = {
                'source': 'https://corona.gov.bd/',
                'data': {
                    'new_infected': new_infected,
                    'total_infected': total_infected,
                    'new_cured': new_cured,
                    'total_cured': total_cured,
                    'new_death': new_death,
                    'total_death': total_death,
                    'new_test': new_test,
                    'total_test': total_test}
            }

        # except:
        #     return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(data, status=status.HTTP_200_OK)

