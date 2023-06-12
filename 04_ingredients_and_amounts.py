import math

# unit list
unit_variables_list = ["kg", "g", "l", "ml"]

# dictionary to store unitcs and their conversion factor
conversion_factors ={
    "kg" :1000,  
    "g":1,
    "ml":1,
    "l":1000,
}

# Rounding function
def round_up(num, round_to):
    return int(math.ceil(num / round_to)) * round_to

# Check if the input matches
def string_checker(question, num_letters, valid_response):
    error = "Please choose "
    
    for item in valid_response[:-1]:
        error += item + ", "
        
    error += "or " + valid_response[-1]

    while True:
        response = input(question).lower().strip()
        
        for item in valid_response:
            if response == item[:num_letters] or response == item:
                return item
            
        print(error)
 
# Check that input is a float or int that is more than 0 (custom error message)
def num_check(question, error, num_type):
    valid = False
    while not valid:
        try:
            response = num_type(input(question))
            
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)
    
# Make sure input is not blank
def not_blank(question, error):
    while True:
        response = input(question).strip()
        if response == "":
            print(error)
        else:
            return response

# Displays instructions, returns ""
def instructions():
    print("\n**** Instructions *****")
    print("This program will ask you for...")
    print("- The name of the product you are selling")
    print("- How many items you plan on selling")
    print("- The costs for each component of the product")
    print("- How much money you want to make")
    print("It will then output an itemised list of the costs")
    print("with subtotals for the variable and fixed costs.")
    print("Finally, it will tell you how much you should sell")
    print("each item for to reach your profit goal.")
    print("The data will also be written to a text file")
    print("which has the same name as your product.")
    print("**** Program launched! ****\n")
    return ""


# metric unit converting funtion(standard unit of g and ml)
def metric_unit_converter(amount,input_unit,standard_unit):

    # convert base amount to standard unit g and ml
    base_amount= amount*conversion_factors[input_unit]
    
    # gets converted amount
    converted_amount = base_amount / conversion_factors[standard_unit]
    
    #returns converted amount
    return converted_amount

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

#**** main routine ****

#sets up lists
amount_list = []
unit_1_list = []
ingredient_list = []

# Sets serving for testing
servings = 2.5

while True:
    
    # activates funtion and oututs amount unit and ingertant lists
    amount, unit, ingredient = servings_and_recipes(servings)
    
    # puts all the information into lists
    amount_list.extend(amount)
    unit_1_list.extend(unit)
    ingredient_list.extend(ingredient)
    

    #asks user if they want to quit
    quit_input = input("Enter xxx to quit: ")

    if quit_input == 'xxx':
        break


#prints lists for testing
print(amount_list)
print(unit_1_list)
print(ingredient_list)


