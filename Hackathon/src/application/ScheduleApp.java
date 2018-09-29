package application;
import view.SchedulePage;;

public class ScheduleApp {
	
	private static ScheduleApp restoapp;
	private static String filename = "menu.resto";
	

	
		
		public static void main(String[] args) {
			// start UI
	        java.awt.EventQueue.invokeLater(new Runnable() {
	            public void run() {
	                new SchedulePage().setVisible(true);
	               
	            }
	        });
	}
	
/*
	public static RestoApp getRestoApp() {
		if (restoapp == null) {
			// load model
			restoapp = load();
		}
 		return restoapp;
	}
	
	public static void save() {
		restoapp.reinitialize();
		PersistenceObjectStream.serialize(restoapp);
	}
	
	public static RestoApp load() {
		PersistenceObjectStream.setFilename(filename);
		restoapp = (RestoApp) PersistenceObjectStream.deserialize();
		// model cannot be loaded - create empty BTMS
		if (restoapp == null) {
			restoapp = new RestoApp();
		}
		else {
			restoapp.reinitialize();
		}
		return restoapp;
	}
	
	public static void setFilename(String newFilename) {
		filename = newFilename;
	}*/

}
