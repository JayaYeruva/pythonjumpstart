#!/usr/bin/env python
from a import A
from b import B

class C(A,B):
  def pprint(self):
    super(C, self).pprint()

if __name__ == '__main__':
   c = C()
   c.pprint()


