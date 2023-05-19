import pandas as pd

# lists for testing
amount_1_list = [166, 40, 5, 2, 1, 3, 4]
unit_1_list = ["g", "g", "g", "g", "g", "g", "g"]
ingredient_list = ["Chickpeas", "Onion", "Parsley", "Cumin", "Ground Coriander", "Salt", "Chickpeas"]
price_list = [3.70, 2.49, 5.00, 2.00, 2.30, 1.40, 10.00]
amount_2_list = [500, 1000, 8, 30, 30, 1000, 1000]
unit_2_list = ["g", "g", "g", "g", "g", "g", "g"]
cost_to_make_list = [1.23, 0.10, 3.13, 0.13, 0.08, 0.00, 0.04]

#dictionarys to format data
recipe_amount_dict = {
    "amount": amount_1_list,
    "ingredients": ingredient_list,
    "units": unit_1_list
}

recipe_cost_dict = {
    "price": price_list,
    "amount": amount_2_list,
    "units": unit_2_list,
    "cost to make": cost_to_make_list
}

# uses pandas to make a dataframe
recipe_cost_frame = pd.DataFrame(recipe_cost_dict)
recipe_amount_frame = pd.DataFrame(recipe_amount_dict)

#sets name of file for testing
recipe_name = "boiled eggs"

# converts dataframes to txt file
recipe_cost_txt = recipe_cost_frame.to_string()
recipe_amount_txt = recipe_amount_frame.to_string()

# puts all files in a list for writing to file
to_write = [recipe_cost_frame, recipe_amount_frame]

# write to file
# create file to hold data (add .txt extension)
file_name = "{}.txt".format(recipe_name)
text_file = open(file_name, 'w+')

# heading
for item in to_write:
    text_file.write(item.to_string())
    text_file.write("\n\n")

# close file
text_file.close()

# print stuff
for item in to_write:
    print(item)
    print()
