# The Puppy Name Wizard

### Data
WNYC generously provided the [raw data](http://project.wnyc.org/dogs-of-nyc/) for their [map of New York dog names](http://project.wnyc.org/dogs-of-nyc/), which is included in this repo in the /data/ directory.

To reduce this ~5MB file to a small list of top names for the HTML file, just run the ```names.py``` script. The output, dognames.csv, is also included in the repo.

### visualization
I use a mostly out-of-the-box version of Mike Bostock's [d3js](http://d3js.org) library for the stack chart with an added tooltip and small bar representing the active data point.