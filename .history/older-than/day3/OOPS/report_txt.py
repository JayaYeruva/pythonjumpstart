#!/usr/bin/env python

from invoice import Invoice

class Report(Invoice): 
  def __init__(self):
    super(Report, self).__init__();
    self.loadLookup()

  def to_txt(self, invoice_no):
    tot = 0
    if self.lookup.has_key(invoice_no):
       print "Invoice Id : %s " % invoice_no 
       for key in self.lookup[invoice_no]:
	  if type(self.lookup[invoice_no][key]) == type([]):
             print "-" * 53;
	     detail = self.lookup[invoice_no][key]
             for order in detail:
	        sub_tot = float(order['unit-cost']) * int( order['quantity'])
                tot += sub_tot
	        print "%20s %10.2f %10s %10.2f" % (order['product'], \
				float(order['unit-cost']), order['quantity'], sub_tot )
          else:
              print "%s : %s" % (key, self.lookup[invoice_no][key])
    print "-" * 53;
    print "%53.2f" % tot 


if __name__ == '__main__':
  r = Report()
  r.to_txt('1001');
	   
	
