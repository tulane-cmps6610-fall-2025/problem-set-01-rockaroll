"""
CMPS 6610  Assignment 1.
See problemset-01.pdf for details.
"""

def foo(x,y):
    if(x==0):
        return y 
    elif(y==0):
        return x
    else:
        a,b=min(x,y),max(x,y)
        c=foo(b,b%a) 
        return c

def longest_run(mylist, key):
    counter=0
    countarr=[]
    for i in mylist:
        if(i==key):
            counter+=1
        else:
            counter=0
        countarr.append(counter)
    return max(countarr)


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size              # the length of the longest run on left side of input
                                                # eg, with a key of 12, [12 12 3] has left_size of 2 
        self.right_size = right_size            # length of longest run on right side of input
                                                # eg, key 12, [3 12 12] has right_size of 2
        self.longest_size = longest_size        # length of longest run in input
                                                # eg, [12 12 4 12 12 12]: longest_size is 3
        self.is_entire_range = is_entire_range  # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
        
def longest_run_recursive(mylist, key):
    if(len(mylist)==1 and (key in mylist)):
        return Result(1,1,1,True)
    elif(len(mylist)==1 and (key not in mylist)):
        return Result(0,0,0,False)
    elif(len(mylist)==0):
        return Result(0,0,0,False)
    elif(len(mylist)>1):
        left=mylist[:int(len(mylist)//2)]
        right=mylist[int(len(mylist)//2):]
        cleft=longest_run_recursive(left,key)
        cright=longest_run_recursive(right,key)
        is_entire=cleft.is_entire_range and cright.is_entire_range
        if cleft.is_entire_range==True:
            if right and right[0]==key:
                left_size=cleft.left_size+cright.left_size 
            else:
                left_size=cleft.left_size
        else:
            left_size=cleft.left_size
        if cright.is_entire_range==True:
            if left and left[-1]==key:
                right_size=cleft.right_size+cright.right_size 
            else:
                right_size=cright.right_size 
        else:
            right_size=cright.right_size
        cross=0
        if left and right and left[-1]==key and right[0]==key:
            cross=cleft.right_size+cright.left_size
        longest_size=max(cleft.longest_size,cright.longest_size,cross)
    return Result(left_size,right_size,longest_size,is_entire)

def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
    assert longest_run([-1,-1,-1,-1,0,2,3,5,6,1,3,1,9,9,9,10,9,9,9,9,12,12],-1) == 4
    assert longest_run_recursive([-1,-1,-1,-1,0,2,3,5,6,1,3,1,9,9,9,10,9,9,9,9,12,12],9).longest_size == 4

test_longest_run()
