# Lukas Schwab, 6/18/14
# github.com/lukasschwab
# lukas.schwab@gmail.com

#-----------------------#

# Randomly generates hex codes for colors, numer of which is input.
# This is probably useless.

#-----------------------#

# Import the pseudorandom number generator
from random import randint

# Import the number of colors that need to be generated.
num=int(raw_input('Enter the number of colors to generate.     '))

# Loop for that number
for x in range(0,num):
	# Empty final color
	colorf = ""
	for y in range(0,3):
		randi = randint(0,255) # Inclusive
		hexi = hex(randi)[2:]
		# Make sure it's two digits
		if len(hexi) < 2:
			hexi2="0"
			hexi2+=str(hexi)
			hexi=hexi2
		colorf+=hexi
	print colorf