import random
import time
import pandas as pd

"""
v3 changes:
- loop for if user enters ingredient that is not found, they are asked if they would 
like to try again. If no - end, if yes, prompt for input again.
- if user enters anything other than 1 or 2 when asked, loops back to ask again.
- added numbering for list of all recipes, user inputs number of recipe instead
of recipe name to list ingredients.
- imported takeaway list from CSV.
- imported dictionary of lists for recipes and recipe ingredients.

IMPROVEMENT:
- lists within dictionaries contain blank values where they are shorter than the longest 
list in the dictionary. This means the print statement following the printed list 
has a big gap. Look into removing the blanks so the lists are only as long as the number 
of items
*quick fix - break loop if item in list is blank.
"""

def main():
    ta_file = pd.read_csv(r"takeaway_list.csv")
    takeaway = ta_file['Takeaway'].tolist()
    #(r"C:\Users\Jeni & Michael\Proton Drive\Jeni.morrison\My files\Coding Projects\takeaway_list.csv")
    
    rc_file = pd.read_csv(r"recipes.csv", na_filter=False)
    all_recipes = rc_file.to_dict('list')
    #(r"C:\Users\Jeni & Michael\Proton Drive\Jeni.morrison\My files\Coding 

    found_recipes = []

    print("\nHmm, what to have for dinner? ")
    time.sleep(0.5)

    # Prompt the user to decide if they want to cook or not.
    choice = 0
    while choice != "y" and choice != "n":
        choice = input("Do you feel like cooking? (y/n): ")

    # If not, give them a random item from the Takeaway list.
    if choice == "n":
        time.sleep(0.5)
        print("\nTakeaway it is! You should get " + takeaway[random.randint(0, len(takeaway)-1)]+ ".")
        print("")

    else:    
        item = get_ingredient(all_recipes, found_recipes)
        
        # If the ingredient entered is not found in any of the recipes, 
        # inform the user and ask if they want to try again.
        while len(found_recipes) == 0:
            print("oh, it looks like you don't have any recipes that contain " + item)
            time.sleep(0.5)
            repeat = input("Would you like to search for another ingredient? (y/n) ")
            if repeat == "y":
                get_ingredient(all_recipes, found_recipes)
            else:
                time.sleep(0.5)
                print("ok, well I hope you find something to eat!\n")
                return
            
        # Provides an option to the user to see all recipes, or a single suggestion.
        # While loop will repeat the input prompt if the user enters anything other than the two options.
        option = 0
        while option != "1" and option != "2":
            option = get_option()

            if option == "1":
                suggest_recipe(all_recipes, found_recipes)
                
            elif option == "2":
                list_of_recipes(item, all_recipes, found_recipes)

            else:
                print("oops, try that again")
                time.sleep(0.5)
                option = 0

        
        print("")
        time.sleep(0.5)
        print("Enjoy your meal :)\n")



def get_ingredient(all_recipes, found_recipes):
        # Prompt the user to enter an ingredient they want to use. 
        # This will be used to display recipes containing this ingredient.
        print("")
        user_input = input("What ingredient do you want to use? ")
        # Search dictionary of recipes to find all instances of the ingredient entered. 
        # The recipes containing the ingredient will be added to a new list.
        for recipe, ingredients in all_recipes.items():
            if user_input in ingredients:
                found_recipes.append(recipe)
        return user_input

def get_option():
        option = input("\nEnter: \n 1 for a single suggestion, or \n 2 for all options \nSelection: ")
        print("")
        return option



# Use randint to print a random recipe from the list of found recipes.
# Provide an option for the user to see the ingredient list for the suggested recipe.
def suggest_recipe(all_recipes, found_recipes):
    suggestion = found_recipes[random.randint(0, len(found_recipes)-1)]
    print("You should make " + suggestion + ".\n")
    time.sleep(1)
    display = input("Would you like to see the list of ingredients? (y/n) ")
    if display == "y":
        print("\n" + suggestion + " contains:")
        for item in all_recipes[suggestion]:
            if item == "":
                break
            else:
                print(item)

# Print all recipes on the list of found recipes.
# Provide an option for the user to see the ingredient list for a recipe of their choice.
def list_of_recipes(item, all_recipes, found_recipes):
    print("These are all your recipes that contain '" +  item + "':")
    for i in range(len(found_recipes)):
        print(i + 1, found_recipes[i])
    print("")
    time.sleep(1)
    display = input("Would you like to see the list of ingredients for one of these recipes? (y/n) ")
    if display == "y":
        show = -1
        while show < 0 or show > len(found_recipes)-1:
            show = int(input("Enter the number of the recipe you would like to see the ingredients for: "))-1          
            if show >= 0 and show <= len(found_recipes)-1: 
                find_recipe = found_recipes[show]
                print("\n" + find_recipe + " contains:")
                for item in all_recipes[find_recipe]:
                    if item == "":
                        break
                    else:
                        print(item) 
            else:
                print("oops, try that again")
                time.sleep(0.5)
                show = -1

if __name__ == "__main__":
    main()