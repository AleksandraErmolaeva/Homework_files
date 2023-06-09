import json
from pprint import pprint

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

def get_shop_list_by_dishes(dishes, person_count):
    shop_list ={}
    for dish in dishes:
        if dish in cook_book.keys():
            res = cook_book.get(dish)
            for el in res:
                if el['ingredient'] not in shop_list.keys():
                    shop_list.update({el['ingredient'] : {'quantity' : int(el['quantity']) * person_count, 'measure' : el['measure'],}})
                else:
                    shop_list[el['ingredient']]['quantity'] = int(shop_list[el['ingredient']]['quantity']) + int(el['quantity']) * person_count
               
                    
    pprint(shop_list)
                

get_shop_list_by_dishes(['Фахитос', 'Омлет'],2)


