# Слияние списков


>Даны два целочисленных списка A и B, упорядоченных по неубыванию. Объедините их в один упорядоченный список С (то есть он должен содержать len(A)+len(B) элементов). Решение оформите в виде функции merge(A, B), возвращающей новый список. Алгоритм должен иметь сложность O(len(A)+len(B)). Модифицировать исходные списки запрещается. Использовать функцию sorted и метод sort запрещается.


## Формат ввода

Программа получает на вход два неубывающих списка, каждый в отдельной строке.

## Формат вывода

Программа должна вывести последовательность неубывающих чисел, полученных объединением двух данных списков.


 ## Примеры
>
> >### Тест 1
>
>>*Входные данные:*
>>
>>1 5 7
>>
>>2 4 4 5
>>
>>
>>
>>
>>
>>
>>
>> 
> 
>>*Вывод программы:*
>>
>>1 2 4 4 5 5 7

>>

 
>### Тест 2
>
>>*Входные данные:*
>>
>>
>>1 4 7
>>
>>1 5 6
>>
>>
>>
>>
>>
>> 
>>
>>
>>
>>
>>
>
>>*Вывод программы:*
>>
>>1 1 4 5 6 7 

>### Тест 3
>>
>>*Входные данные:*
>>
>>
>>
>>1
>>
>>1
>> 
>>
>> 
>>
>>
>>

>>*Вывод программы:*
>>
>>1 1
>>
>>