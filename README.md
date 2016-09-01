# mySidewalk Inc Coding Assessment




## Problem #1:
* The user has a file that is made up of short (less than 1000 character) strings, each on a different line (assume any common character or character combination that means a newline to someone might be used interchangeably in this file). Most of these strings will be preceded by numbers, i.e. “2 Steaks”, “10 Chicken Wings”, “343GuiltySparks”. Accept the file from the user and return them a file with the same items sorted first by the numeric value of any leading number (2 < 10 < 343) and then alphabetically for the rest of the string.

## Solution #1:
* INSTRUCTIONS:

* ASSUMPTIONS:

## Problem #3:
* The user wants to visualize the following geojson layers ([1](https://github.com/mysidewalk/interview/blob/master/assets/kc-neighborhoods.json), [2](https://github.com/mysidewalk/interview/blob/master/assets/kc-tracts.json)) together on a map along with a chart of their commuter population attributes in an interactive manner.

## Solution #3:
* INSTRUCTIONS:

* View interactive map at: https://cdn.rawgit.com/ShawnUrbach/interview/master/Solution%203/index.html 
* Alternative link: https://htmlpreview.github.io/?https://github.com/ShawnUrbach/interview/blob/master/Solution%203/index.html

* ASSUMPTIONS:

* I made this map using a combination of Leaflet.js and Chart.js.

* I put the two geojson layers (Neighborhoods and Census Tracts) into separate layers so that the user may choose one as viewable at a time.

* I decided that the best way to visualize the commuter pattern information was through a choropleth map.  

* The map is colored in a way so that areas where more people walk or take public transportation to work (vs. car or carpool) are shaded in darker colors of red.

* The specific commuter population attributes are shown via popup labels when the user hovers over an area.

* The information in the chart at the bottom is drawn from the Neighborhoods geojson layer.

* As you can see, Manheim Park is the neighborhood with the highest percentage of people either walking or taking public transportation to work (at 53%).
