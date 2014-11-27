#!/usr/bin/env python

class Taxi:
    def __init__(self, km, category):
        self.km = km
        self.category = category
	self.amt = 0
    
    def compute(self):
	if (self.km<=4):
	    self.amt = self.km * 6 
        elif (self.category.lower() == 'normal'):
	    self.amt = (4 * 6) + (self.km - 4) * 1.25  	
        elif (self.category.lower() == 'special'):
	    self.amt = (4 * 6) + (self.km - 4)   	
        else:
            return None
	return self.amt
     
    def printBill(self):
        print "Billable amount : %.2f" % self.compute()  	
    
    def __del__(self):
        pass

if __name__ == '__main__':
    t = Taxi(100, 'normal')
    t.printBill()
