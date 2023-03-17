marvel_heros = {
    "Spiderman": 80,
    "Ironman": 90,
    "Thor": 95
}

dc_heros = {
    "batman": 99,
    "Flash": 70,
    "Aquaman": 85
}

# print(len(dc_heros))
# print(dc_heros.clear())
# print(dc_heros)

dc_heros.update(marvel_heros)

# print(dc_heros)


myTags = ("Name", "Last_Name", "Age", "Phone")

myOne = dict.fromkeys(myTags)

print("My Dictionary is: %s" %str(myOne))