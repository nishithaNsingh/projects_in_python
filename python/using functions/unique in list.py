def unq(list_inp):
    set_res = set(list_inp) 
    print("The unique elements of the input list using set():\n") 
    list_res = (list(set_res))
 
    for item in list_res: 
        print(item)

list_inp=[10,20,30,40,10,20]
print(unq(list_inp))
