a=12
b=2.2
c=True
d=12+3j
e="2"


print("CASE TO ->\tint\tfloat\tbool\tcomplex\t str")
print(f"int \t\t{int(a)}\t{(float(a))}\t{bool(a)}\t{complex(a)}\t {str(a)}")
print(f"float \t\t{int(b)}\t{(float(b))}\t{bool(b)}\t{complex(b)} {str(b)}")
print(f"bool \t\t{int(c)}\t{(float(c))}\t{bool(c)}\t{complex(c)}\t {str(c)}")
print(f"complex \tX\t X\t{bool(d)}\t{complex(d)}\t {str(d)}")
print(f"str(number) \t{int(e)}\t{(float(e))}\t{bool(e)}\t{complex(e)}\t {str(e)}")
e="e"
print(f"str \t\tX\tX\t{bool(e)}\tX\t {str(e)}") 