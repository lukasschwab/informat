# Lukas Schwab, 6/15/14
# github.com/lukasschwab
# lukas.schwab@gmail.com

#-----------------------#

# Defines a color as a weighted average between two, input as a ratio.
# Previously the two values in the ratio were input seperately, each after the color with which it was associated.
# Easy to implement again:
# 	1. Remove the line of code under comment "Input the ratio" (ratio = str...)
#	2. Add the following code somewhere before that block:
#		num1 = input('Enter the ratio value for color 1.')
#		num2 = input('Enter the ratio value for color 2.')
#	3. You may need to modify lines 32-33, because it won't be input as a string.

#-----------------------#

# Prompt the two color inputs and their ratio elements.
clr1=raw_input('Enter the hex value for the first color.     ')
clr2=raw_input('Enter the hex value for the second color.     ')

# Split the colors into a list of the component 2-digit numbers
clrlist1=[clr1[i:i+2] for i in range(0, len(clr1), 2)]
clrlist2=[clr2[i:i+2] for i in range(0, len(clr2), 2)]

# Loop infinitely until broken
loopit = 0
while loopit < 1:

	# Input the ratio
	ratio=raw_input('Enter the ratio in the form x:y, or quit.     ')
	if ratio=="quit":
		import sys
		print "Ending Script"
		sys.exit()
	num1=float(ratio[0:ratio.index(':')])
	num2=float(ratio[(ratio.index(':')+1):len(ratio)])

	# Define the ratios
	both=float(num1+num2)
	rat1=num1/both
	rat2=num2/both

	# Final color to 0
	clrf=""

	# Loop for every index in each of the lists
	for x in range(0,3):
		# Convert the value in both of those spots to a decimal
		dec1=int(clrlist1[x],16)
		dec2=int(clrlist2[x],16)

		# Find the modified color by taking a weighted average
		modded=int((dec1*rat1)+(dec2*rat2))

		# Convert back to hex.
		modded=hex(modded)[2:]
		# Make sure it's two digits
		if len(modded) < 2:
			modded2="0"
			modded2+=str(modded)
			modded=modded2

		# Concatonate to the string.
		clrf+=str(modded)

	print '#' + clrf