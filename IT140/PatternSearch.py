#Edward J Moon
#IT-140: Introduction to Scripting
#Assignment: Project 4 Final
#Instructor: Zoe Likoudis
import re

#Paragraph provided for search and replace

lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

#The instructions say to find any characters that aren't alphanumeric.
#The regex identifiers \W and \D will find non-letters and non-numbers, respectively.
#Excluding numbers gives a result that doesn't pass in Codio, so the instruction
#based pattern will be commented below.
#

#Remember to K.I.S.S. (Keep It Simple, Stupid). No need to make a complicated string of characters to ignore when Python already has it.
#Using a wildcard makes it so that we search for everything that the wildcard is defined as in the language. In this case, we use the
#\W wildcard to find anything that isn't a letter. We could do the same thing with literal characters, but it's unneccessarily complicated.
#To find what we want with literal characters, we use the range of charcters 0-9 along with all special characters. Some special chacters
#would need to be escaped such as \ and ^ or *. We really don't need to do that for this script, so we simplify the process by using a wildcard. 
pattern1="\W" #find anything that's not a letter
#pattern1="\W\D" #instruction based pattern

#Use pattern 1 to find all non-letter characters and get the result that Codio is expecting.
search_result=re.findall(pattern1,lorem_ipsum) 
#Show the number of non-letter characters
print(len(search_result))
#Create a new pattern that will find all instances of sit-amet and sit:amet
#There are specific characters that need to be included in the search, so have them in brackets so Python knows what to look for.
#When we have specific characters to look for, we use literal characters instead of wildcards.
pattern2="sit[-:]amet"
#pattern2 looks for two sequences. It looks for sit-amet and sit:amet. We defined the sequences to look for with [-:] in our pattern definition.
#Python's regular expression methods will automatically generate the strings to find based on our pattern and will separate them.
#Find the pattern options in the string
occurrences_sit_amet=re.findall(pattern2,lorem_ipsum)
#Output the number of pattern occurences
print(len(occurrences_sit_amet))
#Substitute all instances of the pattern with the desired string

#removed identiticle pattern variable to remove redundancy.
replace_results=re.sub(pattern2,"sit amet",lorem_ipsum)
pattern3="sit amet"
#Find how many times the substition string occurs in the changed string and output the number of
#instances.
occurrance_sit_amet=re.findall(pattern3,replace_results)
print(len(occurrance_sit_amet))

#Reflections: This script didn't pose much of an issue. I've used regular expressions before with searching for specific items
#in a URL with PHP. Python's methods were easier to use than PHP's but the process is essentially the same. I'll be pracicing on
#fixed length records a lot more. They gave me a much harder time than this script did.
