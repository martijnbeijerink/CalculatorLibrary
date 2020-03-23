# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:54:45 2020

@author: nlmbeij
"""

import calculator

class TestCalculator:
    def test_addition(self):
        assert 4 == calculator.add(2, 2)
        
    def test_substraction(self):
        assert 2 == calculator.substract(4, 2)