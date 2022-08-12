##########################################################################################################################################################
## Problem: The problem is to remove the duplicates from the linked list
## Solution: So the solution is take two pointers and make 1st pointer point to first value and 2nd pointer point to second value. At each point we will 
##           check that wether the data of two pointer are equal. If they are equal then we will only increment the 2nd pointer until those values 
##           are not equal. After that in order to remove the duplicates make 1stpointer.next points to 2nd pointer which is already incremented.
###########################################################################################################################################################


##### Creating a linked list #####

class Node:
  
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
  
  
# Linked List class contains a Node object
class LinkedList:
  
    # Function to initialize head
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
  
  
# Start with the empty list
llist = LinkedList()
#Assigning Node values
llist.head = Node(1)
second = Node(1)
third = Node(3)
forth = Node(4)
fifith = Node(4)
sixth = Node(4)
seventh = Node(5)
eighth = Node(6)
ninth = Node(6)
#Assigning relations between nodes
llist.head.next = second; 
second.next = third;
third.next = forth;
forth.next = fifith;
fifith.next = sixth;
sixth.next = seventh;
seventh.next = eighth;
seventh.next = ninth;




def checkDuplicates(linked_list):
    current = linked_list.head
    while current is not None:
        next_node = current.next
        while(next_node is not None and current.data == next_node.data):
            next_node = next_node.next
        current.next = next_node
        current = next_node
    linked_list.printList()
    return linked_list
    
        

linked_list = checkDuplicates(llist)

###############################################################################################################################################################
## Time Complexity: O(n) It is because even though we have two while loops but the inner while loop doest not increase the time complexity, as we are moving to
##                  next node without going over one value twice. So we if we have moved across a node then we are not going to get back to it.
## Space Complexity: O(1) as we are updating the previous provided list.
################################################################################################################################################################
