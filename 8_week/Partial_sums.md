# Частичные суммы

>По заданной последовательности:
>
>(a₁,…,an)
>
>посчитайте последовательность частичных сумм:
>
>(S₁,…,Sn),
>
>где Sk=a₁+a₂+…+ak.

## Формат ввода

Вводится последовательность чисел (a₁,…,an), разделённая пробелами.

## Формат вывода

Выведите последовательность (S₁,…,Sn), разделяя числа пробелами.

## Примечания

Для решения задачи можно воспользоваться функцией accumulate из модуля itertools.

 ## Примеры
>
>>### Тест 1
> 
>>*Входные данные:*
>>
>>1 2 3 4 5 6 7
>
>>*Вывод программы:*
>>
>>1 3 6 10 15 21 28

 
>### Тест 2
>
>>*Входные данные:*
>>
>>
>>1 9 5 2
> 
>>*Вывод программы:*
>>
>>1 10 15 17
>>
>>

>### Тест 3
>>
>>*Входные данные:*
>>
>>100000000000
>
>>*Вывод программы:*
>>
>>100000000000