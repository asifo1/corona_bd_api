from flask import Flask
from flask import jsonify
import requests
from lxml import html, etree

app = Flask(__name__)


@app.route('/')
def api():
    try:
        response = requests.get('http://corona.gov.bd')
        parser = etree.HTMLParser(encoding='utf-8')
        tree = html.fromstring(response.content, parser=parser)

        new_infected = tree.xpath(
            '/html/body/section[4]/div/div[1]/div[1]/div/div[1]/div[1]/h3/b')[0].text

        total_infected = tree.xpath(
            '/html/body/section[4]/div/div[1]/div[1]/div/div[1]/div[2]/h3/b')[0].text

        new_death = tree.xpath(
            '/html/body/section[4]/div/div[1]/div[2]/div/div[1]/div[1]/h1/b')[0].text
        total_death = tree.xpath(
            '/html/body/section[4]/div/div[1]/div[2]/div/div[1]/div[2]/h1/b')[0].text

        new_cured = tree.xpath(
            '/html/body/section[4]/div/div[1]/div[3]/div/div[1]/div[1]/h3/b')[0].text
        total_cured = tree.xpath(
            '/html/body/section[4]/div/div[1]/div[3]/div/div[1]/div[2]/h3/b')[0].text

        new_test = tree.xpath(
            '/html/body/section[4]/div/div[1]/div[4]/div/div[1]/div[1]/h3/b')[0].text
        total_test = tree.xpath(
            '/html/body/section[4]/div/div[1]/div[4]/div/div[1]/div[2]/h3/b')[0].text

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
        return jsonify(data), 200
    except:
        data = {
            "error": "Internal Server Error"
        }
        return jsonify(data), 500
