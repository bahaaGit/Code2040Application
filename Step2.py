#Name: Abdul Aziz Bah
#project: Code2040 API Challenge
#Discribtion: this is step 2 of the challenge
#
import requests
import json


def main():

    api_key = "16a7118361220b69045173b3fbdb9700"

    api_url_for_given_string = 'http://challenge.code2040.org/api/reverse'
    api_url_for_reversed_string = 'http://challenge.code2040.org/api/reverse/validate'

    json_data_for_given_data = json.dumps({'token': api_key})
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    results = requests.post(api_url_for_given_string,json_data_for_given_data, headers=headers)

    reg_string = results.text
    print(results.text)
    reversed_string = "".join(reversed(reg_string))

    reversed_string_for_data = json.dumps({'token': api_key, 'string': reversed_string})
    results = requests.post(api_url_for_reversed_string, reversed_string_for_data, headers=headers)

    print (results)
if __name__ == "__main__":
    main()