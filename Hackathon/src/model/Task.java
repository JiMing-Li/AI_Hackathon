package model;
import java.sql.*;
import java.util.List;

public class Task {

	public String name;
	public double predictDuration;
	public double actualDuration;
	public boolean completion;
	public boolean fixed;
	
	public Date startDate;
	public Time startTime;
	public Date endDate;
	public Time endTime;
	
	public static List<Task> tasks;
	
	public Task(String n, double d, boolean c, boolean f) {
		name = n;
		predictDuration = d;
		completion = c;
		fixed = f;
	}
	
	
}
