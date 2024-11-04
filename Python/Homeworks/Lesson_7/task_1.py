from functools import reduce

# Исходные списки
floats = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names=["Vanes","Alen","Jana","William","Richards","Joy"]
numbers=[22,33,10,6894,11,2,1]

#Применяемфункциюmapдлявозведениявтретьюстепеньиокругления дотрехзнаковпослезапятой
map_result=list(map(lambdax:round(x**3,3),floats))

#Применяемфункциюfilterдлявыбораименизпятииболеебукв
filter_result=list(filter(lambdaname:len(name)>=5,names))

#Применяемфункциюreduceдлянахожденияпроизведениявсехчисел в списке
reduce_result=reduce(lambdanum1,num2:num1*num2,numbers)

#Выводрезультатов
print(map_result)
print(filter_result)
print(reduce_result)