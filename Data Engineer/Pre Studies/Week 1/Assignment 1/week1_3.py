#! Python3

"""
Coding Challenge 3 - F-strings
A new way of formatting strings called 'f-strings' was recently introduced to Python. See this 
video https://youtu.be/o0mvgsPQ8JgLinks to an external site for a demo on this functionality.

Declare self-chosen variable names and values for the following filed in python:

Your initials
Population of your hometown
Population on Earth
The current weekday
Duration of the course
The number pi
Write a nice text that uses all the information-values above. Format them into one (or multiple) 
f-strings and print the descriptive string(s) in the console.

Hint:

my_string = “Hello”

print(f”{my_string} world!”)
"""

# Importing necessary libraries
import math

initials = 'mcvk'
population_city = 7692
population_earth = 7982631536
weekday = 'friday'
duration_course = '12 weeks'
pi = math.pi

text = f'''My initials are { initials } and I live in a city with the population of 
{ population_city }, which is almost nothing compared to the population on earth
{ population_earth }. These numbers were taken this { weekday } on October the 21st.
And will most likely change during the duration of this course, which is {duration_course}.
Also, I almost forgot to mention that pi is equal to roughly { pi }.'''

print(text)
