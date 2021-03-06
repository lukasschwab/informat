informat
========

Python color-selection toolkit for the generation of infographics.
I started to practice making infographics, but selecting colors that gradiate proportionally to a percentage (like a statistic) was difficult, so I opted to write a python script to do the job for me.
First time building a practical application of Python, will continue to work on optimizing past scripts.

### Current library
#### Useful:
+ **1color-percent.py** will prompt for a color to indicate 100%, and then ask for the percentage to be colored. It outputs a hex value. The higher the percentage, the darker the color.
+ **2color-percent.py** will prompt for a color to indicate 100% and a color to indicate 0%, and then ask for the percentage to be colored. It outputs a hex value that is the weighted average of those two colors, based on that percentage. The higher the percentage, the closer to the color to incate 100%.
+ **2color-ratio.py** will prompt for two colors and two ratio values. This ratio determines the weights for the average of the two colors.
+ **tint-match.py** will prompt for two colors. The second color's RGB values will be scaled to match the tint of the first color.

#### Probably useless:
+ **50shades.py** will output 50 randomly selected shades of gray.
+ **colors-rand.py** will generate an input number of randomly selected colors.

### To-do
+ Repetition
	+ Add functionality to automatically iterate (example, to output 100 hex codes for every percentage.) Maybe parse in a list of percentages?
+ **tint-match.py**
	+ One of the RGB values could theoretically be pushed over 256 if it has a high initial value but the initial tint is low. How to handle these cases?
	+ Implement a list instead of separate variables in **tint-match.py** (see code for details)
+ Optimize