# This is a brief showcase of regex in Python. 
# The library will take a second to load... be patient!
import re

# Raw data, split by a bunch of different characters
data = "40&45\t12z98$5 25"

# This will split the data by any character inside
# of the square brackets [].
data = re.split("[&\t$z ]", data)

print data