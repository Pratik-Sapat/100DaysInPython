def format_name(f_name, l_name):
    """Takes first and last name and format it in string
     - Doc string example."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."

    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    #end of function
    return f"{formatted_f_name} {formatted_l_name}" 
   


f_string = format_name("PraTik", "SaPAT") 
print(f_string)

#you can ask for input also.
f_string = format_name(input("First name : "), input("Last name : "))
print(f_string)

#title function can make every first word capital in  sentence.
