def mean(list_of_nums):
    total=0 
    for num in list_of_nums:
        total=total+num
    return total/len(list_of_nums)


print ('3. The Mean of values = ',mean([47, 95,88, 73,88, 84]))  


def mode(list_of_nums):
    max_count=(0,0)
    for num in list_of_nums:
        occurences = list_of_nums.count(num)
        if occurences > max_count[0]:
            max_count = (occurences, num)
    return max_count[1]


print ('5. The Mode of values = ', mode([47, 95,88, 73,88, 84]))  


values = [47, 95,88, 73,88, 84]
Count=(values).count(88)

print('1. The Count of 88 values = ',(Count) )

Sum= sum(values)
print ('2. The Sum of values = ', (Sum)   ) 

mean = sum(values) / len(values)
print ('3. The MEAN of values = ', round(mean, 2)   )
 

    
def median(L):
    L.sort()
    if len(L)%2 !=0:
        median= L[int(len(L)/(2))]
    else:
                      median= L[(int(len(L)/2))-1] + L[int(len(L)/2)]
                      median=median/2
    return median


print ('4. The Median of values = ',median([47, 95,88, 73,88, 84]))  


