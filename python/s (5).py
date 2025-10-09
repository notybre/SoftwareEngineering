from collections import Counter
from typing import List,Tuple

def elements_with_count_two(lst: List[int]) -> Tuple[int, ...]:
    counts=Counter(lst)
    seen=set()
    result=[]
    for x in lst:
        if counts[x]==2 and x not in seen:
            result.append(x)
            seen.add(x)
    return tuple(result)

if __name__=='__main__':
    print(elements_with_count_two([1,2,3,2,4,1,5])) 
    print(elements_with_count_two([7,7,7,7]))      
    print(elements_with_count_two([9,8,9,8,7,7]))  
