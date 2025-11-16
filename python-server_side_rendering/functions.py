#!/usr/bin/python3
import json
import csv
import sqlite3

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

def dbRead(dbName):
    products = []
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    product = cursor.fetchall()
    conn.close()
    for row in product:
        products.append({
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        })
    return products