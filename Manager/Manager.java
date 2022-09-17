import java.io.*;
import java.util.ArrayList;
import java.util.Collections;

class Resource {

  /*
   * Amount of the RAM in the system (im MB)
   * Begin and End is the delimiters of the available time (in seconds)
   * Now is the time that the resource was active
   * Elapsed time since the time 0 of the program (in seconds)
   */
  private int amount;
  private int begin;
  private int end;
  private int timePerDay = -2;
  private long elapsedTime;
  private long now = 0;

  /*
   * Just a default constructor
   */
  public Resource() {
    this.amount = 16384;
    this.elapsedTime = this.begin = 0; // 00:00
    this.end = 86400; // 24:00
    this.setTimePerDay();
  }

  public Resource(int amount, int begin, int end) {
    this.amount = amount;
    this.elapsedTime = this.begin = begin;
    this.end = end;
    this.setTimePerDay();
  }

  public void setAmount(int amount) {
    this.amount = amount;
  }

  public void setBegin(int begin) {
    this.elapsedTime = this.begin = begin;
    this.setTimePerDay();
  }

  public void setEnd(int end) {
    this.end = end;
    this.setTimePerDay();
  }

  private void setTimePerDay() {
    if (this.begin > 0 && this.end > 0) {
      this.timePerDay = this.end - this.begin;
    }
  }

  /*
   * Add the seconds to the variables and returns the begin and the end of the task
   */
  public long[] setNow(int begin, int time) {
    long out[] = new long[4];
    if (begin <= this.elapsedTime) {
      out[0] = this.now;
      out[1] = this.getDay();
      this.now += time;
      this.elapsedTime += time;
    } else {
      this.elapsedTime = begin;
      this.now =
        (((int) (this.elapsedTime / 86400)) * this.timePerDay) +
        (this.elapsedTime % 86400);
      out[0] = this.now;
      out[1] = this.getDay();
      this.now += time;
      this.elapsedTime += time;
    }
    out[0] = getTimeAtDay(out[0]);
    out[2] = getTimeAtDay(this.now);
    out[3] = this.getDay();
    return out;
  }

  public int getAmount() {
    return this.amount;
  }

  public int getBegin() {
    return this.begin;
  }

  public int getEnd() {
    return this.end;
  }

  public long getNow() {
    return this.now;
  }

  public long getElapsedTime() {
    return elapsedTime;
  }

  private long getTimeAtDay(long now) {
    return this.begin + now % this.timePerDay;
  }

  private long getDay() {
    return this.now / this.timePerDay;
  }
}

class Task implements Comparable<Task> {

  private String name;
  private int begin;
  private int time;
  private int resource;

  public Task(String name, int begin, int time, int resource) {
    this.name = name;
    this.begin = begin;
    this.time = time;
    this.resource = resource;
  }

  public void setName(String name) {
    this.name = name;
  }

  public void setBegin(int begin) {
    this.begin = begin;
  }

  public void setTime(int time) {
    this.time = time;
  }

  public void setResource(int resource) {
    this.resource = resource;
  }

  public String getName() {
    return this.name;
  }

  public int getBegin() {
    return this.begin;
  }

  public int getTime() {
    return this.time;
  }

  public int getResource() {
    return this.resource;
  }

  public String print(String start, int first, String end, int last) {
    return (
      "Task " +
      this.name +
      " will start at " +
      start +
      " on day " +
      first +
      " and will end at " +
      end +
      " on day " +
      last
    );
  }

  /*
   * Cost of a task
   */
  double cost() {
    return time / resource;
  }

  @Override
  public int compareTo(Task task) {
    return this.cost() < task.cost() ? -1 : 1;
  }
}

public class Manager {

  public static int timeToSec(String time) {
    int sec = 0;
    String temp[] = time.split(":");
    sec += Integer.valueOf(temp[0]) * 3600; // Seconds in 1 hour
    sec += Integer.valueOf(temp[1]) * 60; // Seconds in 1 minute
    sec += Integer.valueOf(temp[2]); // 1 second
    return sec;
  }

  public static String secToTime(long sec) {
    long hour = sec / 3600; //Hour
    long min = (sec - hour * 3600) / 60; // Minute
    long seconds = sec % 60; // Second
    String temp = fill(hour) + ":" + fill(min) + ":" + fill(seconds);

    return temp;
  }

  public static String fill(long time) {
    String out = String.valueOf(time);
    if (out.length() < 2) {
      out = "0" + out;
    }
    return out;
  }

  public static String print(Task current, Resource resource) {
    long data[] = resource.setNow(current.getBegin(), current.getTime());
    return current.print(
      secToTime(data[0]),
      (int) data[1],
      secToTime(data[2]),
      (int) data[3]
    );
  }

  public static void main(String[] args) throws Exception {
    try {
      String path = System.getProperty("user.dir");
      RandomAccessFile in = new RandomAccessFile(path + "/tasks.in", "r");
      FileWriter out = new FileWriter(path + "/tasks.out");
      out.write("");

      ArrayList<Task> tasks = new ArrayList<Task>();
      Resource resource = new Resource();
      //Type in the amount of RAM
      resource.setAmount(Integer.valueOf(in.readLine()));
      //Type in the begin time
      resource.setBegin(timeToSec(in.readLine()));
      //Type in the end time
      resource.setEnd(timeToSec(in.readLine()));
      while (true) {
        try {
          String[] s_params = in.readLine().split(" ");
          //Type in the tasks one per line
          tasks.add(
            new Task(
              s_params[0],
              timeToSec(s_params[1]),
              Integer.valueOf(s_params[2]),
              Integer.valueOf(s_params[3])
            )
          );
          out.append(print(tasks.remove(0), resource) + '\n');
        } catch (Exception e) {
          break;
        }
      }
      in.close();
      out.close();
    } catch (Exception e) {
      System.out.println(e);
    }
  }
}
