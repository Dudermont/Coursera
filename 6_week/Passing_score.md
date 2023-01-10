# Проходной балл


> Для поступления в вуз абитуриент должен предъявить результаты трех экзаменов в виде ЕГЭ, каждый из них оценивается целым числом от 0 до 100 баллов. При этом абитуриенты, набравшие менее 40 баллов (неудовлетворительную оценку) по любому экзамену из конкурса выбывают. Остальные абитуриенты участвуют в конкурсе по сумме баллов за три экзамена.
>
>В конкурсе участвует N человек, при этом количество мест равно K. Определите проходной балл, то есть такое количество баллов, что количество участников, набравших столько или больше баллов не превосходит K, а при добавлении к ним абитуриентов, набравших наибольшее количество баллов среди непринятых абитуриентов, общее число принятых абитуриентов станет больше K.

### Формат вывода

Программа получает на вход количество мест K. Далее идут строки с информацией об абитуриентах, каждая из которых состоит из имени (текстовая строка содержащая произвольное число пробелов) и трех чисел от 0 до 100, разделенных пробелами.

Используйте для ввода файл input.txt с указанием кодировки utf8 (для создания такого файла на своем компьютере в программе Notepad++ следует использовать кодировку UTF-8 без BOM).


### Формат вывода

Программа должна вывести проходной балл в конкурсе. Выведенное значение должно быть минимальным баллом, который набрал абитуриент, прошедший по конкурсу.

Также возможны две ситуации, когда проходной балл не определен.

Если будут зачислены все абитуриенты, не имеющие неудовлетворительных оценок, программа должна вывести число 0.

Если количество имеющих равный максимальный балл абитуриентов больше чем K, программа должна вывести число 1.

Используйте для вывода файл output.txt с указанием кодировки utf8.

### Предупреждение

Пожалуйста, тестируйте файловый ввод и вывод на своем компьютере. В этой задаче слушатели часто получают ошибки вроде RE на первом тесте, протестировав у себя с помощью консоли и просто заменив input() на чтение из файла перед сдачей. К сожалению, такую замену не всегда удается сделать без ошибок, и решение слушателей действительно перестает правильно работать даже на первом тесте.

 ## Примеры
>
>### Тест 1
>>*Входные данные:*
>>
>>5
>>
>>Иванов Сергей 70 70 70
>>
>>Сергеев Петр 100 100 0
>>
>>Петров Василий 70 60 70
>>
>>Васильев Андрей 70 60 70
>>
>>Андреев Денис 100 30 100
>>
>>Денисов Роман 50 50 50
>>
>>Романов Иван 60 70 70
>>
>>Ким Чен Ир 50 50 50
>>
>>Ким Ир Сен 40 40 40
> 
>>*Вывод программы:*
>>
>>200

 
>### Тест 2
>
>>*Входные данные:*
>>
>>
>>1
>>
>>Иванов Сергей 40 40 40
>>
>>Сергеев Петр 100 100 39
> 
>>*Вывод программы:*
>>
>>0
>>
>>
>>

>### Тест 3
>>
>>*Входные данные:*
>>
>>
>>1
>>
>>Иванов Сергей 60 60 60
>>
>>Сергеев Петр 100 40 40

>>*Вывод программы:*
>>
>>1