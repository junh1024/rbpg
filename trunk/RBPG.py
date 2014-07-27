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
nameInProjPat = re.compile(r'(\s+NAME.*?)(\d+)(.*?$)')
fileInProjPat = re.compile(r'(\s+FILE.*?)(\d+)(.*?$)')

# Do the IOps
for file in range(0,iterations):

	write_file = open(filenamematch.group(1)+str(filecounter+1)+filenamematch.group(3), "w") 

	for line in read_file:
		
		m1 = nameInProjPat.search(line)
		m2 = fileInProjPat.search(line)
		if m1:
			incremented= int(m1.group(2)) #convert to int so it can be incremented
			incremented+=filecounter
			incremented=str(incremented)
			incremented=incremented.zfill(m1.group(2).__len__()) #pad zeroes
			line=m1.group(1)+incremented+m1.group(3)+"\n" #reassemble the line
		if m2:
			line=m2.group(1)+m2.group(2)+m2.group(3)+"\n"
			# print("file matched, line is ", line, linecounter)
			
		
		write_file.write(line)
		
		linecounter+=1
	write_file.close
	filecounter+=1