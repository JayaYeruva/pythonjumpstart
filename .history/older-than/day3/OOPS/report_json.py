#!/usr/bin/env python
import json
from invoice import Invoice

class Report(Invoice): 
  def __init__(self):
    super(Report, self).__init__();
    self.loadLookup()

  def to_json(self):
    return json.dumps(self.lookup)

if __name__ == '__main__':
  r = Report()
  print r.to_json()
	
