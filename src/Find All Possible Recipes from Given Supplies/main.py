from collections import defaultdict, deque
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegrees = defaultdict(int)
        all_ingredients = set()

        for index in range(len(recipes)):
            recipe = recipes[index]
            ingredient = ingredients[index]
            for ing in ingredient: 
                graph[ing].append(recipe)
                indegrees[recipe] += 1
                all_ingredients.add(recipe)
                all_ingredients.add(ing)

        queue = deque()
        supplies = set(supplies)
        for ingredient in all_ingredients:
            if indegrees[ingredient] != 0 or ingredient not in supplies: continue
            queue.append(ingredient)

        recipes = set(recipes)
        answer = []
        while queue:
            ingredient = queue.popleft()
            if ingredient in recipes: answer.append(ingredient)
            for neighbour in graph[ingredient]:
                indegrees[neighbour] -= 1
                if indegrees[neighbour] != 0: continue
                queue.append(neighbour)
        return list(answer)
