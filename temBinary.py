

class BinaryEdit:
    str_temp = '00101000010011'

    def fun(self,i,j):
       
        if i>=len(self.str_temp) and j>=len(self.str_temp):
            return 0
        if i==len(self.str_temp)-1:
            if self.str_temp[i]=='0':
                
                return 1
            else:
                return 0
        if self.str_temp[i]==self.str_temp[j]:
           
            return 1 +self.fun(j+1,j+2)
        else:
            if self.str_temp[i]=='0' and self.str_temp[j]=='1':
                return self.fun(j+1,j+2)
            else:
                return 1+self.fun(j+1,j+2)
        
    def fun1(self,i,j):

    

        if i>=len(self.str_temp) and j>=len(self.str_temp):
            return 0
        if i==len(self.str_temp)-1:
            if self.str_temp[i]=='0':
                return 0
            else:
               
                return 1

        if self.str_temp[i]==self.str_temp[j]:
           
            return 1 +self.fun1(j+1,j+2)
        else:
            
            if  (self.str_temp[i]=='1' and self.str_temp[j]=='0'):
                return self.fun1(j+1,j+2)
            else:
                return 1+self.fun1(j+1,j+2)
    
b=BinaryEdit()

min1=b.fun(0,1)
min2=b.fun1(0,1)

print(min1)
print(min2)
print(min(min1,min2))
    


    

