import pathlib


class Resource:
    # Amount of the RAM in the system (im MB)
    # Begin and End is the delimiters of the available time (in seconds)
    # Elapsed time since the time 0 of the program (in seconds)
    def __init__(self) -> None:
        self.__amount = 16384
        self.__begin = self.__elapsedTime = 0
        self.__end = 86400  # 24:00:00

    def setAmount(self, amount) -> None:
        self.__amount = amount

    def setBegin(self, begin) -> None:
        self.__elapsedTime = self.__begin = begin

    def setEnd(self, end) -> None:
        self.__end = end

    def getAmount(self):
        return self.__amount

    def getBegin(self):
        return self.__begin

    def getEnd(self):
        return self.__end

    def getElapsedTime(self):
        return self.__elapsedTime

    # Returns the  amount of time that the resource was active (in seconds)
    # 86400 is the seconds in one day
    def __getUsage(self):
        x = int(self.__elapsedTime / 86400) * self.__getTimePerDay()
        if (self.__elapsedTime % 86400 >= self.__end):
            x += self.__getTimePerDay()
        else:
            x += (self.__elapsedTime % 86400) - self.__begin
        return int(x)

    # Returns the available time per day
    def __getTimePerDay(self):
        return int(self.__end - self.__begin)

    # Returns the non available time per day
    def __getRestPerDay(self):
        return int(86400 - self.__getTimePerDay())

    # Returns the available second of the day
    # The end variable controls how the number will return
    # If it ends at the end mark, will show the end time and not the begin time

    def __getSecDay(self, end):
        x = int(self.__begin + self.__getUsage()) % self.__getTimePerDay()
        if end and x % self.__getTimePerDay() == 0:
            x = self.getEnd()
        return x

    # Returns the day of a available second
    # The end variable controls how the number will return
    # If it ends at the end mark, will show the current day and not the next one

    def __getDay(self, end):
        usage = self.__getUsage()
        x = int(usage / self.__getTimePerDay())
        if end and usage % self.__getTimePerDay() == 0:
            x -= 1
        return x

    # Add the seconds to the variable and returns the begin and the end of the task
    # out[0] - The second of the start
    # out[1] - The day of the start
    # out[2] - The second of the end
    # out[3] - The day of the end
    def setMoment(self, begin, time):
        out = [0] * 4
        if begin <= self.__elapsedTime:
            x = self.__getSecDay(False)
            out[0] = x
            out[1] = self.__getDay(False)
            if x + time > self.__getTimePerDay():
                self.__elapsedTime += time + \
                    int((time / self.__getTimePerDay()) * self.__getRestPerDay())
            else:
                self.__elapsedTime += time
            out[2] = self.__getSecDay(True)
            out[3] = self.__getDay(True)
        else:
            self.__elapsedTime = begin
            newBegin = int(self.__elapsedTime % 86400)
            if newBegin <= self.__end:
                out = self.setMoment(newBegin, time)
            else:
                self.__elapsedTime += 86400 - newBegin
                out = self.setMoment(newBegin, time)
        return out


class Task:
    def __init__(self, name, begin, time, resource) -> None:
        self.__name = name
        self.__begin = begin
        self.__time = time
        self.__resource = resource

    def setName(self, name) -> None:
        self.__name = name

    def setBegin(self, begin) -> None:
        self.__begin = begin

    def setTime(self, time) -> None:
        self.__time = time

    def setResource(self, resource) -> None:
        self.__resource = resource

    def getName(self):
        return self.__name

    def getBegin(self):
        return self.__begin

    def getTime(self):
        return self.__time

    def getResource(self):
        return self.__resource


def timeToSec(time):
    sec = 0
    temp = time.split(":")
    sec += int(temp[0]) * 3600  # Seconds in 1 hour
    sec += int(temp[1]) * 60  # Seconds in 1 minute
    sec += int(temp[2])  # 1 second
    return int(sec)


def secToTime(sec):
    hour = int(sec / 3600)  # Hour
    min = int((sec - hour * 3600) / 60)  # Minute
    seconds = sec % 60  # Second
    temp = fill(hour) + ":" + fill(min) + ":" + fill(seconds)
    return temp


def fill(time):
    out = str(time)
    if len(out) < 2:
        out = "0" + out
    return out


def toString(current, resource):
    data = resource.setMoment(current.getBegin(), current.getTime())
    return "Task " + current.getName() + " will start at " + secToTime(data[0]) + " on day " + str(data[1]) + " and will end at " + secToTime(data[2]) + " on day " + str(data[3])


path = pathlib.Path().resolve()
fileIn = open(str(path) + "/tasks.in", "r")
fileOut = open(str(path) + "/tasks.out", "w")
tasks = []
resource = Resource()
# Type in the amount of RAM
resource.setAmount(int(fileIn.readline()))
# Type in the begin time
resource.setBegin(timeToSec(fileIn.readline()))
# Type in the end time
resource.setEnd(timeToSec(fileIn.readline()))
while True:
    try:
        # Type in the tasks one per line
        s_params = fileIn.readline().split(" ")
        tasks.append(Task(s_params[0], timeToSec(
            s_params[1]), int(s_params[2]), int(s_params[3])))
        fileOut.write(toString(tasks.pop(0), resource) + '\n')
    except:
        break
fileIn .close()
fileOut.close()
