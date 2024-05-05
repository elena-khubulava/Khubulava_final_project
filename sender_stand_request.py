import requests

import configuration
import data


def create_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=data.body_create)

def get_track():
    response = create_order()
    track = response.json()["track"]
    return track

def get_order_by_track(track):
    params = {"t": "track"}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH, params=params)

