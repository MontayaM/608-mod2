values = [13, 16, 14, 18, 13, 10, 15, 15, 22, 9, 18, 18, 13, 17, 14, 10, 18, 16, 15, 18, 12, 16, 13, 12, 12, 9, 13, 17, 14, 13, 25, 16, 20, 23, 15, 10, 23, 14, 16, 18, 19, 22, 13, 16, 20, 16, 15, 12, 12, 13, 17, 15, 18, 13, 13, 17, 15, 15, 20, 15, 13, 16, 14, 18, 15, 15, 19, 17, 16, 21, 17, 20, 19, 14, 16, 16, 17, 19, 17, 23, 14, 20, 17, 13, 15, 21, 21, 23, 17, 22, 9, 11, 21, 12, 20, 15, 22, 15, 20, 15]
Count=(values).count(12)

print('1. The Count of 12 values = ',(Count) )

Sum= sum(values)
print ('2. The Sum of values = ', (Sum)   ) 

mean = sum(values) / len(values)

print ('3. The MEAN of values = ', round(mean, 2)   )
 




def mean(list_of_nums):
    total=0 
    for num in list_of_nums:
        total=total+num
    return total/len(list_of_nums)


print ('3. The Mean of values = ',mean([13, 16, 14, 18, 13, 10, 15, 15, 22, 9, 18, 18, 13, 17, 14, 10, 18, 16, 15, 18, 12, 16, 13, 12, 12, 9, 13, 17, 14, 13, 25, 16, 20, 23, 15, 10, 23, 14, 16, 18, 19, 22, 13, 16, 20, 16, 15, 12, 12, 13, 17, 15, 18, 13, 13, 17, 15, 15, 20, 15, 13, 16, 14, 18, 15, 15, 19, 17, 16, 21, 17, 20, 19, 14, 16, 16, 17, 19, 17, 23, 14, 20, 17, 13, 15, 21, 21, 23, 17, 22, 9, 11, 21, 12, 20, 15, 22, 15, 20, 15])  )  


    
def median(L):
    L.sort()
    if len(L)%2 !=0:
        median= L[int(len(L)/(2))]
    else:
                      median= L[(int(len(L)/2))-1] + L[int(len(L)/2)]
                      median=median/2
    return median


print ('4. The Median of values = ',median([13, 16, 14, 18, 13, 10, 15, 15, 22, 9, 18, 18, 13, 17, 14, 10, 18, 16, 15, 18, 12, 16, 13, 12, 12, 9, 13, 17, 14, 13, 25, 16, 20, 23, 15, 10, 23, 14, 16, 18, 19, 22, 13, 16, 20, 16, 15, 12, 12, 13, 17, 15, 18, 13, 13, 17, 15, 15, 20, 15, 13, 16, 14, 18, 15, 15, 19, 17, 16, 21, 17, 20, 19, 14, 16, 16, 17, 19, 17, 23, 14, 20, 17, 13, 15, 21, 21, 23, 17, 22, 9, 11, 21, 12, 20, 15, 22, 15, 20, 15]))  






def mode(list_of_nums):
    max_count=(0,0)
    for num in list_of_nums:
        occurences = list_of_nums.count(num)
        if occurences > max_count[0]:
            max_count = (occurences, num)
    return max_count[1]


print ('5. The Mode of values = ', mode([13, 16, 14, 18, 13, 10, 15, 15, 22, 9, 18, 18, 13, 17, 14, 10, 18, 16, 15, 18, 12, 16, 13, 12, 12, 9, 13, 17, 14, 13, 25, 16, 20, 23, 15, 10, 23, 14, 16, 18, 19, 22, 13, 16, 20, 16, 15, 12, 12, 13, 17, 15, 18, 13, 13, 17, 15, 15, 20, 15, 13, 16, 14, 18, 15, 15, 19, 17, 16, 21, 17, 20, 19, 14, 16, 16, 17, 19, 17, 23, 14, 20, 17, 13, 15, 21, 21, 23, 17, 22, 9, 11, 21, 12, 20, 15, 22, 15, 20, 15]))  
