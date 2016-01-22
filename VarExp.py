'''
Created on 8. 1. 2016

@author: ppavlu
'''
import sys, requests, json

'''
TESTCTRLURL="https://sandboxapic.cisco.com:9443/api/v1/"
TESTUSERNAME="admin"
TESTPASSWORD="1vtG@lw@y"
GET="get"
POST="post"
'''

# Function to swap values
def swap(a,l,r):
    t = a[l]
    a[l] = a[r]
    a[r] = t
    return a
 
def toList(string):
    List = []
    for x in string:
        List.append(x)
    return List
 
def toString(List):
    return ''.join(List)
 
# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
    if (l==r):
        print (toString(a))
    else:
        for i in range(l,r+1):
            a = swap(a,l,i)
            permute(a, l+1, r)
            a = swap(a,l,i) # backtrack
 
def combine (Seznam, StartList, Left, Right, Ntice, Tot):
    WorkList=[]
    #print("Jsme v combine, StartList je ", StartList)
    #print("Ntice= ",Ntice, " Left=",Left," Right=",Right)
    if Ntice==1:
        #print("Ntice=1 Left=",Left," Right=",Right)
        #print(Seznam,"---", StartList)
        for i in range(Left, Right+1):
            WorkList=StartList.copy()
            WorkList.append(Seznam[i])
            #print("WorkList: ",WorkList, "StartList: ", StartList)
            #WorkList=StartList.append(Seznam[i])
            if len(WorkList)==Tot:
                print(toString(WorkList))
    else:
        #print("rekurze")
        #print("Worklist pred je ",WorkList)
        for i in range (Left, Right+1):
            WorkList=StartList.copy()
            WorkList.append(Seznam[i])
        #WorkList=StartList.append(Seznam[Left])
        #print("Worklist po je ",WorkList)
        #if ((len(WorkList)+Right-Left)>=Tot):
            combine(Seznam, WorkList,i+1, Right, Ntice-1,Tot)
            #if (Right-i)>=Ntice:
                #combine(Seznam, [], i+1, Right, Ntice,Tot)

def main():
    #string = "abcde"
    string=input("String to play with: ")
    ntice=int (input("Group size for combinations: "))
    #ntice=4
    n = len(string)
    a = toList(string)
    print ("Permutations:")
    permute(a, 0, n-1)
    print ("Combinations of ",ntice," prvku:")
    combine(a,[],0,n-1,ntice,ntice)

if __name__ == "__main__":
    main()
    