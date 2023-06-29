# Imports pandas to make dataframes
import pandas as pd
import importlib

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

# Imports all functions
from all_functions import instructions
from all_functions import metric_unit_converter
from all_functions import ingredients_and_amounts
from all_functions import not_blank
from all_functions import num_check
from all_functions import string_checker
from all_functions import amounts_and_costs

# ************* '{Main Routine}' *************

# Sets up lists for ingredients and amounts
amount_list = []
unit_list = []
ingredient_list = []

# Sets up lists for servings and recipes
price_list = []
amount_2_list = []
unit_2_list = []
cost_list = []

# Sets loop and total to zero
loop = 0
total=0
amounts_and_costs_loop =0

# Start of the program
print("\033[38;5;81m********* Wellcome to the recipe cost calculator *********")
print()

# Asks if user wants to see the instructions
instruction =string_checker("\033[0;37;40m Do you want to see the instructions? ",1,["yes","no"] )
print()

# Prints instuctions is the answer is yes
if instruction == "yes":
    instructions()

# Gets recipe name for printing and naming of file
recipe_name = not_blank("\033[0;37;40m What is the name of the recipe? ","\033[38;5;160m !!This answer can not be blank!!")
print()

# Gets the amount of servings made from the recipe
servings_amount = num_check("\033[0;37;40m  How many servings will this recipe have when made? ","\033[38;5;160m please enter a number more than zero",float)

# signals to the user that they now need to input ingredients and amounts
print()
print("\033[38;5;81m**************** [Ingredients and amounts] ****************")

# Gets ingredeant names and amounts
while True:
    
    # Activates funtion and oututs amount unit and ingertant lists
    amount, unit, ingredient = ingredients_and_amounts()
    
    # Puts all the information into lists
    amount_list.extend(amount)
    unit_list.extend(unit)
    ingredient_list.extend(ingredient)
    
    # Asks user if they want to quit
    print()
    quit_input = input("Enter 'xxx' if you have finished entering your ingredients: ")

    if quit_input == 'xxx':
        break

# Bulk price heading
print()
print("\033[38;5;81m**************** [Bulk prices] ****************")
print()

# Gets all bulk price varibles and calculates the cost
while True:
    
    # Gets the ingredent and formats it into a intrduction for each loop to tell the user what ingrent the prices are for
    bulk_price_ingredint = ingredient_list[amounts_and_costs_loop]
    Introduction_for_bulk_prices =f'\033[0;37;40m***** Bulk price for [{bulk_price_ingredint}] *****'
    
    # Prints the introduction for bulk prices
    print(Introduction_for_bulk_prices)

    # Activate function and output amount, unit, and ingredient lists
    price, amount, unit = amounts_and_costs()

    # Puts all the information into lists
    price_list.extend(price)
    amount_2_list.extend(amount)
    unit_2_list.extend(unit)

    # Adds one the the loop
    amounts_and_costs_loop +=1

    #  Quits when all varibles have been gathered
    if amounts_and_costs_loop == len(unit_list):

        # Loops to calcualtes the final cost
        while loop < len(price_list):
            
            # Calculates cost
            cost = price_list[loop] / amount_2_list[loop]
            total_ingredient_cost = cost * amount_list[loop]
            
            # Adds ingredint cost to total cost
            total += total_ingredient_cost
            
            # Rounds and andds ingredeant cost to list
            cost_list.append(round(total_ingredient_cost,2))
            
            # Add one cyle to the loop
            loop += 1
            
        # Breaks loop
        break


# ************ [write to file] ************

# Dictionaries to format data
recipe_amount_dict = {
    "amount": amount_list,
    "units": unit_list,
    "ingredient": ingredient_list
}

recipe_cost_dict = {
    "price": price_list,
    "amount": amount_2_list,
    "units": unit_2_list,
    "cost": cost_list
}

# Uses pandas to create dataframes
recipe_cost_frame = pd.DataFrame(recipe_cost_dict)
recipe_amount_frame = pd.DataFrame(recipe_amount_dict)

# Sets the name of the recipe and serving size
serving_size = f'Servings: {servings_amount}'

# Sets headings
recipe_heading = f"************** {recipe_name} **************"
list_1_heading = "Recipe Ingredients"
list_2_heading = "Ingredient Price"

# Totals for testing
total_heading = f"Total: ${round(total,2)}"
per_serve_heading = f"Per Serve: ${round(total / servings_amount,2)}"

# Converts dataframes to string
recipe_cost_txt = recipe_cost_frame.to_string(index=False)
recipe_amount_txt = recipe_amount_frame.to_string(index=False)

# Puts all files in a list for writing to the file
to_write = [recipe_heading, serving_size, list_1_heading, recipe_amount_txt, 
            list_2_heading, recipe_cost_txt, total_heading, per_serve_heading]

# Write to file
# Create file to hold data (add .txt extension)
file_name = "{}.txt".format(recipe_name)
text_file = open(file_name, 'w+')

# Heading
for item in to_write:
    text_file.write(item)
    text_file.write("\n\n")

# Closes the file
text_file.close()

# Print the contents of the files for testing
for item in to_write:
    print(item)
    print()