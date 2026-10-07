import mymodule as my

keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

resualt = my.bind_lists(keys,values)


print(resualt)

print("test")

values2 = ["Alice", 25]


resualt2 = my.bind_lists(keys,values2)


print(resualt2)

