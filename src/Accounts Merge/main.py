from collections import defaultdict
from typing import List

class Solution:
    def __dfs(self, name: str, merged: set, graph: defaultdict, ans: List[str]):
        merged.add(name)
        ans.append(name)
        for acc in graph[name]:
            if acc in merged: continue
            self.__dfs(acc, merged, graph, ans)

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails = defaultdict(set)
        for account in accounts:
            for i in range(1, len(account)):
                for j in range(i + 1, len(account)):
                    emails[account[i]].add(account[j])
                    emails[account[j]].add(account[i])
        
        merged = set()
        answer = []
        for account in accounts:
            if account[1] in merged: continue
            ans = []
            self.__dfs(account[1], merged, emails, ans)
            answer.append([account[0]] + sorted(ans))
        return answer