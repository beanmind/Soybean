

class Fruit(object):
    pass


class Banana(Fruit):   # Banana inherits from (or extends) Fruit
    colour = 'yellow'   # colour is a class attribute

    def __init__(self, name_of_this_banana, size=10):   # __init__ is the constructor
        # name is a positional argument to the constructor
        # size is a keyword argument

        # defining an attribute 'name' on this instance of 'Banana' whose value is the argument 'name'
        self.name = name_of_this_banana
        self.size = size

    def bite(self):
        pass

b = Banana('fish')
# b is a new instance of Banana. You are calling the constructor with the argument 'fish'
# you are creating a new instance of Banana and assigning it the variable name 'b'
b.bite()
# calling the method 'bite' on b, which is an instance of banana

a = [1, 2, 3, 4]
# a is a list
x = 2
c = a[x]
# c is now the element of the list a at index x

a[1:]  # this is a slice


def lala(a, b, c=3, d='arse'):
    print a, b, c, d

lala(1, 2, 'banana')


if __name__ == '__main__':
    print 'hello'

import csv as csv
import numpy as np

csv_file_object = csv.reader(open('csv/train.csv', 'rb'))
header = csv_file_object.next()
data=[]

for row in csv_file_object:
    data.append(row)
data = np.array(data)

for i in range(0, 2):
    for j in range(0, 3):
        median_age[i,j] = df[(df['Gender'] == i) & \
                              (df['Pclass'] == j+1)]['AgeFill'].dropna().median()

median_age



for i in range(0, 2):
    for j in range(0, 3):
        df.loc[ (df.Age.isnull()) & (df.Gender == i) & (df.Pclass == j+1),'AgeFill'] = median_age[i,j]



csv_file_object = csv.reader(open('csv/test.csv', 'rb'))
header = csv_file_object.next()
data2=[]
for row in csv_file_object:
    data2.append(row)
data2 = np.array(data2)

#males in classes

for i in range(1,4):
    print i, len(df[ (df['Sex'] == 'male') & (df['Pclass'] == i) ])


for i in range(1,4):
    print i, len(df[ (df['Sex'] == 'male') & (df['Pclass'] == i)& (df['Survived']==1) ])


