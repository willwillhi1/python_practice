#list
ls1 = []
ls2 = []
ls1.append(element)
ls1.extend(ls2)
ls1.insert(index, element)
del ls1[index]
ls1.remove(element_name)
ls1.index(element_name) #return element's index
element in ls1 #return true if in list
ls1.count(element) #return num of element
ls1.join(sep) #combine the element by sep
ls2 = sorted(ls1)
len(ls1)
ls2 = ls1.copy()

#tuple
#can not change any element in tuple!
tp1 = ("hello", 95)
#unpacking
a,b = tp1
# >>> a
# hello
# >>> b
# 95

#dict //Key need hashable
dic = {'integer': 1, 'bool': False, 3.14: 3.14}
# >>> dic['integer']
# 1
# >>> dic[3.14]
# >>> 3.14
dic['integer'] = 2

#use list/tuple to create dict
ls = ['a1', 'b2', 'c3']
dictls = dict(ls)
# >>> dictls
# {'a': 1, 'b': 2, 'c':3}
tp = (['a', 1], ['b', 2], ['c', 3])
dicttp = dict(tp)
# >>> dictls
# {'a': 1, 'b': 2, 'c':3}

dict1.update(dict2)
del dict1['key']
dict1.clear()
Key in dict1 #return true if Key in dict1
dict1.keys() #return all key in dict1
dict1.values() #return all value in dict1
dict1.items() #return all key:value in dict1
dict2 = dict1.copy()
