# TextSeek


![TextSeek](http://realwebgeeks.com/wp-content/uploads/2017/06/Outlook-PST-search.jpg)



## Description

Search for text inside files across of massive number of files.



### Inputs & Outputs
To find a phrase in a file you need to type in the location where you want to start you search and a phrase you search for.

Location:

`"Which folder do you want to search: "`


Examples:

* `.` 					- current folder.
* `../` 				- go a back folder.
* `../Publications` 	- go a back folder and enter folder Publications.

Phrase:

`"What do you want to search for, single phrases only: "`


Example:

* `Nemo`
* `World`
* `The earth does not want new continents, but new men.`




Example of output for "Nemo" :


`382: MATCH-----------------------------------------------------
File: actual file location/20000 Leagues under the sea.txt
Line: 12158 
Match text: so many other vessels have been lost!  If it be so--if Captain Nemo`


`383: MATCH-----------------------------------------------------
File: actual file location/20000 Leagues under the sea.txt
Line: 12169 
Match text: CAPTAIN NEMO AND MYSELF.`



`Search is done!
Total number of matches is 383`


## Notes/ Additional Info


Due to high memory usage when scaning a large quantity of files (tested on over 1GB of book and python files) there was a need to 

create TextSeekGen - a TextSeek app version that uses less memory.