#!/usr/bin/env python
import sys
import os
import stat

st = os.stat(sys.argv[1])
print stat.S_ISREG( st.st_mode )

