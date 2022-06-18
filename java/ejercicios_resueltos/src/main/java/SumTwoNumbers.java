import java.util.Scanner;

// Write a Java program that takes two numbers and display the sum of two numbers

public class SumTwoNumbers {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Insert 1st number: ");
        int num1 = input.nextInt(); // User input

        System.out.print("Insert 2nd number: ");
        int num2 = input.nextInt(); // User input

        int sumOfTwo = num1 + num2;
        String output_message = "Sum of " + num1 + " + " + num2 + " = " + sumOfTwo;

        System.out.println(output_message);
    }
}
