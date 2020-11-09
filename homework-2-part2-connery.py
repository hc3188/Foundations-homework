#Harrison Connery
#11/1/2020
#Homework 2, part 2



countries =["France", "United States", "England", "Bolivia", "Spain", "Germany", "Japan"]
for country in countries:
  print(country)  
countries= sorted(countries)
print(countries)
print(countries[0])
print(countries[6])
countries.remove('Bolivia')
print(countries)
for country in countries:
  print(country.upper())


tree = {'name': 'Old_Tjikko', 'species': 'Norway_Spruce', 'age': '9562', 'location_name': 'Norway', 'latitude': 61.583333, 'longitude': 12.666667}
print(tree['name'], " is a", tree['age'], " years old tree that is in",tree['location_name'])
print("The tree ", tree['name'], " in", tree['location_name'],  "is North of NYC")
person_age= int(input("How old are you?"))
if person_age < 9562:
   tree_age = 9562-person_age  
   print("You are ", tree_age, " years younger than", tree['name'])


cities = {'name': 'Moscow', 'latitude':55.7558, 'longitude': 37.6173},{'name': 'Tehran', 'latitude': 35.6892, 'longitude': 51.3890}, {'name':'FalklandIslands', 'latitude': 51.7693, 'longitude': 59.5236},{'name': 'Seoul', 'latitude': 37.5665, 'longitude': 126.9780},{'name':'Santiago', 'latitude':33.4489, 'longitude':70.6693}
for city in cities:
    if city['latitude'] > 0:
      print(city['name'] + ' is above the equator')  
    else:
      print(city['name'] + ' is below the equator')  
for city in cities:
    if city['latitude'] > tree['latitude']:
      print(f"{city['name']} is North of {tree['name']}")
    else:
      print(f"{city['name']} is South of {tree['name']}")   