import json
import csv


def read(file_name):
     with open(file_name, "r") as file:
        data = json.load(file)
        values = data.get("items", [])
        return values

def jsonRead(file_name):
    with open(file_name) as f:
        products = json.load(f)
    return products
    
def csvRead(file_name):
    products = []
    with open(file_name, newline='') as csvF:
        reader = csv.DictReader(csvF)
        for row in reader:
            products.append({
				"id": int(row['id']),
				"name": row['name'],
				"category": row['category'],
				"price": float(row['price'])
            })
    return products
