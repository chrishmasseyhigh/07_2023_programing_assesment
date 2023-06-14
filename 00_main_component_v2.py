
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
def ingredients_and_amounts():
    # Sets up dictionaries and lists
    amount_1_list = []
    unit_1_list = []
    ingredient_list = []
    
    # Loop to get component, quantity, and price  
    print()
    
    #gets ingredeant name and amount
    ingredient_name = not_blank("Ingredient name: ", "The ingredient name must not be blank. \n")
    print()
    amount = num_check("How much of this ingredient do you have? ", "Please enter a number greater than zero. \n", float)
   
   #loops to make sure user gets the right unit
    while True:
        #asks user for unit
        unit_1 = string_checker("What unit are you using for this amount? ", 1, unit_variables_list)
        
        # if the unit is valid
        if unit_1 in unit_variables_list:
            # Sets the standard unit based on the input
            break
        
        # if the unit is invalid
        else:
            print("Please enter the units kg, g, L, or ml. \n")
            continue

    # Sets the standard unit based on the input
    standard_unit = "g" if unit_1 in ["kg", "g"] else "ml"
            
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
    price_1 = num_check("What is the bulk price of this ingredient? $ ", "Please enter a number greater than zero. \n", float)
    print()
    
    # Gets the amount
    amount = num_check("How much of this ingredient do you get for this bulk price? ", "Please enter a number greater than zero. \n", float)
    
    # Loop to make sure user gets the right unit
    while True:
        unit_1 = string_checker("What unit are you using for this amount? ", 1, unit_variables_list)
        if unit_1 in unit_variables_list:
            # Sets the standard unit based on the input
            break
        else:
            print("Please enter the units kg, g, L, or ml. \n")
            continue

    # Sets the standard unit based on the input
    standard_unit = "g" if unit_1 in ["kg", "g"] else "ml"

    # Convert unit and amount into standard unit and amount
    converted_unit_1 = metric_unit_converter(amount, unit_1, standard_unit)

    # Add item, quantity, and price to lists
    price_func_list.append(round(price_1, 2))
    amount_func_2_list.append(converted_unit_1)
    unit_func_2_list.append(standard_unit)

    return price_func_list, amount_func_2_list, unit_func_2_list


# ****** '{Main Routine}' ******

#sets up lists for ingredients and amounts
amount_list = []
unit_list = []
ingredient_list = []

# Sets up lists for servings and recipes
price_list = []
amount_2_list = []
unit_2_list = []
cost_list = []

# sets loop and total to zero
loop = 0
total=0
amounts_and_costs_loop =0

# start of the program
print("********* Wellcome to the recipe cost calculator *********")
print()

#asks if user wants to see the instructions
instruction =string_checker("Do you want to see the instructions? ",1,["yes","no"] )
print()

# prints instuctions is the answer is yes
if instruction == "yes":
    instructions()

# gets recipe name for printing and naming of file
recipe_name = not_blank("What is the name of the recipe? ","!!This answer can not be blank!!")
print()

# get the amount of servings made from the recipe
servings_amount = num_check("How many servings will this recipe have when made? ","please enter a number more than zero",float)

# signils to the user that they now need to input ingredients and amounts
print()
print("**************** [Ingredients and amounts] ****************")

# loops until all varibles are gathered
while True:
    
    # activates funtion and oututs amount unit and ingertant lists
    amount, unit, ingredient = ingredients_and_amounts()
    
    # puts all the information into lists
    amount_list.extend(amount)
    unit_list.extend(unit)
    ingredient_list.extend(ingredient)
    
    #asks user if they want to quit
    quit_input = input("Enter xxx to quit: ")

    if quit_input == 'xxx':
        break

# seperates the two diffrent loops
print()
print("**************** [Bulk prices] ****************")
print()


# loops until all varibles have been gathered
while True:
    
    # gets the ingredent and formats it into a intrduction for each loop to tell the user what ingrent the prices are for
    bulk_price_ingredint = ingredient_list[amounts_and_costs_loop]
    Introduction_for_bulk_prices =f'***** Bulk price for [{bulk_price_ingredint}] *****'
    
    #prints the introduction for bulk prices
    print(Introduction_for_bulk_prices)

    # Activate function and output amount, unit, and ingredient lists
    price, amount, unit = amounts_and_costs()

    # Puts all the information into lists
    price_list.extend(price)
    amount_2_list.extend(amount)
    unit_2_list.extend(unit)

    # adds one the the loop
    amounts_and_costs_loop +=1

    #  quits when all varibles have been gathered
    if amounts_and_costs_loop == len(unit_list):

        # loops to calcualtes the final cost
        while loop < len(price_list):
            
            # calculates cost
            cost = price_list[loop] / amount_2_list[loop]
            total_ingredient_cost = cost * amount_list[loop]
            
            # adds ingredint cost to total cost
            total += total_ingredient_cost
            
            # rounds and andds ingredeant cost to list
            cost_list.append(round(total_ingredient_cost,2))
            
            # add one cyle to the loop
            loop += 1
            
        #breaks loop
        break



# Dictionaries to format data
recipe_amount_dict = {
    "amount": amount_list,
    "units": unit_list,
    "ingredients": ingredient_list
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

# Close the file
text_file.close()

# Print the contents of the files
for item in to_write:
    print(item)
    print()
