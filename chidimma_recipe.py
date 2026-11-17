import os
from datetime import datetime
from tabulate import tabulate

"""
Recipe manager: Build a console-based recipe manager. 
Users should be able to add recipes,view recipes, search for recipes 
by ingredients,and perform other recipes-releted operation.
"""

recipes = []

def view_task():
  """Shows the tasks to perform"""
  print("=== SELECT A TASK TO PERFORM ===")
  print("1. Add recipe")
  print("2. View recipe")
  print("3. Search for a recipe by ingredient")
  print("4. Update a single recipe")
  print("5. Delete a single recipe")
  print("6. Delete all recipes")
  print("7. Exit task")


def clear_console():
  """Clear a console"""
  os.system("cls" if os.name == "nt" else "clear")


def add_recipe():
  food_type = input("Enter food type: ").strip().lower()
  if check_food_exist(food_type):
    print(f"Recipe type {food_type} already exist")
  elif len(food_type) < 3:
    print("Recipe should be descriptive")
  else:
    add = {}
    add["name"] = food_type
    add["ingredients"] = input("Enter ingredients separated by comma: ").strip().split(",")
    add["cooking-step"] = input("Enter the steps in cooking the recipe separated by comma: ").strip().split(",")
    add["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    recipes.append(add)
    print("Recipe added successfully")
    return recipes



def check_food_exist(name):
  """Function that checks if a recipe exists"""
  for food in recipes:
    if food["name"] == name:
      return True
  return False



def View_recipe():
  """Display all recipes in a tabular form"""
  if recipes:
    table = [] #empty
    for num, item in enumerate(recipes,1):
      table.append([
        num,
        item["name"],
        item["ingredients"],
        item["cooking-step"],
        item["date"]
      ])
      print(
        tabulate(
          table,
          headers=["serial number","Recipe Type","Ingredients Used","Cooking Step","Date & Time"],
          tablefmt="grid"
        )
      )
  else:
    print("No recipe found")



def Search_for_a_recipe_by_ingredient():
  """
  The ingredients used to cook the recipe, are used
  to search for the recipe. Make sure you remember
  the ingredients used. View the recipes for easy
  access.
  """

  ingredient = input("Enter ingredients used: ").lower().split(",")
  for recipe in recipes:
    if recipe["ingredients"] == ingredient:
      print(f"Recipe type ({recipe["name"].upper()}) is found!!!")
      break
  else:
    print("No such ingrdients found!")


def Update_a_sindle_recipe():
  """Update a single recipe using an integer"""
  update_num = int(input("Enter a number to update a recipe: "))
  for num,item in enumerate(recipes, 1):
    if num == update_num:
      item["name"] = input("Enter recipe name to update: ").lower().strip()
      item["ingredients"] = input("Enter ingredients separated by comma to update: ").split(",")
      item["cooking-step"] = input("Enter cooking step separated by comma to update: ").split(",")
      item["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      print("Recipe type updated successfully!")
      break
  else:
    print("No such integer exist,Try again later")



def Delete_a_single_recipe():
  """Use an integer to get a recipe to delete"""
  delete_recipe = int(input("Enter an integer to delete a single recipe: "))
  for num,item in enumerate(recipes, 1):
    if num == delete_recipe:
      recipes.remove(item)
      print(f"{item["name"]} deleted successfully!")
      break
  else:
    print("Recipe type does not exist, Try again")



def Delete_all_recipes():
  """Delete all recipes"""
  if recipes:
    recipes.clear()
    print("All recipes deleted successfully!")
  else:
    print("No recipe exist in the list")



def Exit_task():
  """Exit Task"""
  print("Task has finished, Exiting......")
  print("Please enter a number greater than 7 to exit the task program...")



def main():
  """Execution Guard"""
  while True:
    clear_console()
    view_task()
    user = input("Enter a number to perform a task: ")

    if user == "1":
      add_recipe()
      input("Press enter to continue...")
      clear_console()

    elif user == "2":
      View_recipe()
      input("Press enter to continue...")
      clear_console()

    elif user == "3":
      Search_for_a_recipe_by_ingredient()
      input("Press enter to continue...")
      clear_console()


    elif user == "4":
      Update_a_sindle_recipe()
      input("Press enter to continue...")
      clear_console()

    elif user == "5":
      Delete_a_single_recipe()
      input("Press enter to continue...")
      clear_console()


    elif user == "6":
      Delete_all_recipes()
      input("Press enter to continue...")
      clear_console()


    elif user == "7":
      Exit_task()
      input("Please enter a number more than 7 to exit task")
      clear_console()


    else:
      print("Task has finished, come again next time to perform a task")
      break


if __name__ == "__main__":
  main()