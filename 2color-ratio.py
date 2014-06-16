# Lukas Schwab, 6/15/14
# github.com/lukasschwab
# lukas.schwab@gmail.com

#-----------------------#

# Defines a color as a weighted average between two, input as a ratio.

#-----------------------#

# Prompt the two color inputs and their ratio elements.
clr1=str(input('Enter the hex value for the first color.     '))
num1=input('Enter the ratio element for the first color.     ')
clr2=str(input('Enter the hex value for the second color.     '))
num2=input('Enter the ratio element for the second color.     ')

# Split the colors into a list of the component 2-digit numbers
clrlist1=[clr1[i:i+2] for i in range(0, len(clr1), 2)]
clrlist2=[clr2[i:i+2] for i in range(0, len(clr2), 2)]

# Define the ratios
both=num1+num2
rat1=float(num1/both)
rat2=float(num2/both)

# Final color to 0
clrf=""

# Loop for every index in each of the lists
for x in range(0,3):
	# Convert the value in both of those spots to a decimal
	dec1=int(clrlist1[x],16)
	dec2=int(clrlist2[x],16)

	# Find the modified color by taking a weighted average
	modded=int(dec1*rat1)+int(dec2*rat2)

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