import random

#create a function for cointoss and then keep a count of heads and tails for 500 tosses
print("\033[31m" +"create a function for cointoss and then keep a count of heads and tails for 500 tosses"+ "\033[0m")

def cointoss():
  return round(random.random())

heads = 0
tails = 0

print ("tossing coins 500 times")
for i in range(500):
  if cointoss() == 1:
    heads += 1
  else:
    tails += 1

print(f"Heads: {heads}, Tails: {tails}")


#better toss since 0.5 gets rounded to 0 and not 1"
print("\033[31m" +"better toss since 0.5 gets rounded to 0 and not 1"+ "\033[0m")
def cointoss():
  return round(random.randint(0,1))

heads = 0
tails = 0

print ("tossing coins 500 times")
for i in range(500):
  if cointoss() == 1:
    heads += 1
  else:
    tails += 1

print(f"Heads: {heads}, Tails: {tails}")

#create a function for rolling dice and do the same for 1000 rolls
print("\033[31m" +"create a function for rolling dice and do the same for 1000 rolls"+ "\033[0m")

def rolldice():
  return int(6*random.random())

print ("rolling dice 1000 times")

one = 0
two = 0
three=0 
four=0
five=0
six=0

for i in range(1000):
  roll = rolldice()
  if roll == 1:
    one += 1
  elif roll == 2:
    two += 1
  elif roll == 3:
    three += 1
  elif roll == 4:
    four += 1
  elif roll == 5:
    five += 1
  else:
    six+= 1

print(f"one: {one}, two: {two}, three: {three}, four: {four}, five: {five}, six: {six}")

#check if a point p is close to a or b in 2 d space
print("\033[31m" +"check if a point p is close to a or b in 2 d space"+ "\033[0m")
def is_close(p, a, b):
  distance_to_a = (a[0]-p[0])**2 + (a[1]-p[1])**2
  distance_to_b = (b[0]-p[0])**2 + (b[1]-p[1])**2 

  if distance_to_a < distance_to_b:
    return f"point {p} is closer to {a}"
  elif distance_to_b == distance_to_a:
    return "equal"
  else:
    return f"point {p} is closer to {b}"
  
p = (1,2)
a = (2,3)
b = (1,3)
print(is_close(p,a,b))

  
p = (1,2)
a = (1,3)
b = (1,1)
print(is_close(p,a,b))


p = (1,2)
a = (2,3)
b = (1,10)
print(is_close(p,a,b))

#check is point in range
print("\033[31m" +"check is point in range"+ "\033[0m")
def is_in_range(p, a, b):
  if (p <a and p > b) or (p > a and p < b):
    return True
  else:
    return False
p = 5
a = 1
b = 10
print(f"{p} is in range {a} {b} {is_in_range(p,a,b)}")

p = 0
a = 1
b = 10
print(f"{p} is in range {a} {b} {is_in_range(p,a,b)}")

#check if point is on line
print("\033[31m" +"check if point is on line"+ "\033[0m")
def is_on_line(p, a, b):
  if a[0] == b[0]:
    if p[0] == a[0]:
      return f"point {p} is on the line between {a} and {b}"
    else:
      return f"point {p} is not on the line between {a} and {b}"
  
  m= (a[1]- b[1])/( a[0]- b[0]) 
  c=a[1]- m*a[0]
  print (f"y= {m}x+ {c}")
  if p[0]*m+c==p[1]:
    return f"point {p} is on the line between {a} and {b}"
  else:
    return f"point {p} is not on the line between {a} and {b}"  
p= (1,4)
a = (1,0)
b = (1,5)
print(is_on_line(p,a,b))

p= (3,4)
a = (1,0)
b = (1,5)
print(is_on_line(p,a,b))

p = (2,3)
a = (1,1)
b = (5,5)
print(is_on_line(p,a,b))

p = (2,2)
a = (1,1)
b = (5,5)
print(is_on_line(p,a,b))

p = (2,10)
a = (1,10)
b = (5,10)
print(is_on_line(p,a,b))

print("\033[31m" +"range overlapping or not"+ "\033[0m")

def is_overlapping2(x0,y0,x1,y1):
  if (x0<x1 and y0<y1 and y0>x1)or (x1<x0 and x0<y1 and y0>y1)or (x0>x1 and y0<y1)or(x0<x1 and y0>y1) :
    return f"ranges ({x0},{y0}) and ({x1},{y1}) are overlapping"
  else:
    return f"ranges ({x0},{y0}) and ({x1},{y1}) are not overlapping"  
print(is_overlapping2(6,5,7,10))
print(is_overlapping2(5,10,6,7))
print(is_overlapping2(1,5,6,10))
print(is_overlapping2(6,10,1,5))
print(is_overlapping2(1,10,5,7))
print(is_overlapping2(5,7,1,10))  

#check if point is in rectangle
print("\033[31m" +"check if point is in rectangle"+ "\033[0m")
def is_in_rectangle(p, a, b, c, d):
  #ab bc cd da ac bd
  if (is_in_range(p[0], a[0], b[0]) + is_in_range(p[0], b[0], c[0])+is_in_range(p[0], c[0], d[0])+is_in_range(p[0], a[0], d[0])+is_in_range(p[0], a[0], c[0])+is_in_range(p[0], d[0], b[0]))>3:
    if (is_in_range(p[1], a[1], b[1]) + is_in_range(p[1], b[1], c[1])+is_in_range(p[1], c[1], d[1])+is_in_range(p[1], a[1], d[1])+is_in_range(p[1], a[1], c[1])+is_in_range(p[1], d[1], b[1]))>3:
      return f"point {p} is in rectangle formed by {a}, {b}, {c}, {d}"
  return f"point {p} is not in rectangle formed by {a}, {b}, {c}, {d}"

p = (3,3)
a = (1,1)
b = (5,1)
c = (5,5)
d = (1,5)
print(is_in_rectangle(p,a,b,c,d))

p = (6,3)
a = (1,1)
b = (5,1)
c = (5,5)
d = (1,5)
print(is_in_rectangle(p,a,b,c,d))

