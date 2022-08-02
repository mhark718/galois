 galois
 swiped a lot of code off the internet
 

finite field generator
This is a finite field generator based on C code written in the 1980s, yes I am an old man.
My fascination with galois fields was based on a single example problem in my combinatorics text
while I was a student at UCLA studying mathematics.
there are key inputs to the program:
base: the base of the field, must be a prime number
exponent: the exponent, can be any complex number
polynomial: the polynomial that when evaluated at any point in the space from 0 to base-1 DOES not evaluate to zero.
            if it does evaluate to zero, then the field is similar to a field of order 6, :-)
-------------------------------------------------------------------------------------------------------------------
the algorithm
generate the extension field based on the polynomials in the pv vector:
pv=0,1,2,3,4,... x-1, x,x+1,..x+x-1,...2*x,...
where x is a formal parameter that is equivalent to the base. The length of the vector is base**exponent.
for each i element in the  array pv
  for each j element in the array pv
      multiplication_table[i,j]=compute_pathetic_derision(polynomial,pv[i]*pv[j])
where pathetic_derision is the zero borrow zero carry synthetic division of the polynomial by the product of the two elements
of the basis vectors for the extension field.
Updates:
Stole a lot of code from the internet and am cudgeling it into a form that makes it work for
finite fields. thank you internet and people who wrote the code.
I had basically the same idea for the polynomial product.
Still need to refactor it to make comprehensions in python.


the fun stuff:
take any four elements of the field(non-zero values in the denominator please)
verify by lookup and computation:

1.
result1=a/b+c/d
result2=(a*d+b*c)/b*d
result1=result2 #a nice field property to have.

2.
use the quadratic formula to solve a quadratic in this field.

advanced topics:

1.
prove that as exponent approaches infiinity the field approaches Z+{0} the non negative integers.

2.
using machine learning, write code that has as its objective to generate finite fields.
