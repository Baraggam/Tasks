# Manager
How to use:\
Create a "data.yaml" file in the same directory as the python file\
Fill the file with the information about the resource and the tasks as described below\
"\
ram: 10000\
begin: "56:00:54"\
end: "80:02:00"\
tasks:\
  - name: task1\
    begin: "81:00:00"\
    duration: "00:00:01"\
    ram: 5\
  - name: task2\
    begin: "90:00:00"\
    duration: "00:10:49"\
    ram: 5\
  ...\
"\
Run the python file\
This will generate a "results.yaml" file at the same directory with the results.