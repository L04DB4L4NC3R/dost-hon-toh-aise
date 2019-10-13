#Program to calculate the force and torque vectors in Robotic Arm

from sympy import symbols
import numpy as np


    # <><><><><><<><><><><><>><><><><><>
    # Taking T4 as a symbol           |
    # <><><><><><<><><><><><>><><><><><>
T4 = symbols("T4")

    # <><><><><><<><><><><><>><><><><><>
    # Returns T3                      |
    # <><><><><><<><><><><><>><><><><><>
def eq3 (R34, f3, r3c3, f4, r4c3):
    # print(np.cross(f3, r3c3))
    return np.multiply(R34, T4) - np.cross(f3, r3c3) + np.cross(np.multiply(R34,f4), r4c3)

    # <><><><><><<><><><><><>><><><><><>
    # Returns T2                       |
    # <><><><><><<><><><><><>><><><><><>
def eq2 (R23, T3, f2, r22, f3, r32):
    return np.multiply(R23, T3) - np.cross(f2, r22) + np.cross(np.multiply(R23, f3), r32)

    # <><><><><><<><><><><><>><><><><><>
    # Returns T1                       |
    # <><><><><><<><><><><><>><><><><><>
def eq1 (R12, T2, f1, r1c1, f2, r2c1):
    return np.multiply(R12, T2) - np.cross(f1, r1c1) + np.cross(np.multiply(R12, f2), r2c1)



    # <><><><><><<><><><><><>><><><><><>
    # Entrypoint                       |
    # <><><><><><<><><><><><>><><><><><>
if __name__ == "__main__":

    # <><><><><><<><><><><><>><><><><><>
    # Building input                   |
    # <><><><><><<><><><><><>><><><><><>
    text = [[4, 3, 8, 9, 5, 1, 2, 7, 6], [8, 3, 4, 1, 5, 9, 6, 7, 2],
            [6, 1, 8, 7, 5, 3, 2, 9, 4], [6, 9, 8, 7, 5, 3, 2, 1, 4],
            [6, 1, 8, 7, 5, 3, 2, 1, 4], [6, 1, 3, 2, 9, 4, 8, 7, 5]]

    sample_input1 = np.array(text)
    sample_input2 = np.array( [104,105,106] )

    # 3X3 vectors
    R34 = sample_input1[0].reshape((3, 3))
    R12 = sample_input1[1].reshape((3, 3))
    R23 = sample_input1[1].reshape((3, 3))

    # 3X1 vectors
    r1c1 = sample_input2.reshape( (3, 1) )
    r2c1 = sample_input2.reshape( (3, 1) )
    r2c2 = sample_input2.reshape( (3, 1) )
    r3c2 = sample_input2.reshape( (3, 1) )
    r3c3 = sample_input2.reshape( (3, 1) )
    r4c3 = sample_input2.reshape( (3, 1) )

    # 3X1 vectors
    f1 = sample_input2.reshape( (3, 1) )
    f2 = sample_input2.reshape( (3, 1) )
    f3 = sample_input2.reshape( (3, 1) )
    f4 = sample_input2.reshape( (3, 1) )

    # <><><><><><<><><><><><>><><><><><>
    # Solving equations in terms of T4 |
    # <><><><><><<><><><><><>><><><><><>
    T3 = eq3(R34, f3, r3c3, f4, r4c3)
    T2 = eq2(R23, T3, f2, r2c2, f3,r3c2)
    T1 = eq1(R12, T2, f1, r1ci, f2, r2c1)

    print(T1, T2, T3)
