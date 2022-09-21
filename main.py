import os
import requests
import argparse

from urllib.parse import urlparse
from dotenv import load_dotenv


def is_bitlink(url, header):
	bitly_url = f'https://api-ssl.bitly.com/v4/bitlinks/{url}'
	bitly_response = requests.get(bitly_url, headers=header)
	return bitly_response.ok


def shorten_link(link, header):
	bitly_url = 'https://api-ssl.bitly.com/v4/bitlinks'
	body = {'long_url': link}
	bitly_response = requests.post(bitly_url, headers=header, json=body)
	bitly_response.raise_for_status()
	return bitly_response.json()['id']


def count_clicks(url, header):
	bitly_url = f'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary'
	bitly_response = requests.get(bitly_url, headers=header)
	bitly_response.raise_for_status()
	return bitly_response.json()['total_clicks']


def create_parser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('link')
    return parser


def main():
	parser = create_parser()
	linkspace = parser.parse_args()
	parsed_link = urlparse(linkspace.link)
	url = f'{parsed_link.netloc}{parsed_link.path}'
	load_dotenv()
	token = os.environ['BITLY_TOKEN']
	header = {
		'Authorization': f'Bearer {token}',
	}
	try:
		if is_bitlink(url, header):
			sum_of_clicks = count_clicks(url, header)
			print(f'Количество кликов по {url}: ', sum_of_clicks)
		else:
			bitlink = shorten_link(linkspace.link, header)
			print('Битлинк: ', bitlink)
	except requests.exceptions.HTTPError:
		print(f'"{linkspace.link}" - введённая ссылка некорректна!')


if __name__ == '__main__':
	main()
