# List that provides units and is critial to these components working so must be placed above functions(like a import eg import pandas)
unit_variables_list = ["kg", "g", "l", "ml","cups","half cups","teaspoon","tablespoon","no unit"]

# ***** fuctions *****

# Displays instructions, returns ""
def instructions():
    
    # prints instructions
    print('''\n\033[0;36m
    **** Instructions *****

    This program will ask you for...
    - The amount of ingredents you plan to use and ask for units for that amount
    - The name of the ingerdents
    - the bulk cost and amount (with units)
    - and how the cost to make

            It will then output an itemised list of of the costs
            with subtotals for the variable and fixed costs.
            
            Finally it will youtube the total costs and the cost 
            per serve to tell you what it is going to cost you to 
            make this dish and how many mouths it can feed

            The data will also be written to a text file which
            has the same name as your dish and the date.

    **** Program launched! ****''')
    print()
    
    return""

# Checks that input is float or int that is more than 0 (custom error message)           
def num_check(question, error, num_type):

    # Loops unit right input is entered
    valid= False
    while not valid:
        
        # Gets input
        try:
            response = num_type(input(question))
            
            if response <= 0:
                print(error)
                
            else:
                return response

        # tells user if they have entered the wrong thing    
        except ValueError:
            print(error)

# Makes sure input is not blank
def not_blank(question,error):
    
    # Loops untill valid answer is given
    while True:
        response = input(question).strip()

        # Loops unit answer is not blank
        if response == "":
            print()
            print("{}. \n \033[38;5;160m Please try again. \n".format(error))
            print()

        else:
            return response

# Function to check if the input matches any of the valid responses
def string_checker(question, num_letters, valid_response):
    # Creates the error message by joining the valid responses
    error = f"\033[38;5;160m Please choose {', '.join(valid_response[:-1])} or {valid_response[-1]} \n"

    
    # Repeat the loop until a valid response is entered
    while True:
        # Get user input, convert to lowercase, and remove leading/trailing whitespace
        response = input(question).lower().strip()
        
        # Checks if the response matches any of the valid responses
        for item in valid_response:
            # Checks if the response matches either the full item or its first 'num_letters' characters
            if response == item[:num_letters] or response == item:
                return item
        
        # If none of the valid responses are matched, print the error message
        print(error)

# metric unit converting funtion(standard unit of g and ml)
def metric_unit_converter(amount,input_unit,standard_unit):

    # Dictionary that stores units and their conversion factors
    conversion_factors ={
        "kg" :1000,  
        "g":1,
        "ml":1,
        "l":1000,
        "cups":240 ,
        "half cups": 170,
        "teaspoon":4.2 ,
        "tablespoon":21.25,
        "no unit":1
    }

    # Converts base amount to standard unit g and ml
    base_amount= amount*conversion_factors[input_unit]
    
    # Gets converted amount
    converted_amount = base_amount / conversion_factors[standard_unit]
    
    # Returns converted amount
    return converted_amount

# Gets amount unit and ingreadeant name
def ingredients_and_amounts():
    # Sets up dictionaries and lists
    amount_1_list = []
    unit_1_list = []

    # Loops to get component, quantity, and price  
    print()
    
    # Gets amount
    print()
    amount = num_check("\033[0;37;40mHow much of this ingredient do you have? ", "\033[38;5;160m Please enter a number greater than zero. \n", float)
    print()

    # Loops to make sure user gets the right unit
    while True:
        # Asks user for unit
        unit_1 = string_checker("\033[0;37;40mWhat unit are you using for this amount (enter no unit if you have no units)? ", 1, unit_variables_list)
        
        # If the unit is valid
        if unit_1 in unit_variables_list:
            # Sets the standard unit based on the input
            break
        
        # If the unit is invalid
        else:
            print("\033[38;5;160mPlease enter the units {}. \n". format(unit_variables_list))
            continue

    # Sets the standard unit based on the input
    if unit_1 in["ml","l","kg","g"]:
        standard_unit = "ml" if unit_1 in ["ml", "l"] else "g"
    
    else:
        standard_unit = unit_1
    
    # Converts amounts based on the unit    
    converted_unit_1=metric_unit_converter(amount,unit_1,standard_unit)
            
    # Add item, quantity, and price to lists
    amount_1_list.append(converted_unit_1)
    unit_1_list.append(standard_unit)

    # Returns inputs
    return amount_1_list, unit_1_list 

# Gets the cost and amount that you get for this cost
def amounts_and_costs():

    # Sets up lists
    price_func_list = []
    amount_func_2_list = []
    unit_func_2_list = []
    
    
    # Loops to get component, quantity, and price
    print()
    # Gets bulk price
    price_1 = num_check("\033[0;37;40mWhat is the bulk price of this ingredient? $ ", "\033[38;5;160m Please enter a number greater than zero. \n", float)
    print()
    
    # Gets the amount
    amount = num_check("\033[0;37;40mHow much of this ingredient do you get for this bulk price? ", "\033[38;5;160m Please enter a number greater than zero. \n", float)
    print()

    # Loops to make sure user gets the right unit
    while True:
        unit_1 = string_checker("\033[0;37;40mWhat unit are you using for this amount (enter no unit if you have no units)? ", 1, unit_variables_list)
        if unit_1 in unit_variables_list:
            # Sets the standard unit based on the input
            break
        else:
            print("\033[38;5;160mPlease enter the units {}. \n". format(unit_variables_list))
            continue

    # Sets the standard unit based on the input
    if unit_1 in["ml","l","kg","g"]:
        standard_unit = "ml" if unit_1 in ["ml", "l"] else "g"
    
    else:
        standard_unit = unit_1
    

    # Convert unit and amount into standard unit and amount
    converted_unit_1 = metric_unit_converter(amount, unit_1, standard_unit)

    # Add item, quantity, and price to lists
    price_func_list.append(round(price_1, 2))
    amount_func_2_list.append(converted_unit_1)
    unit_func_2_list.append(standard_unit)
    
    # Returns inputs
    return price_func_list, amount_func_2_list, unit_func_2_list
