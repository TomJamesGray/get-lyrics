import argparse
import sys
import requests
from bs4 import BeautifulSoup


def main():
    # Read in client access token
    with open("TOKEN","r") as f:
        token = f.readline()

    parser = argparse.ArgumentParser(description="Get the lyrics to a song using Genius")
    parser.add_argument("artist", action="store", type=str, help="The song's artist")
    parser.add_argument("song", action="store", type=str, help="The song's name")

    args = parser.parse_args(sys.argv[1:])

    resp = requests.get("https://api.genius.com/search",headers={
        "Authorization":"Bearer {}".format(token)
    }, data={"q":"{} {}".format(args.artist,args.song)})

    if resp.status_code != 200:
        print("HTTP request not ok. Error code {}".format(resp.status_code))

    dat = resp.json()
    url = dat["response"]["hits"][1]["result"]["url"]

    print(scrape(url))


def scrape(url : str):
    resp = requests.get(url)

    if resp.status_code != 200:
        print("HTTP request not ok. Error code {}".format(resp.status_code))

    pg = BeautifulSoup(resp.text, "html.parser")
    lyrics = pg.find('div', class_='lyrics').get_text()

    return lyrics


if __name__ == "__main__":
    main()
