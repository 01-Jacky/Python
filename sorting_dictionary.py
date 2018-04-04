my_map = {5:'banana', 2:'apple', 3:'orange', 99:'dragonfruit'}

""" Sort by key (easy)"""
# Get list of tuples sorted by key
sorted_items = sorted(my_map.items())
print(sorted_items)

""" Sort by value (without using ordereddict)"""
# Get list of tuples sorted by value
sorted_items = sorted(my_map.items(), key=lambda x: x[1])
print(sorted_items)

#
keys_sorted_by_value = sorted(my_map, key=my_map.get)
for key in keys_sorted_by_value:
    print('{}:{}'.format(key, my_map[key]))
