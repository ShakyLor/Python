def display_name(name: str)->str:
    """
    Display the String and return the string as well
    Parameters name:str
    return str
    """
    print(name)
    return(name)


display_name('Gonchu')

#def shorter(item): return item['age']

gonchu_family=[
    {'name':'Gonchu','age':50},
    {'name':'Valu','age':30},
    {'name':'Golu','age':10}
]

#gonchu_family.sort(key=shorter)

gonchu_family.sort(key=lambda item:item['age'])
print(gonchu_family)
