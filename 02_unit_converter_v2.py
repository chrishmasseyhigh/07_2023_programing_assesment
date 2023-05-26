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

#main routine

#loop for testing   
while True:

    #gets the unit used
    input_unit = string_checker("What unit are you using? ",1,["kg","g","ml","l"])

    #gets the amount of the unit
    amount = num_check("How much of this unit are you using? ","The amount must be a whole number !!more than zero!!\n",int)

    # Sets the standard unit based on the input
    standard_unit = "g" if input_unit in ["kg", "g"] else "ml"

    #convert input uint into the standard unit
    converted_amount = metric_unit_converter(amount,input_unit,standard_unit)

    # prints out what is being converted and to what
    print(f"{amount} {input_unit} is equal to {converted_amount} {standard_unit}")