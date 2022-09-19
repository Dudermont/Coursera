# Быстрое возведение в степень

>Возводить в степень можно гораздо быстрее, чем за n умножений! Для этого нужно воспользоваться следующими рекуррентными соотношениями: aⁿ = (a²)ⁿ/² при четном n, aⁿ=a⋅aⁿ⁻¹ при нечетном n. Реализуйте алгоритм быстрого возведения в степень. Если вы все сделаете правильно,то сложность вашего алгоритма будет O(logn).


## Формат ввода

Вводится действительное число a и целое неотрицательное число n.

## Формат вывода

Выведите ответ на задачу.


 ## Примеры
>
>### **Тест 1**
>
>>*Входные данные:*
>>
>> 2
>>
>> 1
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
>> 2
> 

>### Тест 2
>
>>*Входные данные:*
>>
>> 
>>
>> 
>> 2
>> 
>>
>> 2
>>
>> 
>>
>> 
> 
>>*Вывод программы:*
>>
>> 4
> 
> 
> >### Тест 3
>
>>*Входные данные:*
>>
>> 2
>>
>> 
>> 3
>> 
>> 
>>
>> 
>>
>> 
> 
>>*Вывод программы:*
>>
>>8