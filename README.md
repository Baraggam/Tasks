# Manager
How to use:\
Create a "tasks.in" file in the same directory as the java or python file\
Fill the file with the information about the resource and the tasks as described below\
\
ram HH:MM:SS HH:MM:SS # RESOURCE: Ram (in MB), Start, End\
name HH:MM:SS duration resource # TASK: name, begin, end, duration (in seconds), the amount of the resource (in MB)\
name HH:MM:SS duration resource # TASK\
...\
\
Compile one of them and run\
This will generate a "tasks.out" file at the same directory with the results.
