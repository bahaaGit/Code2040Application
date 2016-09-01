#Name: Abdul Aziz Bah
#project: Code2040 API Challenge
#Discribtion: this is step 3 of the challenge
#
import requests
import json


def main():
    api_key = "16a7118361220b69045173b3fbdb9700"
    api_url_for_given_haystack = 'http://challenge.code2040.org/api/haystack'
    api_url_for_validation = 'http://challenge.code2040.org/api/haystack/validate'

    json_data_for_given_data = json.dumps({'token': api_key})
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    results = requests.post(api_url_for_given_haystack, json_data_for_given_data, headers=headers)

    dictionary = json.loads(results.text)

    needle = dictionary["needle"]
    haystack = dictionary["haystack"]

    index_of_haystack_at_needle = 0
    for i in range(0, len(haystack)):
        if haystack[i] == needle:
            index_of_haystack_at_needle = i

    json_data_for_array = json.dumps({'token': api_key, 'needle': index_of_haystack_at_needle})
    results = requests.post(api_url_for_validation, json_data_for_array, headers=headers)

    print(results)

if __name__ == "__main__":
    main()



