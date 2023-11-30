'''
Regular expression(RegEx) is a module that can be used to search for a character, a word or even a special character in a given string.
It can be used after importing the 're' library
There are four different RegEx functions:
-search:	The search() function searches the string for a match, and returns a match object if there is a match. If there is more than one match, only the first occurrence of 	the match will be returned.'''

import re

txt = "building a better working world"
x = re.search("bet", txt)
print (x)

#output : <re.Match object; span=(11, 14), match='bet'>
'''
-findall:	The findall() function returns a list containing all matches'''

import re

txt = "building a better working world"
x = re.findall("b", txt)
print (x)

#output : ['b', 'b']
'''
-split:		The split() function returns a list where the string has been split at each match.'''

import re

txt = "building a better working world"
x = re.split("\s", txt)
print (x)

#output : ['building', 'a', 'better', 'working', 'world']
'''
-sub:		The sub() function is used to replace the matches with a different set of characters of your choice.'''

import re

txt = "building a better working world"
x = re.sub("b", "c", txt)
print (x)

#output : cuilding a cetter working world

'''

MetaCharacters
[]	A set of characters															"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)									"he..o"	
^	Starts with																	"^hello"	
$	Ends with																	"planet$"	
*	Zero or more occurrences													"he.*o"	
+	One or more occurrences														"he.+o"	
?	Zero or one occurrences														"he.?o"	
{}	Exactly the specified number of occurrences									"he.{2}o"	
|	Either or																	"falls|stays"	
()	Capture and group


Special Sequences
\A	Returns a match if the specified characters are at the beginning of the string										"\AThe"	
\b	Returns a match where the specified characters are at the beginning or at the end of a word 						r"\bain"
	(the "r" in the beginning is making sure that the string is being treated as a "raw string")							r"ain\b"
\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word 		r"\Bain"
	(the "r" in the beginning is making sure that the string is being treated as a "raw string")							r"ain\B"	
\d	Returns a match where the string contains digits (numbers from 0-9)													"\d"	
\D	Returns a match where the string DOES NOT contain digits															"\D"	
\s	Returns a match where the string contains a white space character													"\s"	
\S	Returns a match where the string DOES NOT contain a white space character											"\S"	
\w	Returns a match where the string contains any word characters														"\w"	
\W	Returns a match where the string DOES NOT contain any word characters												"\W"	
\Z	Returns a match if the specified characters are at the end of the string											"Spain\Z"

'''