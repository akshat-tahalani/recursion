from collections import deque , defaultdict
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        #we wiell try coding kahns algorithm for topological sorting first then we will perfrom the resrt

        #find out the indegree firsr 
        ans = []
        graph = defaultdict(list)

        indegree = {}

        for i , recipe in enumerate(recipes):
            indegree[recipe] = len(ingredients[i])
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipe)

        q = deque(supplies)

        while len(q) > 0:
            curr = q.popleft()
            
            for recipe in graph[curr] :
                indegree[recipe] -=1
                if indegree[recipe] == 0:
                    q.append(recipe) 
                    ans.append(recipe)
               
                    
        
        return ans

        
        

        