import java.io.*;
import java.util.ArrayList;
import java.util.Collections;

class Resource {

	/*
	 * Amount of the RAM in the system (im MB)
	 * Begin and End is the delimiters of the available time (in seconds)
	 * Elapsed time since the time 0 of the program (in seconds)
	 */
	private int amount;
	private int begin;
	private int end;
	private long elapsedTime;

	//private long now = 0;

	/*
	 * Just a default constructor
	 */
	public Resource() {
		this.amount = 16384;
		this.elapsedTime = this.begin = 0; // 00:00
		this.end = 86400; // 24:00
	}

	public Resource(int amount, int begin, int end) {
		this.amount = amount;
		this.elapsedTime = this.begin = begin;
		this.end = end;
	}

	public void setAmount(int amount) {
		this.amount = amount;
	}

	public void setBegin(int begin) {
		this.elapsedTime = this.begin = begin;
	}

	public void setEnd(int end) {
		this.end = end;
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

	public long getElapsedTime() {
		return elapsedTime;
	}

	/*
	 * Returns the  amount of time that the resource was active (in seconds)
	 * 86400 is the seconds in one day
	 */
	private long getUsage() {
		long x = (int) (this.elapsedTime / 86400) * getTimePerDay();
		if (this.elapsedTime % 86400 >= this.end) {
			x += getTimePerDay();
		} else {
			x += (this.elapsedTime % 86400) - this.begin;
		}
		return x;
	}

	/*
	 * Returns the available time per day
	 */
	private int getTimePerDay() {
		return this.end - this.begin;
	}

	/*
	 * Returns the non available time per day
	 */
	private int getRestPerDay() {
		return 86400 - getTimePerDay();
	}

	/*
	 * Returns the available second of the day
	 * The end variable controls how the number will return
	 * If it ends at the end mark, will show the end time and not the begin time
	 */
	private long getSecDay(boolean end) {
		long x = (this.begin + getUsage()) % getTimePerDay();
		if (end && x % getTimePerDay() == 0) {
			x = getEnd();
		}
		return x;
	}

	/*
	 * Returns the day of a available second
	 * The end variable controls how the number will return
	 * If it ends at the end mark, will show the current day and not the next one
	 */
	private long getDay(boolean end) {
		long usage = getUsage();
		long x = usage / getTimePerDay();
		if (end && usage % getTimePerDay() == 0) {
			x--;
		}
		return x;
	}

	/*
	 * Add the seconds to the variable and returns the begin and the end of the task
	 * out[0] - The second of the start
	 * out[1] - The day of the start
	 * out[2] - The second of the end
	 * out[3] - The day of the end
	 */
	public long[] setMoment(long begin, int time) {
		long out[] = new long[4];
		if (begin <= this.elapsedTime) {
			long x = this.getSecDay(false);
			out[0] = x;
			out[1] = this.getDay(false);
			if (x + time > getTimePerDay()) {
				this.elapsedTime +=
					time + (int) (time / getTimePerDay()) * getRestPerDay();
			} else {
				this.elapsedTime += time;
			}
			out[2] = getSecDay(true);
			out[3] = this.getDay(true);
		} else {
			this.elapsedTime = begin;
			long newBegin = this.elapsedTime % 86400;
			if (newBegin < this.end) {
				out = setMoment(newBegin, time);
			} else {
				this.elapsedTime += 86400 - newBegin;
				out = setMoment(newBegin, time);
			}
		}
		return out;
	}
}

class Task {

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

	public static String toString(Task current, Resource resource) {
		long data[] = resource.setMoment(current.getBegin(), current.getTime());
		return (
			"Task " +
			current.getName() +
			" will start at " +
			secToTime(data[0]) +
			" on day " +
			(int) data[1] +
			" and will end at " +
			secToTime(data[2]) +
			" on day " +
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
					out.append(toString(tasks.remove(0), resource) + '\n');
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
