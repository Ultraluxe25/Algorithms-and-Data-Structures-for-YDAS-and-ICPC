"""
876. Middle of the Linked List
Solved 20.05.2024
Easy

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 
Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.


Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 
Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""

# Solution 1 (Brute force)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []

        counter = head
        while counter is not None:
            values.append(counter.val)
            counter = counter.next

        n = len(values)
        second_middle_node = values[n//2:]

        result_list = ListNode(second_middle_node[0])
        current = result_list
        for i in second_middle_node[1:]:
            current.next = ListNode(i)
            current = current.next

        return result_list
