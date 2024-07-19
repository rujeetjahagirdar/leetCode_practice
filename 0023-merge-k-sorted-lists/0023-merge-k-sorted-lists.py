# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeLL(self, l1, l2):
        dummyNode = ListNode()
        result = dummyNode
        while l1 and l2:
            if(l1.val == l2.val):
                result.next = ListNode(l1.val)
                l1 = l1.next
                result = result.next
            elif(l1.val < l2.val):
                result.next = ListNode(l1.val)
                l1 = l1.next
                result=result.next
            else:
                result.next = ListNode(l2.val)
                l2 = l2.next
                result=result.next
        if(l1):
            result.next = l1
        if(l2):
            result.next = l2
        return(dummyNode.next)
            
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if(len(lists)==0):
            return
        elif(len(lists)==1):
            # t = ListNode()
            return lists[0]
        while(len(lists)>1):
            # l1 = lists.pop(0)
            # l2 = lists.pop(0)
            # lists.insert(0, self.mergeLL(l1, l2))
            # break
            temp = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                if (i+1 < len(lists)):
                    l2 = lists[i+1]
                else:
                    l2 = None
                temp.append(self.mergeLL(l1, l2))
            lists = temp
        # print(lists)
        # print(self.mergeLL(lists[1], lists[2]))
        return lists[0]