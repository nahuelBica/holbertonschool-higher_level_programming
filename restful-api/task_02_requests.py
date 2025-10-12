#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts(
    fetch_URL="https://jsonplaceholder.typicode.com/posts",
):
    response = requests.get(fetch_URL)
    print(f"Status Code: {response.status_code}")

    if response.ok:
        dic_resp = response.json()

        for dic in dic_resp:
            print(dic["title"])


def fetch_and_save_posts(
    fetch_URL="https://jsonplaceholder.typicode.com/posts",
):
    response = requests.get(fetch_URL)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        dic_response = response.json()
        fieldnames = ["id", "title", "body"]
        filename = "posts.csv"

        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file, fieldnames=fieldnames, extrasaction="ignore"
            )
            writer.writeheader()

            for dic in dic_response:
                writer.writerow(dic)
