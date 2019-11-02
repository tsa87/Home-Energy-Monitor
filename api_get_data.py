import requests

# Build Arguments
def get_curr_usage():
    curr_usage = requests.get("https://sfuec-2019.herokuapp.com/usage/current").json()
    return curr_usage

    
