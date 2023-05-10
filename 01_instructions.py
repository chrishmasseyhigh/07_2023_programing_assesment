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


# **** main routine ****

#loop for testing
while True:
    #asks if user wants to see the instructions
    instruction =string_checker("Do you want to see the instructions? ",1,["yes","no"] )

    # prints instuctions is the answer is yes
    if instruction == "yes":
        instructions()
