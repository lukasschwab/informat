# Lukas Schwab, 6/17/14
# github.com/lukasschwab
# lukas.schwab@gmail.com

#-----------------------#

# Randomly selects 50 shades of gray.

#-----------------------#

# Import the pseudorandom number generator
from random import randint

# Loop for the 50 shades
for x in range(0,50):
	randi = randint(0,256) # Inclusive
	hexi = hex(randi)[2:]
	# Make sure it's two digits
	if len(hexi) < 2:
		hexi2="0"
		hexi2+=str(hexi)
		hexi=hexi2
	total = ""

	# This should be implemented as a loop
	# for y in range (1,3):
	total += str(hexi)
	total += str(hexi)
	total += str(hexi)

	# Output
	print total