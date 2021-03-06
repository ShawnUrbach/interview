# mySidewalk Inc Coding Assessment




## Problem #1:
* The user has a file that is made up of short (less than 1000 character) strings, each on a different line (assume any common character or character combination that means a newline to someone might be used interchangeably in this file). Most of these strings will be preceded by numbers, i.e. “2 Steaks”, “10 Chicken Wings”, “343GuiltySparks”. Accept the file from the user and return them a file with the same items sorted first by the numeric value of any leading number (2 < 10 < 343) and then alphabetically for the rest of the string.

## Solution #1:
* INSTRUCTIONS:  

* Use Python 3.5 to open sorting.py.  

* At the prompt, type in the path of the existing text file you wish to sort.

* testfile.txt already contains 17 lines of random numbers, spaces and uppercase/lowercase letters.

* Another option would be to use randomgen.py (also Python 3.5) to generate a text file consisting of 10,000 lines of random 1-3 digit numbers followed by 1-1,000 characters of letters.

* Output file of sorting.py is called sorted.txt.

* ASSUMPTIONS:

* sorting.py includes functions for inserting whitespace between numbers and other characters (if none exists) and removing multiple whitespace (if more than one space exists) for a cleaner output.

* It will sort numbers first and then alpahebtically following the space after the number.

* Sorting will work correctly whether the input file contains floats, lines with no whitespace, lines with multiple whitespace, only letters, or only numbers.

* Tested with files of 100,000+ lines including all alphanumeric combinations above. 

## Problem #3:
* The user wants to visualize the following geojson layers ([1](https://github.com/mysidewalk/interview/blob/master/assets/kc-neighborhoods.json), [2](https://github.com/mysidewalk/interview/blob/master/assets/kc-tracts.json)) together on a map along with a chart of their commuter population attributes in an interactive manner.

## Solution #3:
* INSTRUCTIONS:

* View interactive map at: https://htmlpreview.github.io/?https://github.com/ShawnUrbach/interview/blob/master/Solution%203/index.html

* Alternative link: https://rawcdn.githack.com/ShawnUrbach/interview/master/Solution%203/index.html

* ASSUMPTIONS:

* I made this map using a combination of Leaflet.js and Chart.js.

* I put the two geojson layers (Neighborhoods and Census Tracts) into separate layers so that the user may choose one as viewable at a time.

* I decided that the best way to visualize the commuter pattern information was through a choropleth map.  

* The map is colored in a way so that areas where more people walk or take public transportation to work (vs. car or carpool) are shaded in darker colors of red.

* The specific commuter population attributes are shown via popup labels when the user hovers over an area.

* The information in the chart at the bottom is drawn from the Neighborhoods geojson layer.

* As you can see, Manheim Park is the neighborhood with the highest percentage of people either walking or taking public transportation to work (at 53%).
