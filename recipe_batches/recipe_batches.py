#!/usr/bin/python

import math

#We need to compare the amounts of ingredients we have vs what's in the recipe and if we don't have enough, function ends as we can't make the recipe

def recipe_batches(recipe, ingredients):
    results = [0] * len(recipe.values())                                          #the 0 index for the length of recipe.values
    difference = set(recipe.keys()) - set(ingredients.keys())                     #difference = collection of recipe keys minus ingredient keys
    for d in difference:                                                          #for each item in the difference
        ingredients[d] = 0                                                        #index of ingredients set to 0
    ingredients_values = list(ingredients.values())                               #ingredients_values = the list of ingredients.values
    recipe_values = list(recipe.values())                                         #recipe_values = the list of recipe.values
    for i in range(len(results)):                                                 #for loop for each item in range of the length of results
        results[i] = int(ingredients_values[i] / recipe_values[i])                #results of index item = integer of ingredients_values item / recipe_values item
    if min(results) < 1:                                                          #if min of results is less than 1
        return 0                                                                  #return 0
    return min(results)                                                           #return min results

"""
def recipe_batches(recipe, ingredients):
  finished = 0
  total = 0
  while finished == 0:
    for i in recipe.keys():
      if i in ingredients.keys():
        ingredients[i] = ingredients[i] - recipe[i]
        if ingredients[i] < 0:
          finished = 1
        else:
          return 0 
        if finished == 0:
          total = total +1
      return total
      """

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))