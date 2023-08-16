#!/usr/bin/bash
# 0-square_matrix_simple.py

def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    new_matrix = (x**2 for x in (new_matrix))
    return (new_matrix)
