# Manager
How to use:\
Create a "data.yaml" file in the same directory as the python file\
Fill the file with the information about the resource and the tasks as described below\
then run the python file to generate a "results.yaml" file at the same directory with the results.

> ram: number\
> begin: "HH:MM:SS"\
> end: "HH:MM:SS"\
> tasks:
>   - name: task1\
>     begin: "HH:MM:SS"\
>     duration: "HH:MM:SS"\
>     ram: number
>   - name: task2\
>     begin: "HH:MM:SS"\
>     duration: "HH:MM:SS"\
>     ram: number\
> ...