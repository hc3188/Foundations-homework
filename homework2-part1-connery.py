#Harrison Connery
#11/1/2020
#Homework 2 part 1 


list = [22, 90, -10, 3, 22, 48]
print(len(list))
print(list[3])
print(list[1] + list[3])
list1=sorted(list)
print(list1[-2])
print(list[5])
mean= sum(list)/2
print(mean)
median=22
if mean > median:
  print("The mean is greater thant the median.")
else:
  print("The median is greater than the mean.")

movie={'name': 'AustinPowers', 'year':'1997', 'director': 'Jay Roach'}

movie['budget']= 16500000
movie['revenue']= 67000000

if movie['budget'] > movie['revenue']:
  print("That was a bad investment.")
elif movie['revenue'] >= movie['budget']*5:
  print("That was a great investment.")  
else:
  print("That was an ok investment.")  


nyc={'manhattan_pop':1600000, 'brooklyn_pop':2600000, 'bronx_pop': 1400000, 'queens_pop': 2300000, 'staten_island_pop': 470000}

print(nyc['brooklyn_pop'])
print(nyc['manhattan_pop'] + nyc['brooklyn_pop'] +nyc['bronx_pop'] + nyc['queens_pop'] + nyc['staten_island_pop']) 



