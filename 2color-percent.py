# Lukas Schwab, 6/15/14
# github.com/lukasschwab
# lukas.schwab@gmail.com

#-----------------------#

# Defines a color as a weighted average between two, input as a percentage.

#-----------------------#

# Prompt the two color inputs
clr0=raw_input('Enter the hex value for the 0 percent color.     ')
clr100=raw_input('Enter the hex value for the 100 percent color.     ')
# Split into a list of the component 2-digit numbers
clrlist0=[clr0[i:i+2] for i in range(0, len(clr0), 2)]
clrlist100=[clr100[i:i+2] for i in range(0, len(clr100), 2)]


# Start off the while-loop at x=0 so it isn't triggered
loopit=0
# Open the loop. Will continue indefinitely until an unacceptable value is input.
while loopit < 1:
	# Input the percentage you're looking for
	pct=raw_input('Enter the percentage, without a percent sign, or quit.     ')
	if pct=='quit':
		import sys
		print "Ending Script"
		sys.exit()
	pct = int(pct)
	pct=float(100-pct)
	pct=pct/100

	# Final color to 0
	clrf=""

	# Loop for every index in each of the lists
	for x in range(0,3):
		# Convert the value in both of those spots to a decimal
		dec0=int(clrlist0[x],16)
		dec100=int(clrlist100[x],16)

		# Find the modified color by taking a weighted average
		modded=int(dec100*pct)+int(dec0*(1-pct))

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