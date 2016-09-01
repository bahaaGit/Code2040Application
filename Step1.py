#Name: Abdul Aziz Bah
#project: Code2040 API Challenge
#Discribtion: this is step 1 of the challenge
#
import requests
import json


def main():

    github = "https://github.com/bahaaGit/Code2040Application"
    api_key = "16a7118361220b69045173b3fbdb9700"
    api_url = "http://challenge.code2040.org/api/register"
    payload = json.dumps({'token': api_key, 'github': github})
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    results = requests.post(api_url, payload, headers=headers)
    print(results.text)

if __name__ == "__main__":
    main()
