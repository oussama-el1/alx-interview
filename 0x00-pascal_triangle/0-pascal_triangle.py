#!/usr/bin/python3
"""
Create a function def pascal_triangle(n): that returns a list of lists of
  integers representing the Pascal’s triangle of n:

- Returns an empty list if n <= 0
- You can assume n will be always an integer
"""

def pascal_triangle(n):
  """ function create a pascal triangle with 'n' row"""
  
  if n <= 0:
      return []
  
  triangle = []
  for i in range(n):
    row = [1]
    j = 1
    for j in range(1, i + 1):
      if j == i:
        row.append(1)
      else:
        row.append(triangle[i - 1][j] + triangle[i - 1][j - 1])
    triangle.append(row)

  return triangle