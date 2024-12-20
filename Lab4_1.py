import json

def calculate_sum_of_products(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        total_sum = 0.0
        for item in data:
            if 'score' in item and 'weight' in item:
                total_sum += item['score'] * item['weight']
    return round(total_sum, 3)

json_file_path = 'data.json'
result = calculate_sum_of_products(json_file_path)
print(result)
