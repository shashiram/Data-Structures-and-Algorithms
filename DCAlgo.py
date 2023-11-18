
from TrieDC3Algo import Trie

class DC3Demo:

    def main(self):
        given="monsoonnomnoms"

        t0=given

        if (len(given) +1)%3==0:
            t0=t0+'$'
        if (len(given)+2)%3==0:
            t0=t0+'$$'
        
        t1=given[1:]

        if (len(given[1:])+1)%3==0:
            t1=t1+'$'
        if (len(given[1:])+2)%3==0:
            t1=t1+'$$'
    

        t2=given[2:]

        if (len(given[2:])+1)%3==0:
            t2=t2+'$'
        elif (len(given[2:])+2)%3==0:
            t2=t2+'$$'
        else:
            t2=t2+'$$$'

        t=t1+t2

        triplesArry=[]

        i=0

        while i<len(t):
            triple=t[i:i+3]
            triplesArry.append(triple)
            i=i+3

        print(triplesArry)

        tr= Trie()
        tr.main(triplesArry)
      
        # print(tr.sortedList)

        for j in range(len(triplesArry)):

            for i in range(len(tr.sortedList)):
                if triplesArry[j]==tr.sortedList[i]:
                    triplesArry[j]=i+1
                    break

        #print(triplesArry)


        






dc3=DC3Demo()
dc3.main()

