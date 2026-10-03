class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # dfs approach- each email is a node and emails belonging same account are connected by edges. Then each connected component represents one merged account. 
        emailtoname= {}
        adj= defaultdict(list) # adj list- first email is mapped to its neighbours (connected emails belonging to same account)

        # build the graph
        for account in accounts:
            name= account[0]
            for email in account[1:]:
                emailtoname[email]=name
            first= account[1]
            for email in account[2:]:
                adj[first].append(email)
                adj[email].append(first)

        # dfs function
        visited= set()
        res=[]
        def dfs(email,group):
            visited.add(email)
            group.append(email)
            for nei in adj[email]:
                if nei not in visited:
                    dfs(nei,group)

        # dfs each connected component
        for email in emailtoname:
            if email not in visited:
                group= []
                dfs(email,group)
                res.append([emailtoname[email]] + sorted(group))
        return res

            

        
