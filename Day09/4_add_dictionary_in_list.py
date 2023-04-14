travel_log = [
    {
        "country" : "France",
        "visits" : 12, 
        "cities" : ["paris", "Lille", "Dijon"],  
    },
    {
        "country" :"Germany", 
        "visits" : 5,
        "cities" : ["Berlin", "Hamburg", "Stuttgart"],    
    },
]
#do not change avobe code.

#write function fto add new dictionary in list.

def add_new_country(country_visited,times_visited,cities_visited):
    #create another dictionry with same key's and then append it to original.
    new_country = {} 
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited

    #to store new dictionary in travel_log use .append func.
    travel_log.append(new_country) 
#

#do not change below code.
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)