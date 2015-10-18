__author__ = 'pather'


# Question 9
# Function Real average(Real values[], Integer size)
# Declare Real total = 0.0
# 		Declare Integer counter = 0
#
# 		While counter < size
# 			Set total = total + values[counter]
# 			Set counter = counter + 1
# 		End While
#
# 		Return total / size
# 	End Function
#
# 	Declare Real scores[6] = 90, 80, 70, 100, 60, 80
# 	Display average(scores, 6)

#
# def average(values, size):
#     total = 0
#     counter = 0
#
#     while counter < size:
#         total = total + values[counter]
#         counter += 1
#     return total / size
#
#
# scores = [90, 80, 70, 100, 60, 80]
# print(average(scores, 6))


# def main():
#
#     returns = aveage(scores, 6)
####################################################################

# Question 10

# Function Real getScore(String student, String names[], Real scores[], Integer size)
# 		Declare Integer counter = 0
#
# 		While counter < size
# 			If student = names[counter] Then
# 				Return scores[counter]
# 			End If
# 			Set counter = counter + 1
# 		End While
# 		Return -1
# 	End Function
#
# 	Declare String names[5] = "John", "Paul", "George", "Ringo", "Pete"
# 	Declare Real scores[5] = 100, 80, 90, 70, 50
#
# 	Display getScore("George", names, scores, 5)


# names = ['john', 'paul', 'george', 'ringo', 'pete']
# scores = [100, 80, 90, 70, 50]


def get_score(student, name, scores, size):
    counter = 0

    while counter < size:
        if student = name[counter]:
            return scores[counter]
        else:
            counter += 1
    return - 1


def main():
    name = ['john', 'paul', 'george', 'ringo', 'pete']
    scores = [100, 80, 90, 70, 50]

    print(get_score('george', name, scores, 5))

main()


#########################################################################33333
 # Question 11

# Module getStats(Real scores[], Integer size)
#  	Declare Integer counter = 0
# 	Declare Real min = 100
# 	Declare Real max = 0
# 	Declare Real total = 0
#
# 	While counter < size
# 		If scores[counter] > max Then
# 			Set max = scores[counter]
#  		End If
# 		If scores[counter] < min Then
# 			Set min = scores[counter]
# 		End If
# 		Set total = total + scores[counter]
#  		Set counter = counter + 1
# 	End While
# 	Display min, max, total / counter
# End Function
#
# Declare Real scores[5] = 100, 80, 90, 70, 50
#
# Display getStats(scores, 5)
# scores = [100, 80, 90, 70, 50]
#
#
# def get_stats(scores, size):
#     counter = 0
#     min1 = 100
#     max1 = 0
#     total = 0
#
#     while counter < size:
#         if scores[counter] > max1:
#             max1 = scores[counter]
#
#         if scores[counter] < min1:
#             min1 = scores[counter]
#
#         total += scores[counter]
#         counter += 1
#     print(min1, max1, total / counter)
#
#
# print(get_stats(scores, 5))

###############################################################################
# Question 12


# Function Real[] fibo(Integer n)
# 		Declare Integer vals[n]
# 		Declare Integer counter = 2
#
# 		Set vals[0] = 1
# 		Set vals[1] = 1
# 		While counter < n
# 			Set vals[counter] = vals[counter - 1] + vals[counter - 2]
# 			Set counter = counter + 1
# 		End While
#
# 		Return vals
# 	End Function
#
# 	Module output_vals(Integer vals[], Integer n)
# 		Declare Integer counter = 0
#
# 		While counter < n
# 			Display vals[counter]
# 			Set counter = counter + 1
# 		End While
# 	End Module
#
# 	Module main(Integer n)
# 		Declare Integer vals[n] = fibo(n)
# 		Call output_vals(vals, n)
# 	End Module

# def fibo(n):
#     vals = [n]
#     counter = 2
#     print(vals)
#     # vals[0] = 1
#     # vals[1] = 1
#     vals[0:2] = [1, 1]
#     while counter < n:
#         vals[counter] = vals[counter - 1] + vals[counter - 2]
#         counter += 1
#     return vals
#
#
# def out_put(vals, n):
#     counter = 0
#
#     while counter < n:
#         print(vals[counter])
#         counter += 1
#
# def main(n):
#     # vals = vals[n]
#     vals = fibo(8)
#     out_put(vals, n)
# main(8)

###################################################################
# Question 13

# Class Coordinate
# 		Private Real _x
# 		Private Real _y
#
# 		Public Module set_x(Real value)
# 			Set _x = value
# 		End Module
#
# 		Public Module set_y(Real value)
# 			Set _y = value
# 		End Module
#
# 		Public Function get_x()
# 			Return _x
# 		End Module
#
# 		Public Function get_y()
# 			Return _y
# 		End Module
#
# 		Public Module add(Coordinate c)
# 			Set _x = _x + c.get_x()
# 			Set _y = _y + c.get_y()
# 		End Module
# 	End Class
#
# 	Module main()
# 		Declare Coordinate c1 = New Coordinate()
# 		Declare Coordinate c2 = New Coordinate()
#
# 		Call c1.set_x(1.0)
# 		Call c1.set_y(2.0)
# 		Call c2.set_x(3.0)
# 		Call c2.set_y(4.0)
#
# 		Display c1.get_x(), c1.get_y(), c2.get_x(), c2.get_y()
#
# 		Call c1.add(c2)
#
# 		Display c1.get_x(), c1.get_y(), c2.get_x(), c2.get_y()
# 	End Module

# class Coordinate:
#     _x = 0
#     _y = 0
#     print('step 1')
#
#     def set_x(self, value):
#         print('step 2')
#         self._x = value
#
#     def set_y(self, value):
#         self._y = value
#
#     def get_x(self):
#         return self._x
#
#     def get_y(self):
#         return self._y
#
#     def add(self, c):
#         self._x = self._x + c.get_x()
#         self._y = self._y + c.get_y()
#
#
# def main():
#     c1 = Coordinate()
#     c2 = Coordinate()
#
#     c1.set_x(1.0)
#     c1.set_y(2.0)
#     c2.set_x(3.0)
#     c2.set_y(4.0)
#
#     print(c1.get_x(), c1.get_y(), c2.get_x(), c2.get_y())
#
#     c1.add(c2)
#
#     print(c1.get_x(), c1.get_y(), c2.get_x(), c2.get_y())

#
# 		Public Module set_x(Real value)
# 			Set _x = value
# 		End Module
#
# 		Public Module set_y(Real value)
# 			Set _y = value
# 		End Module
#
# 		Public Function get_x()
# 			Return _x
# 		End Module
#
# 		Public Function get_y()
# 			Return _y
# 		End Module
#
# 		Public Module add(Coordinate c)
# 			Set _x = _x + c.get_x()
# 			Set _y = _y + c.get_y()
# 		End Module
# 	End Class

#######################################################################3333
#   Question 14

# Class Animal
# 	Private String _name
#
# 	Public Module setName(String name)
# 		Set _name = name
# 	End Module
#
# 	Public Module vocalize()
# 		Display _name + " makes a noise."
# 	End Module
# End Class
#
# Class Dog Extends Animal
# 	Public Module vocalize()
# 		Display _name + " woofs."
# 	End Module
# End Class
#
# Class Cat Extends Animal
# 	Public Module vocalize()
# 		Display _name + " meows."
# 	End Module
# End Class
#
# Class Bird Extends Animal
# 	Public Module vocalize()
# 		Display _name + " chirps."
# 	End Module
# End Class
#
# Module main()
# 	Declare Animal pets[3]
# 	Declare Integer counter = 0
#
# 	Set pets[0] = New Dog()
# 	Set pets[1] = New Cat()
# 	Set pets[2] = New Bird()
# 	Call pets[0].setName("Dorothy")
# 	Call pets[1].setName("Ginger")
# 	Call pets[2].setName("Ralph")
# 	While counter < 3
# 		Call pets[counter].vocalize()
# 		counter = counter + 1
# 	End While
# End Module

# class Animal:
#     _name = ''
#
#     def set_name(self, name):
#         self._name = name
#
#     def vocalize(self):
#         print(self._name, 'makes noise')
#
#
# class Dog:
#
#     def vocalize(self):
#         print(self._name, 'woof')
#
#
# class Cat:
#
#     def vocalize(self):
#         print(self._name, 'meows')
#
#
# class Brid:
#
#     def vocalize(self):
#         print(self._name, 'chrips')
#
# def main():
#     pets = []
#  	counter = 0
#     pets[0] = Dog()
#     pets[0] = Cat()
#     pets[0] = Brid()

#################################################################################
#   Question 15
# Class Musician
# 		Private String _name
# 		Private Integer _rating
# 		Private String _song
#
# 		Public Module Musician(String name, Integer rating, String song)
# 			Set _name = name
# 			Set _rating = rating
# 			Set _song = song
# 		End Module
#
# 		Public Module display()
# 			Display name, rating, song
# 		End Module
#
# 		Public Function Boolean matches(String name)
# 			Return name == _name
# 		End Function
# 	End Class
#
# 	Module main(String name)
# 		Declare Musician musicians[4]
# 		Declare Integer counter = 0
#
# 		Set musicians[0] = New Musician("John", 10, "Imagine")
# 		Set musicians[1] = New Musician("Paul", 9, "Listen to What the Man Said")
# 		Set musicians[2] = New Musician("George", 8, "Here Comes the Sun")
# 		Set musicians[3] = New Musician("Ringo", 7, "With a Little Help From My Friends")
#
# 		While counter < 4
# 			If musicians[counter].matches(name) Then
# 				Call musicians[counter].display()
# 			End If
# 			counter = counter + 1
# 		End While
# 	End Module


#####################################################################

#   Question 16

# Class Material
# 		Private String _type
#
# 		Public Module Material(String type)
# 			_type = type
# 		End Module
#
# 		Public Module display()
# 			Display _type
# 		End Module
# 	End Class
#
# 	Class Furniture
# 		Private Material _material
# 		Private String _type
#
# 		Public Module set_material(Material material)
# 			_material = material
# 		End Module
#
# 		Public Module display()
# 			Display _type
# 			Call _material.display()
# 		End Module
# 	End Class
#
# 	Class Chair Extends Furniture
# 		Public Module Chair()
# 			Set _type = "Chair"
# 		End Module
# 	End Class
#
# 	Module main()
# 		Declare Furniture furniture = New Chair()
#
# 		Call furniture.set_material(New Material("Wood"))
# 		Call furniture.display()
# 	End Module