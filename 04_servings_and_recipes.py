import math
import pandas
# unit list
unit_list =["kg","g","l","ml"]



#Rounding function
def round_up(num, round_to):
  
    return int(math.ceil(num / round_to)) * round_to

#check if the input matches 
def string_checker(question,num_letters,valid_response):
    
    error = "Please choose "
    
    for item in valid_response[:-1]:
        error += item
        error += " "
        
    error += "or "
    error += valid_response[-1]

    while True:
        response=input(question).lower().strip()
        
        for item in valid_response:
            if response == item[:num_letters] or response== item:
                return item
            
        print(error)
 
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

# currency formatting function
def currency(x):
    return "${:.2f}".format(x)

# gets expenses, returns list which has
# the data frame and sub total
def get_expenses(var_fixed):
    
    
    
    #sets up dictionaries and lists
    
    item_list = []
    quantity_list = []
    price_list = []
    
    variable_dict = {
       "Item": item_list,
       "Quantity":quantity_list,
       "Price":price_list
            
    }
    
    # loop to get component, quantity and price  
    while True:
        
        print()
        # get name, quantity and item 
        item_name = not_blank("Item name(xxx to quit): ", "the Component name must not be blank ")
        if item_name.lower() == "xxx":
            break

        if var_fixed == "variable":  
            quantity = num_check("Quantity: ",
            "The amount must be a whole number !!more than zero!!\n",int)
        else:
            quantity = 1

        price =  num_check("How much for a singe item?: $ ","Please enter a number !!more than zero!!\n",float)

        # add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)
    
    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')
    

    # # Calculate cost of each component
    expense_frame['Cost'] = expense_frame['Quantity']  * expense_frame["Price"]  
        

    # Find sub total
    sub_total = expense_frame['Cost'].sum()
    
    # currency formatting (uses currency function)
    add_dollars = ['Price','Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)
        
    return [expense_frame,sub_total]

def expense_print(heading,frame,subtotal):
    print()
    print("**** {} Costs ****".format(heading))
    print(frame)
    print()
    print("{} Costs: ${:.2f}".format(heading, subtotal))


def profit_goal(total_costs):
    
    # Initialise variables and error message
    error = "Please enter a valid profit goal\n"
    
    while True:
        
        #ask for profit goal...
        response = input("What is your profit goal (eg $500 or 50%): ")
        
        # checks if first character is $
        if response[0] == "$":
            profit_type = "$"  
            # Get amount(everything after the $)
            amount = response[1:]
            
        # check if last char is %
        elif response[-1] == "%":
            profit_type = "%"
            # Get amount (everything before the %)
            amount = response[:-1]
        
        else:
            # set response to amount for now
            profit_type = "unknown"
            amount = response
        
        try:
            # Check amount is a number more than 0
            amount = float(amount)
            if amount<= 0:
                print(error) 
                continue  
        except ValueError:
            print(error)
            continue

        if profit_type == "unknown" and amount >=100:
            dollar_type = string_checker("Do you mean ${:.2f}. ie {:.2f} dollars , y / n: ".format(amount,amount),1,yes_no_list)

            # set profit type based on user answer above
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type ="%"
                
        if profit_type == "unknown" and amount <=100:
            percent_type = string_checker("Do you mean {:.2f}% , y / n: ".format(amount),1,yes_no_list)

            # set profit type based on user answer above
            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type ="$"
        
        # return profit goal to main routine
        if profit_type == "$":
            return amount
        else:
            goal =(amount/100) * total_costs
            return goal

# Displays instructions, returns ""
def instructions():
    print()

    print('''\n
    **** Instructions *****

    This program will ask you for...
    - The name of the product you are selling
    - How many items you plan on selling
    - The costs for each component of the product
    - How much money you want to make

    It will then output an itemised list of of the costs
    with subtotals for the variable and fixed costs.
    
    Finally it will tell you how much you should sell
    each item for to reach your profit goal.

    The data will also be written to a text file which
    has the same name a» your product.

    **** Program launched! ****''')

    return""
    

def servings_and_recipes(var_fixed):
    
    
    #sets up dictionaries and lists
    
    amount_1_list = [166, 40, 5, 2, 1, 3, 4]
    unit_1_list = ["g", "g", "g", "g", "g", "g", "g"]
    ingredient_list = ["Chickpeas", "Onion", "Parsley", "Cumin", "Ground Coriander", "Salt", "Chickpeas"]
    
    # Dictionaries to format data
    recipe_amount_dict = {
        "amount": amount_1_list,
        "ingredients": ingredient_list,
        "units": unit_1_list
    }
    
    # loop to get component, quantity and price  
    while True:
        x=0
        print()
        amount =  num_check("How much for a singe item?: $ ","Please enter a number !!more than zero!!\n",float)
       
        while x==0:
            unit_1 = not_blank("what unit are you using for this amount?: ","please eneter the units kg,g,L or ml")
            
            if unit_1 in unit_1_list:
                break
            
            else:
                print("please eneter the units kg,g,L or ml")
                continue

        ingredeant_name = not_blank("Item name(xxx to quit): ", "the Component name must not be blank ")
       

        # add item, quantity and price to lists
        amount_1_list.append(amount)
        unit_1_list.append(unit_1)
        ingredient_list.append(ingredeant_name)