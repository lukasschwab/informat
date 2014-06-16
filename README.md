informat
========

Python color-selection toolkit for the generation of infographics.

I started to practice making infographics, but selecting colors that gradiate proportionally to a percentage (like a statistic) was difficult, so I opted to write a python script to do the job for me.

First time building a practical application of Python, will continue to work on optimizing past scripts.

### Current library

+ **1color-percent.py** will prompt for a color to indicate 100%, and then ask for the percentage to be colored. It outputs a hex value. The higher the percentage, the darker the color.

+ **2color-percent.py** will prompt for a color to indicate 100% and a color to indicate 0%, and then ask for the percentage to be colored. It outputs a hex value that is the weighted average of those two colors, based on that percentage. The higher the percentage, the closer to the color to incate 100%.

+ **2color-ratio.py** will prompt for two colors and two ratio values. This ratio determines the weights for the average of the two colors. Still debugging.

### To-do

+ Write tests for the **2color-percent.py** script

+ Debug and write tests for the **2color-ratio.py** script

+ Get rid of single quotes for hex inputs

+ Optimize