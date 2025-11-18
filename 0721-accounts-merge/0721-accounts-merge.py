class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        #approach 1: dfs
        #approach 2: union-find/disjoint set

        #dfs

        def dfs(email, merged_emails):
            visited.add(email)

            merged_emails.append(email)

            if(email in adjacency_list):
                for neighbour in adjacency_list[email]:
                    if(neighbour not in visited):
                        dfs(neighbour, merged_emails)

            # return merged_emails

        adjacency_list = defaultdict(list)

        for account in accounts:
            name = account[0]
            first_email = account[1]
            other_emails = account[2:]
            # adjacency_list[first_email].add(first_email)
            for email in other_emails:
                # if email not in adjacency_list[first_email]:
                adjacency_list[first_email].append(email)
                adjacency_list[email].append(first_email)
        
        print(adjacency_list)
        print("\n")

        visited = set()
        merged_accounts = []

        for account in accounts:
            name = account[0]
            first_email = account[1]

            if(first_email not in visited):
                merged_emails = []
                dfs(first_email,  merged_emails)
                # print("t= ", merged_emails)
                merged_emails.sort()
                t = [name]+merged_emails
                merged_accounts.append(t)
        
        return(merged_accounts)