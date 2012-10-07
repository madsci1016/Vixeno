******************************************************************
*  Vixeno - Vixen Sequence Parser in Python for Arduino
*		details and example sketch: 
*			http://www.billporter.info/?p=1458
*
*		Brought to you by:
*              Bill Porter
*              www.billporter.info
*
*
*  Lib version history
*    1.0 created
*	
*
*
*This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
<http://www.gnu.org/licenses/>
*  
*
*This work is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License. 
*To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/ or
*send a letter to Creative Commons, 444 Castro Street, Suite 900, Mountain View, California, 94041, USA.
******************************************************************/

*******************How to Use***********************
0) Have python 2.7 installed on your computer. http://www.python.org/download/
1) create a sequence to your liking in Vixen and save to a file.
2) copy Vixeno.py into the folder with your saved sequence
3) in a command window running from that folder, run this command: "python Vixeno.py [NameOfYourShow].vix"
4) if successful, it will create a 'VixenShow.cpp' file with your show data and some other useful information
5] add that file to your arduino sketch and run your own code to grab the show data
