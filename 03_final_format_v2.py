# imports pandas to make dataframes
import pandas as pd

# Lists for testing
amount_1_list = [166, 40, 5, 2, 1, 3, 4]
unit_1_list = ["g", "g", "g", "g", "g", "g", "g"]
ingredient_list = ["Chickpeas", "Onion", "Parsley", "Cumin", "Ground Coriander", "Salt", "Chickpeas"]
price_list = [3.70, 2.49, 5.00, 2.00, 2.30, 1.40, 10.00]
amount_2_list = [500, 1000, 8, 30, 30, 1000, 1000]
unit_2_list = ["g", "g", "g", "g", "g", "g", "g"]
cost_to_make_list = [1.23, 0.10, 3.13, 0.13, 0.08, 0.00, 0.04]

# Dictionaries to format data
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

# Uses pandas to create dataframes
recipe_cost_frame = pd.DataFrame(recipe_cost_dict)
recipe_amount_frame = pd.DataFrame(recipe_amount_dict)

# Remove the index column from the dataframes
recipe_cost_frame = recipe_cost_frame.reset_index(drop=True)
recipe_amount_frame = recipe_amount_frame.reset_index(drop=True)

# Sets the name of the recipe and serving size
recipe_name = "dog_food"
servings = 2.5
serving_size = "Servings: 2.5"

# Sets headings
recipe_heading = f"************** {recipe_name} **************"
list_1_heading = "Recipe Ingredients"
list_2_heading = "Ingredient Price"

# Totals for testing
total = 4.71
total_heading = f"Total: ${total}"
per_serve_heading = f"Per Serve: ${total/servings}"

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

