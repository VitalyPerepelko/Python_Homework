#Task2
#VitalyPerepelko

max_val = 3
odd_nums_gen = (n for n in range(1, max_val + 1, 2))
print(next(odd_nums_gen))

#Task3

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей',
          'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

gen = ((tutor, klass) for tutor, klass in zip(tutors, klasses))
print(next(gen))

from itertools import zip_longest

gen = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses))
print(next(gen))


#Task4

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [num for i, num in enumerate(src) if num > src[i - 1] and i != 0]
print(new_list)


#Task5
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([x for x in src if src.count(x) == 1])
