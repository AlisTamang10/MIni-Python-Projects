elements = [5,9,2,1,67,34,88,34]

def bubblesort(elements):
     size = len(elements)
     
     for i in range(size-1):
         swapped = False
         
         for j in range (size-1-i):
            if elements[j]>elements[j+1]:
                temp = elements[j]
                elements[j] = elements[j + 1]
                elements[j+1] = temp
                
                swapped = True
                
         if not swapped:
            break
            
         
         
         
s = bubblesort(elements)
print(elements)