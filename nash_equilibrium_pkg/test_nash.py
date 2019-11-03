#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import unittest
from nash_equilibrium_pkg import nash_equilibrium


def check_matrix(game_p, v1, v2, val, vect1, vect2):
    ebs = 0.01
    if abs(val - game_p) > ebs:
        print("Error has occured in unit test with game price")
        return False
    for i in range(0, len(v1)):
        # print(v1[i]," ",vect1[i])
        if abs(v1[i] - vect1[i]) > ebs:
            print("Error has occured in unit test in checking vector 1")
            return False
        if abs(v2[i] - vect2[i]) > ebs:
            print("Error has occured in unit test in checking vector 2")
            return False
    return True


class TestNashEquilibrium(unittest.TestCase):
    def test_one(self):
        a = np.array([   #mixed strategies
            [4,0,6,2,2,1],
            [3,8,4,10,4,4],
            [1,2,6,5,0,0],
            [6,6,4,4,10,3],
            [10,4,6,4,0,9],
            [10,7,0,7,9,8]])
        vect1 = [0.0,0.12,0.09,0.43,0.33,0.0]
        vect2 = [0.0,0.0,0.69,0.14,0.14,0.01]
        val = 4.87
        game_p, v1, v2 = nash_equilibrium(a)
        self.assertTrue(check_matrix(game_p,v1,v2,val,vect1,vect2))

    def test_two(self):
        a = np.array([  #mixed strategies
            [10, 30],
            [40, 20]])
        val = 25.0
        vect1 = [0.5, 0.5]
        vect2 = [0.25, 0.75]
        game_p, v1, v2 = nash_equilibrium(a)
        self.assertTrue(check_matrix(game_p,v1,v2,val,vect1,vect2))

    def test_three(self):
        a = np.array([ #with saddle point
            [3,9,2,1],
            [7,8,5,6],
            [4,7,3,5],
            [5,6,1,7]])
        val = 5
        vect1 = [1]
        vect2 = [2]
        game_p, v1, v2 = nash_equilibrium(a)
        self.assertTrue(check_matrix(game_p,v1,v2,val,vect1,vect2))

    def test_four(self):
        a = np.array([   #with saddle point
            [2,7,2],
            [2,3,2],
            [2,1,8]])
        val = 2
        vect1 = [1]
        vect2 = [0]
        game_p, v1, v2 = nash_equilibrium(a)
        self.assertTrue(check_matrix(game_p, v1, v2, val, vect1, vect2))


if __name__ == '__main__':
    unittest.main()
