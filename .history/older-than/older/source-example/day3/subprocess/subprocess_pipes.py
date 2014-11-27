#!/usr/bin/env python
import subprocess
cat = subprocess.Popen(['cat', '/etc/passwd'], 
                        stdout=subprocess.PIPE
                        )

cut = subprocess.Popen(['cut', '-f', '1', '-d:'],
                        stdin=cat.stdout,
                        stdout=subprocess.PIPE,
                        )

sort = subprocess.Popen(['sort'],
                        stdin=cut.stdout,
                        stdout=subprocess.PIPE,
                        )

tr = subprocess.Popen(['title'],
			stdin=sort.stdout,
			stdout=subprocess.PIPE
			)

nl = subprocess.Popen(['nl'],
			stdin=tr.stdout,
			stdout=subprocess.PIPE
			)				

print 'Included files:'
for line in nl.stdout:
    print '\t', line.strip()
