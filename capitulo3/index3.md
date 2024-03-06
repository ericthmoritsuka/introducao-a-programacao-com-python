# Capitulo 3 - Exercicios

- 3.1

   [3.1, 3.2, 3.3 - Checking Answers](3.1-3.2-3.3.py)


   | Number |   Type    |
   |:------:|:---------:|
   |   5    | `integer` |
   |  5.0   |  `float`  |
   |  4.3   |  `float`  |
   |   -2   | `integer` |
   |  100   | `integer` |
   | 1.333  |  `float`  |

- 3.2

  [3.1, 3.2, 3.3 - Checking Answers](3.1-3.2-3.3.py)

  a = 4, b = 10, c = 5.0, d = 1 e f = 5

  | Operation | &rarr; | Answer  |
  |:---------:|:------:|:-------:|
  |  a == c   | &rarr; | `False` |
  |   a < b   | &rarr; | `True`  |
  |   d > b   | &rarr; | `False` |
  |  c != f   | &rarr; | `False` |
  |  a == b   | &rarr; | `False` |
  |   c < d   | &rarr; | `False` |
  |   b > a   | &rarr; | `True`  |
  |  c >= f   | &rarr; | `True`  |
  |  f >= c   | &rarr; | `True`  |
  |  c <= c   | &rarr; | `True`  |
  |  c <= f   | &rarr; | `True`  |

- 3.3

  [3.1, 3.2, 3.3 - Checking Answers](3.1-3.2-3.3.py)

  g = True, h = False, i = True

  | Operation | &rarr; | Answer  |
  |:---------:|:------:|:-------:|
  |  g and g  | &rarr; | `True`  |
  |  h and h  | &rarr; | `False` |
  |   not i   | &rarr; | `False` |
  |   not h   | &rarr; | `True`  |
  |   not g   | &rarr; | `False` |
  |  g and h  | &rarr; | `False` |
  |  h and i  | &rarr; | `False` |
  |  g or i   | &rarr; | `True`  |
  |  h or i   | &rarr; | `True`  |
  |  i or g   | &rarr; | `True`  |
  |  i or h   | &rarr; | `True`  |
  |  i or i   | &rarr; | `True`  |
  |  h or h   | &rarr; | `False` |

- 3.5

  [3.4, 3.5, 3.6 - Checking Answers](3.4-3.5-3.6.py)

  A > B and C or D

  Precendencia: Relacionais primeiro, depois expressoes logicas (i.e, > < = antes de and, not, or).

  | A  | B |   C   |   D   | Result  |
  |:--:|:-:|:-----:|:-----:|:-------:|
  | 1  | 2 | True  | False | `False` |
  | 10 | 3 | False | False | `False` |
  | 5  | 1 | True  | True  | `True`  |

[Voltar](../README.md)