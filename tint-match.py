# Lukas Schwab, 6/18/14
# github.com/lukasschwab
# lukas.schwab@gmail.com

#-----------------------#

# Finds the average tint of one input color, scales another input color so the tint matches
#
# Here's some math:
#	Normally you would express tint like this:
#		tint = (r+g+b)/3
#	But here is a comparison of two, so the "/3" is irrelevant.
#	Want to keep the ratio constant, so there's a constant multiplier (s)
#		r2*s + g2*s + b2*s = r1 + g1 + b1
#		s(r2+g2+b2)

#-----------------------#

# First, find tint to be matched
clr1=str(input('Enter the hex value for the tint to be matched.     '))\
# Split into RGB components
# SHOULD SPLIT INTO A LIST HERE INSTEAD
r1=int(clr1[0:2],16)
g1=int(clr1[2:4],16)
b1=int(clr1[4:6],16)
# Calculate the sum
total1=float(r1+g1+b1)

clr2=str(input('Enter the hex value for the color to be changed.     '))
# Split into RGB components
# SHOULD SPLIT INTO A LIST HERE INSTEAD
r2=int(clr2[0:2],16)
g2=int(clr2[2:4],16)
b2=int(clr2[4:6],16)
# Calculate the sum
total2=float(r2+g2+b2)

# Calculate the ratio
ratio=float(total1/total2)

# Empty final color
clrf=""

# Shift color 2
rf=int(r2*ratio)
gf=int(g2*ratio)
bf=int(b2*ratio)
# Convert back to hex.
rf=hex(rf)[2:]
if len(rf) < 2:
	rf2="0"
	rf2+=str(rf)
	rf=rf2
clrf+=rf
gf=hex(gf)[2:]
if len(gf) < 2:
	gf2="0"
	gf2+=str(gf)
	gf=gf2
clrf+=gf
bf=hex(bf)[2:]
if len(bf) < 2:
	bf2="0"
	bf2+=str(bf)
	bf=bf2
clrf+=bf

print '#' + clrf