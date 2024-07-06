# class TrieNode:
#     def __init__(self):
#         self.child = [None] * 26
#         self.wordEnd = False
# class Trie:

#     def __init__(self):
#         self.root = TrieNode()
#         self.ansWords=[]
    
#     def insert(self, word):
#         currentNode = self.root
#         for w in word:
#             charIndex = ord(w) - ord('a')
#             if(currentNode.child[charIndex]) ==None:
#                 currentNode.child[charIndex] = TrieNode()
#             currentNode = currentNode.child[charIndex]
#         currentNode.wordEnd = True
#     def trace(self, rut):
#         currentNode= rut
#         ans=''
#         while(currentNode.wordEnd==False):
#             for i in range(len(currentNode.child)):
#                 if(currentNode.child[i]!=None):
#                     ans=''
#                     ans=ans+self.trace(currentNode.child[i])
#             self.ansWords.append(ans)
#             break
#         ans=ans + chr(ord('a')+i)
#         return ans

#     def searchSuggestions(self, word):
#         ans=[]
#         currentNode = self.root
#         for w in word:
#             charIndex = ord(w) - ord('a')
#             if(currentNode.child[charIndex]) == None:
#                 return ans
#             self.trace(currentNode)
#         print(self.ansWords)


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products=sorted(products)
        print("Products=\n",products)
        finalans=[[]]*len(searchWord)
        # obj = Trie()
        # for p in products:
        #     obj.insert(p)
        # for i in range(len(searchWord)):
        #     obj.searchSuggestions(searchWord[:i+1])
        l, r = 0, len(products)-1
        # if(len(products)==1):
        #     if(searchWord!=products[0]):
        #         return []
        for w in range(len(searchWord)):
            ans=[]
            while(l<=r):
                # if word == left word and right word
                    #return first three from left
                if((len(products[l])<=w) or (searchWord[w]!= products[l][w])):
                    l=l+1
                # if word !=right
                    #right = right -1
                elif((len(products[r])<=w) or (searchWord[w]!= products[r][w])):
                    # print(searchWord[w]+" right not matched")
                    r=r-1
                elif((searchWord[w]== products[l][w]) and (searchWord[w]== products[r][w])):
                    ans.extend(products[l:l+min(r-l+1,3)])
                    # print(ans)
                    break
                # if word!=left
                    #left = left +1
            print(ans)
            finalans[w]=ans
        # print(finalans)
        return finalans