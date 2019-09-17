package petClass;         // created by Eclipse, throws error if removed
import java.util.Scanner; // prep for input
import java.util.regex.*; // prep for re search of records file
import java.io.File;      // prep for file management

public class Pet {
   // create class fields
   private static String petType;
   private static String petName;
   private static int    petAge;
   private static int    dogSpace;
   private static int    catSpace;
   private static int    daysStay;
   private static int    amountDue;
   private static Scanner scnr = new Scanner(System.in);
	
   Pet() {
      petType = "";
      petName = "";
      petAge = 0;
      dogSpace = 0;
      catSpace = 0;
      daysStay = 0;
      amountDue = 0;
   } // constructor

   Pet(String animalType, String animalName, int animalAge, int dogRoom, int catRoom, int boardingDuration) {
      petType = animalType;
      petName = animalName;
      petAge = animalAge;
      if (animalType.toLowerCase() == "dog") {
         dogSpace = dogRoom;
      }
      else {
         catSpace = catRoom;
      }
      daysStay = boardingDuration;
      amountDue = 0;
   } // overloaded constructor
   
	public static void checkIn() {
		// setter function, user input prompts for each var
		System.out.println("Type of Pet: ");
		petType = scnr.next();
		System.out.println("Pet Name: ");
		petName = scnr.next();
		System.out.println("Age of pet: ");
		petAge = scnr.nextInt();
		System.out.println("Days " + petName + " is staying: ");
		daysStay = scnr.nextInt();
		// assign pet a room
		if (petType.toLowerCase() == "dog") {
			System.out.println("Dog room: ");
			dogSpace = scnr.nextInt();
		}
		else {
			System.out.println("Cat room: ");
			catSpace = scnr.nextInt();
		}
   }
	
   public static void checkOut(String animalName, int roomNumber) {
		//FIXME: Add Method code
   }
   public static String [] getPet() {
      // getter function, create an array of strings and return all vars in that array
	  String petVars [] = {
         petName,
         petType,
         //convert ints to strings for return array
         "" + petAge,
         "" + dogSpace,
         "" + catSpace,
         "" + daysStay,
         "" + amountDue
      };
      return petVars;
   }
   
   public static void createPet() {
	   //FIXME: add method code
	   //FIXME: add file management create new file if petRecords.txt doesn't exist
	   //FIXME: add file management appent current pet information if petRecords.txt does exist
   }
   
   public static void updatePet(String animalName, String animalRoom) {
	   //FIXME: add file management OPEN petRecords.txt mode READ into array 
	   //FIXME: add fileManagement CLOSE petRecords.txt
	   //FIXME: add re search petRecord array for animalName and animalRoom
	   //FIXME: add code for changing pet variables
	   //FIXME: add fileManagement OPEN petRecords.txt mode WRITEALL
	   //FIXME: output entire petRecord array into petRecords.txt
	   //FIXME: add file management CLOSE petRecords.txt
   }
}