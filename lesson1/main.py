# my_file = open('C:\Python_1y_15_22\semester II\my_name.txt', 'w')
# my_file.write('My name is Oleh')
# my_file.close()

# my_file = open('C:\Python_1y_15_22\semester II\my_name.txt', 'w')
# my_file.write('\nI am 14 years old')
# my_file.close()


# my_file = open('semester II\my_name.txt', 'r')
# info = my_file.read(10)
# print(info)
# my_file.close()


# my_file = open('semester II\my_name.txt', 'r')
# print(my_file.readlines()[::-1])
# inf = my_file.readlines()
# r = reversed(inf)
# print(r)
# my_file.close()

# my_file = open('semester II\my_name.txt', 'w')
# my_file.write('\nI live in Lviv')
# my_file.close()

# my_file = open('semester II\my_name.txt', 'a')
# my_file.write('\nI am from in Ukraine')
# my_file.close()

# my_file = open('semester II\my_name.txt', 'r')
# info = my_file.read()



# file = open('C:\Python_1y_15_22\lessons\semester II\lesson1\grades.csv', 'r')
# print(file.read())
# file.close()


# file = open('C:\Python_1y_15_22\lessons\semester II\lesson1\grades.csv', 'a')
# file.write('\n№5, 6, 8, 7')
# file.close()

# file = open('C:\Python_1y_15_22\lessons\semester II\lesson1\grades.csv', 'r')
# result = []
# for line in file:
#     arr = line.split(',')
#     result.append(arr)
#     print(arr)

# print(int(result[4][2]))
# file.close()

file = open('C:\Python_1y_15_22\lessons\semester II\lesson1\grades.csv', 'r')
result = []
for line in file:
    score = line.split(',')
    result.append(score)

sum_of_grades = sum(map(int, result[6][1:]))
print(sum_of_grades)
# sixth_student = result[6]
# list_of_grades = sixth_student[1:]
# b = [int(i) for i in list_of_grades]
# print(list_of_grades)
# print(b)
# print(sum(b))

file.close()
