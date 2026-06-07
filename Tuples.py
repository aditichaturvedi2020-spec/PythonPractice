# Tuples 

tup = (33,54,56,76,87,98)
print(tup[4])

# empty tuple
tupl = ()
print(type(tupl))

# single tuple

tup2 = (1)          #tuple
print(type(tup2))   # int

# but to represnt single tuple's type as tuple we do

tup3 = (1,)
print(type(tup3))

# Tuples are immutable (once created can't be changed)

tuple = ("Aditi", "Khushi", "Kelly", "Manisha")
tuple[1] = "Nalini"
print(tuple)