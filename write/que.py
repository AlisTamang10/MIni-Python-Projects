from collections import deque

class Qeue:
    
    def __init__(self):
        self.container = deque()
        
    def enque(self,val):
        self.container.appendleft(val)
        
    def dequee(self):
        self.container.pop()
        
    def is_empty(self):
        return len(self.container) == 0
    
    
q = Qeue()
q.enque({ 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'})
q.enque({ 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'})
q.dequee()
q.dequee()
print(q.container)