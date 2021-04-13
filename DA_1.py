import requests
import os
import json




def auth():
#enter auth token here
    return ""

def create_url():
    # Replace with user ID below(here Sachin Tendulkar)
    user_id = 135421739
    return "https://api.twitter.com/2/users/{}/followers".format(user_id)


def get_params():
    return {"user.fields": "created_at"}


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers, params):
    response = requests.request("GET", url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    bearer_token = auth()
    url = create_url()
    headers = create_headers(bearer_token)
    params = get_params()
    json_response = connect_to_endpoint(url, headers, params)
    for i in range(100):
        print(json_response['data'][i])
        # print("**************")
        # print("Name: ",i['name'])
        # print("ID: ",i['id'])



if __name__ == "__main__":
    main()