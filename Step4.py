#Name: Abdul Aziz Bah
#project: Code2040 API Challenge
#Discribtion: this is step 4 of the challenge
#
import requests
import json


def main():

    api_key = "16a7118361220b69045173b3fbdb9700"
    api_url_for_prefix = 'http://challenge.code2040.org/api/prefix'
    api_url_for_prefix_validation = 'http://challenge.code2040.org/api/prefix/validate'

    json_data_for_prefix = json.dumps({'token': api_key})
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    results = requests.post(api_url_for_prefix, json_data_for_prefix, headers=headers)

    dictionary = json.loads(results.text)

    prefix = dictionary["prefix"]
    array = dictionary["array"]

    new_string_array = [array_str for array_str in array if not array_str.startswith(prefix)]

    json_data_for_array = json.dumps({'token': api_key, 'array': new_string_array})
    results = requests.post(api_url_for_prefix_validation, json_data_for_array, headers=headers)

    print(results)

if __name__ == "__main__":
    main()
