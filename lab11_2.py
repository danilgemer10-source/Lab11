import json

with open('d:/дз/ВКН/lab11 full/disk.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    
best_disk = data[0]
data[0]['price']
data[0]['capacity']
data[0]['price'] / data[0]['capacity']
best_price = best_disk['price'] / best_disk['capacity']

worst_disk = data[0]
data[0]['price']
data[0]['capacity']
data[0]['price'] / data[0]['capacity']
worst_price = worst_disk['price'] / worst_disk['capacity']


    
for disk in data:
    brand = disk['brand']
    capacity = disk['capacity']
    price = disk['price']
    
    price_per_gb = price / capacity

    print(f"Brand: {brand}, Capacity: {capacity}GB, Price: ${price}, Price per GB: ${price_per_gb:.2f}")
    
    if price_per_gb < best_price:
        best_disk = disk
        best_price = price_per_gb
        
    elif price_per_gb > worst_price:
        worst_disk = disk
        worst_price = price_per_gb
    
print('Найвигідніший диск:', best_disk['brand'], best_disk['capacity'], best_disk['price'], best_price)
print('Найменш вигідний диск:', worst_disk['brand'], worst_disk['capacity'], worst_disk['price'], worst_price)
