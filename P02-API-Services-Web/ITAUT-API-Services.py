#!/usr/bin/env python3

import os
import requests
import json


def feeds_upload(dirs):

    feeds_list = []
    files = os.listdir(dirs)

    for file in files:

        if file.lower().endswith('.txt'):

            print(file)
            print(type(files))
            print("File {} loading!".format(file))

            with open(file, "r") as infile:
                try:
                    feeds = infile.readlines()
                    feedbacks = dict(title=feeds[0],
                                     name=feeds[1],
                                     date=feeds[2],
                                     feedback=feeds[3])

                    feeds_list.append(feedbacks)
                    print(feeds_list)
                    print("List created!")

                except OSError as e:
                    print(e)

    return feeds_list


def feeds_send(list_feeds, url):

    url = url
    feeds_data = list_feeds

    try:
        r = requests.post(url, json=feeds_data)

        if r.status_code == r.ok:
            print("Sent with success {}!".format(r.status_code))

        else:
            print("Oh no! Something went wrong {}.".format(r.raise_for_status))

    except OSError as e:
        print(e)


if __name__ == '__main__':
    dirs = "data/feedback/"
    url = "http://35.238.170.53/feedback/post"
    feeds = feeds_upload(dirs)
    feeds_send(feeds, url)

# Incluir um while para enviar os feeds para o service
