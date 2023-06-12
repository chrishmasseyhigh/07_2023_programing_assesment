import math
# imports pandas to make dataframes
import pandas as pd

# sets up unit list
unit_variables_list = ["kg", "g", "l", "ml"]

# dictionary to store unitcs and their conversion factor
conversion_factors ={
    "kg" :1000,  
    "g":1,
    "ml":1,
    "l":1000,
}

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
            print("{}. \n Please try again. \n".format(error))
            print()

        else:
            return response

# Function to check if the input matches any of the valid responses
def string_checker(question, num_letters, valid_response):
    # Create the error message by joining the valid responses
    error = f"Please choose {', '.join(valid_response[:-1])} or {valid_response[-1]}"

    
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

# Displays instructions, returns ""
def instructions():
    
    print()

    print('''\n
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

    return""

#gets amount unit and ingreadeant name
def servings_and_recipes():
    # Sets up dictionaries and lists
    amount_1_list = []
    unit_1_list = []
    ingredient_list = []
    
    # Loop to get component, quantity, and price  
    x = 0
    print()
    
    #gets ingredeant name and amount
    ingredient_name = not_blank("Ingredient name: ", "The ingredient name must not be blank.")
    print()
    amount = num_check("How much of this ingredient do you have? ", "Please enter a number greater than zero.", float)
   
   #loops to make sure user gets the right unit
    while x == 0:
        #asks user for unit
        unit_1 = string_checker("What unit are you using for this amount? ", 1, unit_variables_list)
        
        # if the unit is valid
        if unit_1 in unit_variables_list:
            # Sets the standard unit based on the input
            break
        
        # if the unit is invalid
        else:
            print("Please enter the units kg, g, L, or ml.")
            continue

    # Sets the standard unit based on the input
    standard_unit = "g" if unit_1 in ["kg", "g"] else "ml"
            
    converted_unit_1=metric_unit_converter(amount,unit_1,standard_unit)
            

    # Add item, quantity, and price to lists
    amount_1_list.append(converted_unit_1)
    unit_1_list.append(standard_unit)
    ingredient_list.append(ingredient_name)

    return amount_1_list, unit_1_list , ingredient_list

#gets amount unit and ingreadeant name
def servings_and_recipes():
    # Sets up dictionaries and lists
    amount_1_list = []
    unit_1_list = []
    ingredient_list = []
    
    # Loop to get component, quantity, and price  
    x = 0
    print()
    
    #gets ingredeant name and amount
    ingredient_name = not_blank("Ingredient name: ", "The ingredient name must not be blank.")
    print()
    amount = num_check("How much of this ingredient do you have? ", "Please enter a number greater than zero.", float)
   
   #loops to make sure user gets the right unit
    while x == 0:
        #asks user for unit
        unit_1 = string_checker("What unit are you using for this amount? ", 1, unit_variables_list)
        
        # if the unit is valid
        if unit_1 in unit_variables_list:
            # Sets the standard unit based on the input
            break
        
        # if the unit is invalid
        else:
            print("Please enter the units kg, g, L, or ml.")
            continue

    # Sets the standard unit based on the input
    standard_unit = "g" if unit_1 in ["kg", "g"] else "ml"
            
    converted_unit_1=metric_unit_converter(amount,unit_1,standard_unit)
            

    # Add item, quantity, and price to lists
    amount_1_list.append(converted_unit_1)
    unit_1_list.append(standard_unit)
    ingredient_list.append(ingredient_name)

    return amount_1_list, unit_1_list , ingredient_list


# ****** '{Main Routine}' ******

#sets up lists for ingredients and amounts
amount_list = []
unit_1_list = []
ingredient_list = []

# Sets up lists for servings and recipes
price_list = []
amount_2_list = []
unit_2_list = []
cost_list = []

# sets loop and total to zero
loop = 0
total=0

#asks if user wants to see the instructions
instruction =string_checker("Do you want to see the instructions? ",1,["yes","no"] )

# prints instuctions is the answer is yes
if instruction == "yes":
    instructions()

servings_amount = num_check("How many servings will this recipe have when made? ","please enter a number more than zero",float)