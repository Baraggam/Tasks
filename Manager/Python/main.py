import input_handler
import task
import resource
import utility

input_file_path = "data.yaml"
input_data = input_handler.load_from_line(input_file_path)


# path = pathlib.Path().resolve()
# fileIn = open(str(path) + "/tasks.in", "r")
# fileOut = open(str(path) + "/tasks.out", "w")
# tasks = []
# resource = Resource()
# # Type in the amount of RAM
# resource.setAmount(int(fileIn.readline()))
# # Type in the begin time
# resource.setBegin(timeToSec(fileIn.readline()))
# # Type in the end time
# resource.setEnd(timeToSec(fileIn.readline()))
# while True:
#     try:
#         # Type in the tasks one per line
#         s_params = fileIn.readline().split(" ")
#         tasks.append(Task(s_params[0], timeToSec(
#             s_params[1]), int(s_params[2]), int(s_params[3])))
#         fileOut.write(toString(tasks.pop(0), resource) + '\n')
#     except:
#         break
# fileIn .close()
# fileOut.close()
