"""
Professor Utonium is restless because of the increasing crime in the world. The number of villains and their activities has increased to a great extent. The current trio of Powerpuff Girls is not well to fight the evils of the whole world. Professor has decided to create the maximum number of Powerpuff Girls with the ingredients he has.

There are N ingredients required in a certain quantity to create a Powerpuff Girl. Professor has all the N ingredients in his laboratory and knows the quantity of each available ingredient. He also knows the quantity of a particular ingredient required to create a Powerpuff Girl. Professor is busy with the preparations and wants to start asap.

The villains, on the other hand, want to destroy the laboratory and stop Professor Utonium from creating more Powerpuff girls. Mojo Jojo is coming prepared with ammunition and Him is leading other villains like Princess, Amoeba Boys, Sedusa, Gangreen Gang etc.

Professor does not have much time as villains will reach the laboratory soon. He is starting the process but does not know the number of Powerpuff Girls which will be created. He needs your help in determining the maximum number of Powerpuff Girls which will be created with the current quantity of ingredients. 

Example:

Professor Utonium requires 3 ingredients to make Powerpuff Girls. The 3 ingredients are present in the laboratory in the given quantity:

10 units of Ingredient A

20 units of Ingredient B

30 units of Ingredient C

To make a Powerpuff Girl, Professor Utonium requires:

3 units of Ingredient A

6 units of Ingredient B

10 units of Ingredient C

The maximum number of Powerpuff Girls which can be created are 3 as after 3, Professor will run out of Ingredient C.
"""


def main():

    # Number of ingredients
    ingredients = int(input())
    # Quantity of each ingredient required to create a Powerpuff Girl.
    quantity_of_each_ingredients = list(map(int,input().split()))
    # Quantity of each ingredient present in the laboratory.
    ingredients_in_laboratory = list(map(int,input().split()))
    # Total Powerpuff Girl created from each ingredient
    powerpuff_girls = []

    for ingredient_in_laboratory,quantity_of_ingredient in zip(ingredients_in_laboratory, quantity_of_each_ingredients):
        created_powerpuff_girl = ingredient_in_laboratory / quantity_of_ingredient
        powerpuff_girls.append(created_powerpuff_girl)
    print(int(sorted(powerpuff_girls)[0]))
 
if __name__ == "__main__":
    main()


"""
Input:
4
2 5 6 3 
20 40 90 50 

Output:
8
"""