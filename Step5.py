#Name: Abdul Aziz Bah
#project: Code2040 API Challenge
#Discribtion: this is step 5 of the challenge
#

import iso8601
import requests
import json
from datetime import timedelta


def main():

    api_key = "16a7118361220b69045173b3fbdb9700"
    api_url_for_date = 'http://challenge.code2040.org/api/dating'
    api_url_for_date_validation = 'http://challenge.code2040.org/api/dating/validate'

    json_data_for_date = json.dumps({'token': api_key})
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    results = requests.post(api_url_for_date, json_data_for_date, headers=headers)

    dictionary = json.loads(results.text)

    date_stamp = dictionary["datestamp"]
    interval = dictionary["interval"]

    date = iso8601.parse_date(date_stamp) + timedelta(seconds=int(interval))
    new_date = date.isoformat()

    number_of_sec = int(interval)
    new_time = iso8601.parse_date(date_stamp) + timedelta(seconds=number_of_sec)
    new_time_without_timezone = new_time.replace(tzinfo=None)
    new_date_n_time = new_time_without_timezone.strftime('%Y-%m-%dT%H:%M:%SZ')

    json_data_for_new_date = json.dumps({'token': api_key, 'datestamp': new_date_n_time})
    results = requests.post(api_url_for_date_validation, json_data_for_new_date, headers=headers)

    print(results)


if __name__ == "__main__":
    main()
