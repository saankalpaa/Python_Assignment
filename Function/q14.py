sort = lambda dic: sorted(dic, key=lambda x: x['color'])
list = [{'make':'Apple', 'model':11, 'color':'Matte Black'}, {'make':'Mi Max', 'model':2, 'color':'Gold'}, {'make':'Samsung', 'model': 9, 'color':'Blue'}]

print(sort(list))