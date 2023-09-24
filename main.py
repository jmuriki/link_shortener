import os
import requests
import argparse

from urllib.parse import urlparse
from dotenv import load_dotenv


def is_bitlink(url, token):
	bitly_url = f"https://api-ssl.bitly.com/v4/bitlinks/{url}"
	header = {
		"Authorization": f"Bearer {token}",
	}
	bitly_response = requests.get(bitly_url, headers=header)
	return bitly_response.ok


def shorten_link(link, token):
	bitly_url = "https://api-ssl.bitly.com/v4/bitlinks"
	header = {
		"Authorization": f"Bearer {token}",
	}
	body = {"long_url": link}
	bitly_response = requests.post(bitly_url, headers=header, json=body)
	bitly_response.raise_for_status()
	return bitly_response.json()["id"]


def count_clicks(url, token):
	bitly_url = f"https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary"
	header = {
		"Authorization": f"Bearer {token}",
	}
	bitly_response = requests.get(bitly_url, headers=header)
	bitly_response.raise_for_status()
	return bitly_response.json()["total_clicks"]


def create_parser ():
	parser = argparse.ArgumentParser()
	parser.add_argument ("link")
	return parser


def main():
	load_dotenv()
	token = os.environ["BITLY_TOKEN"]
	link = create_parser().parse_args().link
	parsed_link = urlparse(link)
	url = f"{parsed_link.netloc}{parsed_link.path}"
	try:
		if is_bitlink(url, token):
			sum_of_clicks = count_clicks(url, token)
			print(f"Количество кликов по {url}: ", sum_of_clicks)
		else:
			bitlink = shorten_link(link, token)
			print("Битлинк: ", bitlink)
	except requests.exceptions.HTTPError:
		print(f"'{link}' - введённая ссылка некорректна!")


if __name__ == "__main__":
	main()
