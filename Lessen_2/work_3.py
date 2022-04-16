import yaml

DATA = {'items': ['computer', 'printer', 'keyboard', 'mouse'],
           'items_quantity': 4,
           'items_price': {'computer': '200\u20ac-1000\u20ac',
                           'printer': '100\u20ac-300\u20ac',
                           'keyboard': '5\u20ac-50\u20ac',
                           'mouse': '4\u20ac-7\u20ac'}
           }

with open('file.yaml', 'w', encoding='utf-8') as f_in:
    yaml.dump(DATA, f_in, default_flow_style=False, allow_unicode=True)

with open("file.yaml", 'r', encoding='utf-8') as f_out:
    DATA2 = yaml.load(f_out, Loader=yaml.SafeLoader)

print(DATA == DATA2)