# task_6

items = [
    (1, {'name': input('Name: '), 'price': int(input('Price: ')),
         'quantity': int(input('Quantity: ')), 'measure': input('Measure: ')}),
    (2, {'name': int(input('Name: ')), 'price': int(input('Price: ')),
         'quantity': int(input('Quantity: ')), 'measure': input('Measure: ')}),
    (1, {'name': input('Name: '), 'price': int(input('Price: ')),
         'quantity': int(input('Quantity: ')), 'measure': input('Measure: ')})
]
sorted_dict = {'name': [], 'price': [], 'quantity': [], 'measure': []}
i = 0
while i < len(items):
    sorted_dict.get('name').append(items[i][1].get('name'))
    sorted_dict.get('price').append(items[i][1].get('price'))
    sorted_dict.get('quantity').append(items[i][1].get('quantity'))
    sorted_dict.get('measure').append(items[i][1].get('measure'))
    i += 1
print(sorted_dict)
