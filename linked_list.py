# create node
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# create linked list 
class linked_list:
    def __init__(self):
        self.head = node()
        
    # insert at end
    def insert_at_end(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    
    # get length
    def get_length(self):
        cur = self.head
        total = 0
        while(cur != None):
            print(cur.data)
            cur = cur.next
            total+=1
        print(total)
    
    # display elements
    def display_elements(self):
        elements = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elements.append(cur.data)
        print(elements)
        
    # getting element by index 
    def get_element(self, index):
        # if index >= self.length():
        #     print(f'Error: you must give a valid length')
        #     return None
        cur_index = 0
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            if cur_index == index: return cur_node.data
            cur_index += 1
            
    # deleted element and mapped to next one 
    def delete_element(self, index):
        cur_index = 0
        cur_node = self.head
        while cur_node.next != None:
            prev_node = cur_node
            cur_node = cur_node.next
            if cur_index == index:
                prev_node.next = cur_node.next
                return
            cur_index += 1

# driver code
if __name__ == "__main__":
    # creating instances and invoking methods
    list = linked_list()
    list.insert_at_end(1)
    list.insert_at_end(2)
    list.insert_at_end(3)
    list.insert_at_end(4)
    list.display_elements()
    list.delete_element(2)
    list.display_elements()
    
