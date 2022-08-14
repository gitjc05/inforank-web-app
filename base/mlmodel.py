import requests


def ranker(context):

    url = "https://powerful-chamber-06502.herokuapp.com"

    r = requests.post(url=url, data=context)
    return r.json()



