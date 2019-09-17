package petClass; //created by Eclipse, throws error if removed
import java.util.Scanner; // prep for input

public class Dog extends Pet {
	//create class fields
	public static int dogSpaceNbr;
	public static int dogWeight;
	public static boolean grooming;
	public static Scanner scnr = new Scanner(System.in);
	
	Dog() {
		dogSpaceNbr = 0;
		dogWeight = 0;
		grooming = false;
	} // Constructor
	
	Dog(int room, int weight, boolean toBeGroomed) {
		dogSpaceNbr = room;
		dogWeight = weight;
		grooming = toBeGroomed;
	} // overloaded constructor
	
	public static void setGrooming() {
		//setter function, create a prompt and set the var
		System.out.println("Pet to be groomed?: ");
		grooming = scnr.nextBoolean();
	}
	
	public static void setDogWeight() {
		//setter function, create a prompt and set the var
		System.out.println("Pet weight: ");
		dogWeight = scnr.nextInt();
	}
	
	public static boolean getGrooming() {
		//getter function, just return the value of the var
		return grooming;
	}
	
	public static int getWeight() {
		//getter function, just return the value of the var
		return dogWeight;
	}
}