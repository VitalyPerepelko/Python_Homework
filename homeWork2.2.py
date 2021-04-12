#Vitaly Perepelko
#home_work2_2

first_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
           'была', '+5', 'градусов']
second_list = []
for var, element in enumerate(first_list):
    if element.isdigit():
        second_list.extend(['"', f'{int(element):02}', '"'])
    elif (element.startswith('+') or element.startswith('-')) and element[1:].isdigit():
        second_list.extend(['"', f'{element[0]}{int(element):02}', '"']) 
    else:
        second_list.append(element)

new_info = ' '.join(second_list)   
print(new_info)

symbol_idxs = []
for var, letter in enumerate(new_info):
    if letter == '"':
        symbol_idxs.append(var)

# some logic to find delete indexes
for var in range(len(symbol_idxs)):
    if var % 2 == 0:
        symbol_idxs[var] = symbol_idxs[var] + 1
    else:
        symbol_idxs[var] = symbol_idxs[var] - 1

# delete indexes from original string
for del_var in reversed(symbol_idxs):
    new_info = new_info[:del_var] + new_info[del_var+1:]