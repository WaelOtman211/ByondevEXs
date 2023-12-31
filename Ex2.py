# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""




class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
 
    # Method to add a node at begin of LL
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
 
    # Method to add a node at any index
    # Indexing starts from 0.
    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")
 
    # Method to add a node at the end of LL
 
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
 
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
 
        current_node.next = new_node
 
    # Update node of a linked list
        # at given position
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")
 
    # Method to remove first node of linked list
 
    def remove_first_node(self):
        if(self.head == None):
            return
 
        self.head = self.head.next
 
    # Method to remove last node of linked list
    def remove_last_node(self):
 
        if self.head is None:
            return
 
        current_node = self.head
        while(current_node.next.next):
            current_node = current_node.next
 
        current_node.next = None
 
    # Method to remove at given index
    def remove_at_index(self, index):
        if self.head == None:
            return
 
        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")
 
    # Method to remove a node from linked list
    def remove_node(self, data):
        current_node = self.head
 
        while(current_node != None and current_node.next.data != data):
            current_node = current_node.next
 
        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next
 
    # Print the size of linked list
    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0
 
    # print method for the linked list
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next
            
    def getNodeValueFromEnd(self):
        current_node = self.head
        while(current_node.next != None):
            current_node=current_node.next
        
        return current_node.data 
    
    def ReverseList(self):
        sizeOfLL=self.sizeOfLL()
        j=0
        for i in range(0, sizeOfLL-1):
            data=self.getNodeValueFromEnd()
            self.remove_last_node()
            self.insertAtIndex(data,j)
            j=j+1
        return self   
         
    def FindMiddle(self):     
        current_node = self.head
        i=0
        sizeOfLL=self.sizeOfLL()
        while(i != int(sizeOfLL/2)):
            current_node = current_node.next
            i=i+1
        return current_node.data    
    
    def insertCycleNode(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
 
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        current_node.next = new_node
        current_node.next.next = self.head
     
    def getHead(self):
        return self.head
        
      
        
    def checkIfCycleList(self):
          head = self.getHead()
          current_node =self.getHead().next
    
          while(current_node != head and current_node != None):
            current_node = current_node.next
          return current_node != None




def main() :
    
    # create a new linked list
    llist = LinkedList()
    llistCycle=LinkedList()
    # add nodes to the linked list
    llist.insertAtEnd('a')
    llist.insertAtEnd('b')
    llist.insertAtBegin('c')
    llist.insertAtEnd('d')
    llist.insertAtIndex('g', 2)
    
    
    # print the linked list
    llist.printLL()
    print("revers list is :")
    llist=llist.ReverseList()
    llist.printLL()
    
    print("the middle element is :")
    data =llist.FindMiddle()
    print(data)
   
    
   # add nodes to the linked list
    llistCycle.insertAtEnd('a')
    llistCycle.insertAtEnd('b')
    llistCycle.insertAtBegin('c')
    llistCycle.insertAtEnd('d')
    llistCycle.insertAtIndex('g', 2)
    llistCycle.insertCycleNode('z')
    print("check llistCycle if it is a cycle :")
    print(llistCycle.checkIfCycleList())
    print("check llist if it is a cycle :")
    print(llist.checkIfCycleList())
    
    
if __name__ == "__main__":
    main()
 
    
        
