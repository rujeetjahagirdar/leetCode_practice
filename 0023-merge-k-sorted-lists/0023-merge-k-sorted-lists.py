# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # min_heap = []

        # for i in range(len(lists)):
        #     if(lists[i]):
        #         heapq.heappush(min_heap, (lists[i].val, i, lists[i]))

        # dummy = current = ListNode()

        # while min_heap:
        #     val, i, node = heapq.heappop(min_heap)
        #     current.next = node
        #     current = current.next

        #     if(node.next):
        #         heapq.heappush(min_heap, (node.next.val, i, node.next))
        
        # return dummy.next

        min_heap = []

        for i in range(len(lists)):
            if(lists[i]):
                curr = lists[i]
                node_counter=0
                while curr:
                    heapq.heappush(min_heap, (curr.val, i, node_counter, curr))
                    curr = curr.next
                    node_counter+=1
        
        dummy = curr = ListNode(-1)

        while min_heap:
            n = heapq.heappop(min_heap)
            curr.next = n[3]
            curr = curr.next
        
        return dummy.next