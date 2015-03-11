 
>>> #lambda args1, args2,... : exp
... 
>>> 
>>> sqr = lambda n: n**2
>>> 
>>> sqr
<function <lambda> at 0x7f22ea462f50>
>>> 
>>> type(sqr)
<type 'function'>
>>> 
>>> sqr(5)
25
>>> 
>>> power = lambda x, n=0 : x ** n
>>> power(5)
1
>>> power(5, 3)
125
>>> raiseme = lambda n: n**2 if n>5  else n**3
>>> raiseme(6)
