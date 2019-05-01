import argparse
import sys
import requests

def main():
    # Read in client access token
    with open("TOKEN","r") as f:
        token = f.readline()

    parser = argparse.ArgumentParser(description="Get the lyrics to a song using Genius")
    parser.add_argument("artist",action="store",type=str,help="The song's artist")
    parser.add_argument("song", action="store", type=str, help="The song's name")

    args = parser.parse_args(sys.argv[1:])

    print(args.song)

    resp = requests.get("https://api.genius.com/search",headers={
        "Authorization":"Bearer {}".format(token)
    },data={"q":"{} {}".format(args.artist,args.song)})
    dat = resp.json()
    print(dat["response"]["hits"][1]["result"]["url"])




if __name__ == "__main__":
    main()