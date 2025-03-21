class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        ableToMake = []
        supplyIndex = 0
        while supplyIndex < len(supplies):
            ingredientIndex = 0
            while ingredientIndex < len(ingredients):
                # print(supplies[supplyIndex])
                if supplies[supplyIndex] in ingredients[ingredientIndex]:
                    ingredients[ingredientIndex].remove(supplies[supplyIndex])
                # print(ingredients, ingredientIndex)
                if ingredients[ingredientIndex] == []:
                    # print('able to make', recipes[ingredientIndex])
                    ableToMake.append(recipes[ingredientIndex])
                    supplies.append(recipes[ingredientIndex])
                    ingredients.pop(ingredientIndex)
                    recipes.pop(ingredientIndex)
                    ingredientIndex -= 1
                ingredientIndex += 1
            supplyIndex += 1
            # print(supplyIndex, len(supplies))
        return ableToMake


if __name__ == '__main__':
    print('in main')
    recipes = ["bread", "sandwich", "burger"]
    ingredients = [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]]
    supplies = ["yeast", "flour", "meat"]
    print(Solution().findAllRecipes(recipes, ingredients, supplies))
