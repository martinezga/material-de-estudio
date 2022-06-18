import java.util.Scanner;

// Write a Java program to convert minutes to seconds

public class ConvertMinutes2Seconds {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Insert minutes: ");
        int minutes = input.nextInt();

        int seconds = minutes * 60;
        System.out.println(minutes + " minutes into seconds: " + seconds);
    }
}
