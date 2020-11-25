# Task

## Весілля та племена

Вождь Ваі-Ву з острова Пасхи вирішив поміняти традиції одруження на острові.

Раніше усі одружувались всередині свого племені.  Але після курсу біології на Coursera Ваі-Ву дізнався, що змішування генів - це корисна штука.  Тому він попросив усіх голів племен підготувати списки молодих хлопців/дівчат, і спробує організувати шлюби між племенами.

Завдання проаналізувати списки, та сказати Ваі-Ву скільки можливих пар з різних племен він може скласти.

### Формат списків племен:
Кожен юнак/дівчина - це ціле число
Юнаки - непарні числа, дівчата - парні
У кожному рядку - два числа, які означають що юнак чи дівчина належать до одного племені.  Наприклад:
	
	1 2
	2 4
	3 5

	Описує два племені - в одному є хлопець 1 та двоє дівчат 2 та 4, а в іншому племені - двоє хлопців 3 та 5.

### Вхідні дані:
	- Перший рядок містить кількість пар N
	- Наступні N рядків містять пари людей з різних племен

### Вихідні дані:
	Кількість можливих комбінацій пар таких, що хлопець і дівчина походять з різних племен.

### Обмеження:
	0 < N < 10000
### Приклади:

	In:
		3
		1 2
		2 4
		3 5
	Out:
		4 (Можливі пари - 2/3, 2/5, 4/3, 4/5)
---
	In:
		5
		1 2
		2 4
		1 3
		3 5
		8 10
	Out:
		6 (Можливі пари - 1/8, 1/10,  3/8, 3/10,  5/8, 5/10)

## Solution

#### Problem was mainly solved by using union-find algorithm

- at first step we divide all connected people into tribes using modification of union-find algorithm and fill special counter lists with girls and boys amount per tribe
- then calculate cross product of two gender counter lists to get all possible pairs
    
## How-to-use instructions
- clone repository
- open project folder in console
- do either:
    - run `python solution/main.py` in console
- or:
  - open `solution` folder
  - run `python main.py`

## Algorithm analysis

### Time complexity
O(N(N*T))
where T is amount of newly formed tribes
 
### Space complexity
O(N)
