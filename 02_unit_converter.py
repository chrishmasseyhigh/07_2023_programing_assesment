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
 
# metric unit converting funtion(standard unit of g and ml)
def metric_unit_converter(amount,input_unit,standard_unit):

    # convert base amount to standard unit g and ml
    base_amount= amount*conversion_factors[input_unit]
    
    converted_amount = base_amount / conversion_factors[standard_unit]
    return converted_amount

#main routine
#gets the unit used
input_unit = string_checker("What unit are you using? ",1,["kg","g","ml","l"])

#gets the amount of the unit
amount = num_check("how much of this unit are you using? ","The amount must be a whole number !!more than zero!!\n",int)

# sets the standard unit based on the input
if input_unit =="kg" or "g":
    standard_unit = "g"
else:
    standard_unit ="ml"

#convert input uint into the standard unit
converted_amount = metric_unit_converter(amount,input_unit,standard_unit)

# prints out what is being converted and to what
print(f"{amount} {input_unit} is equal to {converted_amount} {standard_unit}")