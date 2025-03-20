#catch a KeyError
try:
    my_dict= {"key1":"value1", "key2":"value2"}
    value = my_dict["key3"]
except KeyError:
    print("KeyError : key does not exist")
finally:
    print(" program is over ")