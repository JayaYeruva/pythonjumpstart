__author__ = 'ravi'

name = raw_input('Enter the name :')
city = raw_input('Enter the city :')
zip_code = raw_input('Enter the zip code :')

if zip_code.isdigit():
    zip_code = int(zip_code)
else:
    print "invalid input for the zip code :", zip_code
    exit(1)


print zip_code
print type(zip_code)

"""
print "name :", name
print "city :", city
"""

