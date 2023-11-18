


class HeapSort:
    size=0
    data=[]

    def sort(self,data):
        self.size=len(data)
        self.data=data

        i=self.size-1
        while i>=0:
            self.max_heap_down(i)
            i-=1

        while(self.size>0):
            self.delete_max()

    def max_heap_down(self,index):

        left_index=2*index +1
        right_index=2*index+2

        if  not(left_index>self.size and right_index>self.size):
                max_index=index

                if left_index<self.size and self.data[left_index]>self.data[max_index]:
                    max_index=left_index
                if right_index<self.size and self.data[right_index]>self.data[max_index]:
                    max_index=right_index

                if index!=max_index:
                    tem=self.data[index]
                    self.data[index]=self.data[max_index]
                    self.data[max_index]=tem
                    self.max_heap_down(max_index)

    def delete_max(self):

        if self.size==1:
            self.size=self.size-1

        else:

            tem=self.data[0]
            self.data[0]=self.data[self.size-1]
            self.data[self.size-1]=tem
            self.size=self.size-1
            self.max_heap_down(0)

given=[4,2,4,0,0,3,0,5,1,0]
cl=HeapSort()

cl.sort(given)

print(cl.data)
            


        

