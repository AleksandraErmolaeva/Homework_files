import json

with open ('c:/Users/alexa/Desktop/HomeWork/hw_files/recipes.txt', encoding = 'utf-8') as f:
    cook_book = {}
    for dish_name in f:
        ingredients_count = int(f.readline())
        ingredients_list = []
        for i in range(ingredients_count):
            ingredient, quantity, measure = f.readline().strip().split(' | ')
            ingredients_list.append({
                'ingredient': ingredient,
                'quantity' : quantity,
                'measure' : measure
            })
        f.readline()
        cook_book[dish_name.strip()] = ingredients_list
res = json.dumps(cook_book, indent=2, ensure_ascii = False)
print(res)
