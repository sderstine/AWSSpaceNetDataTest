import requests
from requests.exceptions import HTTPError
import string

def get_response_dict():
    URLS = ["https://maxar-opendata.s3.amazonaws.com/events/catalog.json"]

    for url in URLS:
        try:
            response = requests.get(url, verify=False)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        else:
            print("Success!")
            
            response_dict = response.json()
            print(response_dict)
            if response_dict is None:
                print("Error: Failed to retrieve response data from API.")
            else:
                return(response_dict)
            
            
def get_linkresponse_dict(extended_link):
    
    
        try:
            response = requests.get(extended_link, verify=False)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        else:
            print("Success!")
            
            extended_response_dict = response.json()
            if response.json() is None:
                print("Error: Failed to retrieve response data from API.")
            else:
                print("FUN!!!")
                return(extended_response_dict)