import os
import json
import requests

from dotenv import load_dotenv


def shorten_link(url, bitly_token):
	bitly_url = "https://api-ssl.bitly.com/v4/bitlinks"
	headers = {
		"Authorization": f"Bearer {bitly_token}",
	}
	json_string = {
		"long_url": f"{url}"
	}
	short_link = requests.post(bitly_url, headers=headers, json=json_string)
	short_link.raise_for_status
	return json.loads(short_link.text)["id"]


def count_clicks(bitlink, bitly_token):
	bitly_url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary"
	header = {
		"Authorization": f"Bearer {bitly_token}",
	}
	response = requests.get(bitly_url, headers=header)
	response.raise_for_status
	return response.json()["total_clicks"]


def main():
	load_dotenv()
	url = input("Введите ссылку 'http://*.*' или 'https://*.*' : ")
	bitly_token = os.environ["BITLY_TOKEN"]

	try:
		bitlink = shorten_link(url, bitly_token)
		print("Битлинк: ", bitlink)
	except:
		print("Введеная ссылка некорректна.")

	try:
		print(count_clicks(bitlink, bitly_token))
	except:
		print("Введеная ссылка некорректна")


if __name__ == "__main__":
	main()
