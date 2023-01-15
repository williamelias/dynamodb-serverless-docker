import json
from copy import deepcopy
import use_cases

def manage_cats(event, context):
    cats = json.loads(event.get('Body',[]))
    print("Gatos a serem salvos:",cats)
    for cat in cats:
        save_cat = use_cases.SaveCat(data=cat)
        save_cat.exec()
  
    return {
        "status_code":200,
        "message": "sucesss"
    }


if __name__ == '__main__':
    cats = {}
    with open('mock/cats.json', 'rb') as file:
        mock = json.load(file)
    
    formatted_cats = json.dumps(mock.get('Body',[]))

    manage_cats(
        event={
            'Body':formatted_cats
        },
        context={}
    )

    print("Itens processados...")
    while True:
        pass
