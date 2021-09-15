import math


def area_of_tetrahedron(side):
    return (math.sqrt(3) *
            (side * side))


def area_of_cube(length, width, height):
    volume = length * width * height
    return (volume)


print("välja en form")
print("1. en kub ")
print("2. tetrahedron")

try:
    shape = int(input())
    if shape == 1:
        length = float(input('Ange längden på en kuboid i cm '))
        width = float(input('Ange bredden på en kuboid i cm '))
        height = float(input('Ange1 höjden på en kuboid i cm '))
        print("yta av kub = ",
              area_of_cube(length, width, height), "cm")

    if shape == 2:
        side = float(input('Ange liksidig  på en tetrahedron i cm '))
        print("yta av tetrahedron = ",
              round(area_of_tetrahedron(side), 4))

except:
    print("det finns ett fel med input type")
