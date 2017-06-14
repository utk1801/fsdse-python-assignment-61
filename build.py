def solution(list_of_nums):
    d={}
    count_even=[x for x in list_of_nums if x%2==0]
    count_odd=[x for x in list_of_nums if x%2==1]
    d['ODD']=len(count_odd)
    d['EVEN']=len(count_even)
    return d
print solution([1, 2, 3, 5, 8, 9])
