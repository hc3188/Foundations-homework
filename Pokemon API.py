#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#What is the URL of the documentation?

#https://pokeapi.co/docs/v2#pokemon

#What Pokemon has ID 55?

url ="https://pokeapi.co/api/v2/pokemon/55"

import requests

response = requests.get(url, allow_redirects=True)
pokeID = response.json()

print(pokeID['name'])

#golduck

#How tall is golduck?

print(pokeID['height'])

#17 decimeters

#How many version of Pokemon games have been released?

url2= "https://pokeapi.co/api/v2/version/"

import requests

response = requests.get(url2, allow_redirects=True)
version = response.json()


print(version.keys())
print(version['count'])

#There have been 34 versions

#Name all the electric type pokemon

url3= "https://pokeapi.co/api/v2/type/electric"

import requests

response = requests.get(url3, allow_redirects=True)
type = response.json()    

print(type.keys())
print(type['pokemon'])

#What are electric-type Pokemon called in Korean?

url3= "https://pokeapi.co/api/v2/type/electric"

import requests

response = requests.get(url3, allow_redirects=True)
type = response.json()    

print(type.keys())

pokemon_names_multilingual=type['names']



print(pokemon_names_multilingual)

print(pokemon_names_multilingual[1])

korean = [electric_names['name'] for electric_names in pokemon_names_multilingual]
print(korean[1])

#Can use for loop to get keys for dictionaries in lists. 

#Who has a higher speed stat, Eevee or Pikachu?

url4= "https://pokeapi.co/api/v2/pokemon/pikachu"
    
import requests

response = requests.get(url4, allow_redirects=True)
pokemon_speed = response.json()  

print(pokemon_speed.keys())
print(pokemon_speed['stats'])


url5= "https://pokeapi.co/api/v2/pokemon/eevee"
    
import requests

response = requests.get(url5, allow_redirects=True)
evee_speed = response.json()  

print(evee_speed.keys())
print(evee_speed['stats'])


#Pikachu has a higher speed stat

