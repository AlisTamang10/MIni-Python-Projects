
class Stack():
    def __init__(self):
        self.item = []
        
    def is_empty(self):
        return len(self.item) == 0
    
    def push(self,item):
        self.item.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            print("index is empty")
            
    def peek(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            print('satck is empty')
            
     
st = Stack()
st.push(1)
st.push(2)
st.push(3)
print(st.peek())
st.pop()
st.pop()
st.pop()
print(st.peek())
print(st.is_empty())