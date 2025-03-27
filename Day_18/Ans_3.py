# Handle KeyError in a dictionary.

My_dict = {"name": "Raj",
           "location": "Banglore"}
try:
    print(My_dict["name"],My_dict["location"],My_dict["country"])
except KeyError:
    print(" the key you enterd does not exist")