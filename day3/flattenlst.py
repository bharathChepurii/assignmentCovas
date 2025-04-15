def flattenlst(lst):
    flat_lst = []
    for i in lst:
        if isinstance(i, list):
            flat_lst.extend(flattenlst(i))
        else:
            flat_lst.append(i)
    return flat_lst
    
input_list = [1, 2, 3, [1, 2, 3, [3, 4], 2]]
print(flattenlst(input_list))
        
