# Maximum sum such that no two elements are adjacent
numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
index2 = len ( numbers ) - 1
index1 = 0

while index1 < index2 :
    if  index1 % 2 == 1 : index1 += 1
    elif index2 % 2 == 0 : index2 -= 1
    elif ( index1 % 2 == 0 and index2 % 2 == 1 ) :
        temp = numbers [ index1 ] 
        numbers [ index1 ] = numbers [ index2 ] 
        numbers [ index2 ] = temp
        index1 += 1
        index2 -= 1
        
arr1 = numbers [ : index1 ]
arr2 = numbers [ index1 : ]
ans1 = sum ( arr1 )
ans2 = sum ( arr2 )
if ans1 > ans2 : print ( ans1 , arr1 )
else : print ( ans2 , arr2 )