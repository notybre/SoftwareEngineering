def make_special_set(lst):
    result = set()       #итоговое множество
    for i in range(len(lst)):
        num = lst[i]
        #считаем, сколько раз встречается num в списке
        count = 0
        for j in range(len(lst)):
            if lst[j] ==num:
                count+=1
        #добавляем само число
        result.add(num)
        #добавляем строки 'xx', 'xxx' и т.д. (если повторов > 1)
        k = 2
        while k<=count:
            result.add(str(num)*k)
            k+=1
    return result

list_1 = [1,1,3,3,1]
list_2 = [5,5,5,5,5,5,5]
list_3 = [2,2,1,2,2,5,6,7,1,3,2,2]

print(make_special_set(list_1))
print(make_special_set(list_2))
print(make_special_set(list_3))
