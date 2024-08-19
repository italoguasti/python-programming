# Positional args

def user_info(name, age, city):
    '''This function prints name, age, and city
    from an argument provided to the function.'''

    print("{} is {} years old, from {}".format(name, age, city))

user_info("Italo", 26, "Ouro Preto City")


# Positional args + default

def user_info_named(name, age=26, city="OP City"):
    '''This function prints name, age, and city
    from an argument provided to the function.'''

    print("{} is {} years old, from {}".format(name, age, city))

user_info("Italo", 26, "Ouro Preto City")

# * args e **kwargs

def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. Her email is {}.".format(fname, lname, company, email))