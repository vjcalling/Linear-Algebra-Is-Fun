from decimal import Decimal, getcontext
from math import acos, sqrt, pi

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(c) for c in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format([round(coord, 3)
                                    for coord in self.coordinates])

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x - y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, factor):
        return Vector([Decimal(factor) * coord for coord in self.coordinates])

    def magnitude(self):
        return Decimal(sqrt(sum([coord * coord
                                 for coord in self.coordinates])))

    def normalize(self):
        try:
            return self.times_scalar(Decimal('1.0') / self.magnitude())
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')







#==============================================================================================


if __name__ == '__main__':
    v = Vector([8.218, -9.341])
    w = Vector([-1.129, 2.111])
    addition = v.plus(w)
    print('addition: {}'.format(addition))

    v = Vector([7.119, 8.215])
    w = Vector([-8.223, 0.878])
    subtraction = v.minus(w)
    print('subtraction: {}'.format(subtraction))

    v = Vector([1.671, -1.012, -0.318])
    multiplication = v.times_scalar(7.41)
    print('multiplication: {}'.format(multiplication))

    # *****************

    v = Vector([-0.221, 7.437])
    first_magintude = v.magnitude()
    print('first_magintude: {}'.format(round(first_magintude, 3)))

    v = Vector([8.813, -1.331, -6.247])
    second_magintude = v.magnitude()
    print('second_magintude: {}'.format(round(second_magintude, 3)))

    v = Vector([5.581, -2.136])
    first_normalization = v.normalize()
    print('first_normailization: {}'.format(first_normalization))

    v = Vector([1.996, 3.108, -4.554])
    second_normalization = v.normalize()
    print('second_normailization: {}'.format(second_normalization))

    # *****************






