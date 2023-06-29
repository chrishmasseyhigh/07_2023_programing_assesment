# sets up unit list
unit_variables_list = ["kg", "g", "l", "ml","cups","half cups","teaspoon","tablespoon"]

# dictionary to store unitcs and their conversion factor
conversion_factors ={
    "kg" :1000,  
    "g":1,
    "ml":1,
    "l":1000,
    "cups":240 ,
    "half cups": 170,
    "teaspoon":4.2 ,
    "tablespoon":21.25
}

# Displays instructions, returns ""
def instructions():
    
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

# checks that input is float or int that is more than 0 (custom error message)           
def num_check(question, error, num_type):

    valid= False
    while not valid:
        
        try:
            response = num_type(input(question))
            
            if response <= 0:
                print(error)
                
            else:
                return response
            
        except ValueError:
            print(error)

#makes sure input is not blank
def not_blank(question,error):
    while True:
        response = input(question).strip()

        if response == "":
            print()
            print("{}. \n \033[38;5;160m Please try again. \n".format(error))
            print()

        else:
            return response

# Function to check if the input matches any of the valid responses
def string_checker(question, num_letters, valid_response):
    # Create the error message by joining the valid responses
    error = f"\033[38;5;160m Please choose {', '.join(valid_response[:-1])} or {valid_response[-1]} \n"

    
    # Repeat the loop until a valid response is entered
    while True:
        # Get user input, convert to lowercase, and remove leading/trailing whitespace
        response = input(question).lower().strip()
        
        # Check if the response matches any of the valid responses
        for item in valid_response:
            # Check if the response matches either the full item or its first 'num_letters' characters
            if response == item[:num_letters] or response == item:
                return item
        
        # If none of the valid responses are matched, print the error message
        print(error)

# metric unit converting funtion(standard unit of g and ml)
def metric_unit_converter(amount,input_unit,standard_unit):

    # convert base amount to standard unit g and ml
    base_amount= amount*conversion_factors[input_unit]
    
    # gets converted amount
    converted_amount = base_amount / conversion_factors[standard_unit]
    
    #returns converted amount
    return converted_amount

#gets amount unit and ingreadeant name
def ingredients_and_amounts():
    # Sets up dictionaries and lists
    amount_1_list = []
    unit_1_list = []
    ingredient_list = []
    
    # Loop to get component, quantity, and price  
    print()
    
    #gets ingredeant name and amount
    ingredient_name = not_blank("\033[0;37;40mIngredient name: ", "\033[38;5;160m!!The ingredient name must not be blank!!. \n")
    print()
    amount = num_check("\033[0;37;40mHow much of this ingredient do you have? ", "\033[38;5;160m Please enter a number greater than zero. \n", float)
    print()

   #loops to make sure user gets the right unit
    while True:
        #asks user for unit
        unit_1 = string_checker("\033[0;37;40mWhat unit are you using for this amount? ", 1, unit_variables_list)
        
        # if the unit is valid
        if unit_1 in unit_variables_list:
            # Sets the standard unit based on the input
            break
        
        # if the unit is invalid
        else:
            print("\033[38;5;160mPlease enter the units kg, g, L, or ml. \n")
            continue

    # Sets the standard unit based on the input
    standard_unit = "ml" if unit_1 in ["ml", "l"] else "g"

    # converts amounts based on the unit    
    converted_unit_1=metric_unit_converter(amount,unit_1,standard_unit)
            
    # Add item, quantity, and price to lists
    amount_1_list.append(converted_unit_1)
    unit_1_list.append(standard_unit)
    ingredient_list.append(ingredient_name)

    return amount_1_list, unit_1_list , ingredient_list

# gets the cost and amount that you get for this cost
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

    # Loop to make sure user gets the right unit
    while True:
        unit_1 = string_checker("\033[0;37;40mWhat unit are you using for this amount? ", 1, unit_variables_list)
        if unit_1 in unit_variables_list:
            # Sets the standard unit based on the input
            break
        else:
            print("\033[38;5;160mPlease enter the units kg, g, L, or ml. \n")
            continue

    # Sets the standard unit based on the input
    standard_unit = "ml" if unit_1 in ["ml", "l"] else "g"

    # Convert unit and amount into standard unit and amount
    converted_unit_1 = metric_unit_converter(amount, unit_1, standard_unit)

    # Add item, quantity, and price to lists
    price_func_list.append(round(price_1, 2))
    amount_func_2_list.append(converted_unit_1)
    unit_func_2_list.append(standard_unit)

    return price_func_list, amount_func_2_list, unit_func_2_list
