#!/usr/bin/env python
import re

class Invoice(object):
  def __init__(self):
	self.master = 'master.dat'
        self.detail = 'detail.dat'
        self.lookup = {}

  def loadLookup(self):
    next = 0
    detail = open('detail.dat')
    with open(self.master) as master:
      for m_record in  master:
        if next == 0:
	  next += 1
          continue
        m_record = m_record.rstrip()
        t_master = m_record.split(',')
	self.lookup[t_master[0]] = { 
				'customer' : t_master[1], 
				'sales person' :t_master[2],
				'detail' : []
				}
        detail.seek(0, 0)
        for d_rec in detail:
          if re.match(t_master[0], d_rec):
             d_rec = d_rec.rstrip()
             t_detail = d_rec.split(',')
	     prod_det = { 
		   	  'product'   : t_detail[1],
			  'unit-cost' :t_detail[2], 
			  'quantity'   : t_detail[3]
			}
	     self.lookup[t_master[0]]['detail'].append(prod_det) 
    detail.close()
	     	
  def report(self):
    self.loadLookup()
    from pprint import pprint
    pprint(self.lookup)

if __name__ == '__main__':
    inv = Invoice()
    inv.report() 	     

