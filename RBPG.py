# Reaper Batch Project Generator
# By Jun-Hong, 2014

# http://stackoverflow.com/questions/3141642/increment-a-version-number-using-regular-expression

import re, sys,string

in_file=sys.argv[1]
iterations=int(sys.argv[2])

linecounter=0

length=0
modifiedline=""

#recognizing the filename number
filenamePat = re.compile(r'(.*?)(\d+)(.*)')
filenamematch = filenamePat.search(in_file)

if filenamematch:
	filecounter=int(filenamematch.group(2)) #set the initial filecounter number
	
read_file = open(in_file).readlines() 


# The stuff we want to match
# nameInProjPat = re.compile(r'(\s+NAME.*?|\s+FILE.*?)(\d+)(.*$)')
nameInProjPat = re.compile(r'(\s+NAME.*?|\s+FILE.*\\.*?)(\d+)(.*\..*$)')
#match as much stuff as possible until a slash=folder path and then as much stuff until a dot = file exietnsion

# Do the IOps
for file in range(0,iterations):

	write_file = open(filenamematch.group(1)+str(filecounter+1)+filenamematch.group(3), "w") 

	for line in read_file:
		
		m1 = nameInProjPat.search(line)
		# m2 = fileInProjPat.search(line)
		if m1:
			incremented= int(m1.group(2)) #convert to int so it can be incremented
			incremented+=file+1
			incremented=str(incremented)
			incremented=incremented.zfill(m1.group(2).__len__()) #pad zeroes
			line=m1.group(1)+incremented+m1.group(3)+"\n" #reassemble the line
		
		write_file.write(line)
		
		linecounter+=1
	write_file.close
	filecounter+=1
