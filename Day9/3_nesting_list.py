#nesting

capitals = {
    "farnce" : "paris",
    "Germany" : "Berlin",
}

#nesting list in dictionary.
travel_log = {
    "France" : ["paris", "Lille", "Dijon"],
    "Germany" : ["Berlin", "Hamburg", "Stuttgart"],
}


#nesting dictionary in a dictionary.
travel_log = {
    "France" : {"cities_visited" : ["paris", "Lille", "Dijon"], "total_visits" : 12},
    "Germany" : ["Berlin", "Hamburg", "Stuttgart"],
}


#nesting dictionary inside list.
travel_log = [
    {
        "country" : "France", 
        "cities_visited" : ["paris", "Lille", "Dijon"], "total_visits" : 12
    },
    {
        "country" :"Germany", 
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits" : 5
    }
]
