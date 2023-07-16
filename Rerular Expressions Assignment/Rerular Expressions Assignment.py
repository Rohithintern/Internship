#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

# In[12]:


import re

test_string = "Uzumaki Naruto 1113345rock lee"
pattern = r"[0-9A-Za-z]"
result = re.findall(pattern,test_string)
print(result)


# 2. Function in python that matches a string that has an a followed by zero or more b's
# 

# In[16]:


import re

txt = "Abc comics is greater than baab comics."
pattern = r'ab*'
result = re.findall(pattern, txt)
print(result)


# 3. Function in python that matches a string that has an a followed by one or more b's
# 

# In[18]:


import re

my_string = "Sample string with abracadabra and abb"
pattern = r'ab+'
result = re.findall(pattern, my_string)
print(result)


# 4. Python and use RegEx that matches a string that has an a followed by zero or one 'b'.
# 

# In[20]:


import re

my_string = "Another example with cab and dab."
pattern = r'ab?'
result = re.findall(pattern, my_string)
print(result)


# 5. Python program that matches a string that has an a followed by three 'b'.
# 

# In[22]:


import re

my_string = "The quick brown fox jumps over the lazy dog with bbbadwag."
pattern = r'b{3}\w+'
result = re.findall(pattern, my_string)
print(result)


# 6. Regular expression in Python to split a string into uppercase letters.
# 

# In[56]:


import re

my_string ="ImportanceOfRegularExpressionsInPython"
result = re.split(r'(?=[A-Z])', my_string)
print(result)


# 7. Write a Python program that matches a string that has an a followed by two to three 'b'.
# 

# In[28]:


import re

my_string = "The rabbit jumped over the hurdle with a bbbwww baboon and bbbkjj"
pattern = r'\bb{2,3}\w+'
result = re.findall(pattern,my_string)
result


# 8. Python program to find sequences of lowercase letters joined with a underscore.
# 

# In[30]:


import re

my_string ="c_h_a_l_l_a_m_a_l_l_a_R_o_h_i_t,"
pattern = r'[a-z]\w'
result = re.findall(pattern, my_string)
result


# 9. Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
# 

# In[38]:


import re


my_string ="AirBnb is the coolest place to have fun"
pattern = "A....b"
result = re.search(pattern, my_string)
result


# 10. Write a Python program that matches a word at the beginning of a string.
# 

# In[39]:


import re

my_string = "Hello, how are you?"
pattern = r"^Hello"
result = re.findall(pattern,my_string)
result


# 11. Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
# 
# 

# In[40]:


my_string = "Winner Winner chicken dinner with 23 kill team kills_ 7 solo kills"
pattern = r'\b[a-zA-Z0-9_]\w+'
result = re.findall(pattern, my_string)
result


# 12. Write a Python program where a string will start with a specific number.
# 

# In[44]:


my_string= "23kill Winner Winner chicken dinner with team kills_ 7 solo killsL"
pattern = r'^[23]\w+'
result= re.findall(pattern,my_string)
result


# 13. Write a Python program to remove leading zeros from an IP address

# In[45]:


my_string = "222.001.1100.110"
pattern = r'[0]'
result = re.sub(pattern," ",my_string)
result


# 14. Regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.
# 
# 

# In[65]:


import re

text = "On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country"
pattern = r'\b([A-Za-z]+ \d{1,3}(?:st|nd|rd|th)? \d{4})'
result = re.findall(pattern,text)
result


# 15. Write a Python program to search some literals strings in a string. Go to the editor
# 

# In[58]:


my_string = 'The quick brown fox jumps over the lazy dog.'
pattern = r'\b[f.x,d.g,h...e]\w+'
result= re.findall(pattern,my_string)
result


# 16. Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
# 

# In[66]:


import re
my_string = 'The quick brown fox jumps over the lazy dog.'
pattern = r'[f.x]\w+'
result = re.search(pattern, my_string)
result


# 17. Python program to find the substrings within a string.
# 
# 

# In[67]:


import re
my_string = 'Python exercises, PHP exercises, C# exercises'
pattern =  r'[e.*]\w'
result = re.findall(pattern,my_string)
result


# 18. Python program to find the occurrence and position of the substrings within a string.
# 

# In[52]:


import re
my_string = "hogwarts train travells with magic"
pattern = r'[g..]\w+'
result = re.search(pattern,my_string)
result


# 19. Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
# 

# In[53]:


import re

date = "1995-12-03"
pattern = r'(\d{4})-(\d{2})-(\d{2})'
result = re.sub(pattern, r'\3-\2-\1', date)
result


# 20. Python program to find all words starting with 'a' or 'e' in a given string.
# 
# 

# In[54]:


import re
my_string = "first Wimbledon championships All England Club"
pattern =  r'\b[aAeE]\w+'
result = re.findall(pattern,my_string)
result


# 21. Write a Python program to separate and print the numbers and their position of a given string.
# 

# In[55]:


import re

my_string = "Nadal has won 92 ATP singles titles, including 22 Grand Slam men's singles titles and 36 ATP Tour Masters 1000 titles"
matches = re.finditer(r'\d+', my_string)
for match in matches:
    number = match.group()
    position = match.span()
    print(f"Number: {number}, Position: {position}")


# 22. Write a regular expression in python program to extract maximum numeric value from a string
# 

# In[71]:


import re

my_string = "Nadal has won 92 ATP singles titles, including 22 Grand Slam men's singles titles"
pattern = r'\d+'
result = re.findall(pattern, my_string)
max_value = max(map(int, result))

print(max_value)


# 23. write a Regex in Python to put spaces between words starting with capital letters
# 

# In[72]:


import re

my_string = "ThisIsAnExampleStringWithCapitalWordsInTheMiddle"
pattern = r'(?<!^)(?=[A-Z])'
result = re.sub(pattern, ' ', my_string)

print(result)


# 24. Python regex to find sequences of one upper case letter followed by lower case letters
# 

# In[73]:


import re

my_string = "Hello World, Messi is Awesome"
pattern = r'[A-Z][a-z]+'
result = re.findall(pattern, my_string)

print(result)


# 25. Write a Python program to remove duplicate words from Sentence using Regular Expression

# In[76]:


import re

my_string = "This is is a test sentence to test duplicate duplicate words removal."
pattern = r'\b(\w+)\b\s+(?=.*\b\1\b)'
result =re.sub(pattern," " , my_string)
result


# 26. python program using RegEx to accept string ending with alphanumeric character.
# 

# In[78]:


import re

my_string = "sleepyhead1133"
my_string1 = "Sayonara sleepyhead"
pattern = r'^.*[a-zA-Z0-9]$'
result = re.match(pattern,my_string)
result1 = re.match(pattern, my_string1)
result
result1


# 27. Write a python program using RegEx to extract the hashtags.

# In[79]:


my_string = "RT @kapil_kausik: #Doltiwal I mean #xyzabc is hurt by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> acquired funds No wo"
pattern = "[#..............]\w+"
result = re.findall(pattern,my_string)
result
#Output: ['#Doltiwal', '#xyzabc', '#Demonetization']


# 28. Python program using RegEx to remove <U+..> like symbols.

# In[80]:


my_string = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
pattern = "<U+.....>"
result = re.sub(pattern," ",my_string)
result
#Output: @Jags123456 Bharat band on 28??<ed><ed>Those who  are protesting #demonetization  are all different party leaders


# 29. Python program to extract dates from the text stored in the text file.
# 
# 

# In[81]:


import re

my_string= 'Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.'
pattern = r'\d{2}-\d{2}-\d{4}'
result = re.findall(pattern, my_string)
result


# 30. Python program to replace all occurrences of a space, comma, or dot with a colon.
# 
# 

# In[83]:


import re
my_string= 'Python Exercises, PHP exercises.'
x = re.sub(r'[ ,.]', ':', my_string)
print(x)
#Output: Python:Exercises::PHP:exercises:


# In[ ]:




