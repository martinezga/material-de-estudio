import java.util.Scanner;

// Write a Java program to find area of triangle

public class AreaOfTriangle {
    public static void main(String[] args){
    Triangle triangleObj = new Triangle();
    Scanner input = new Scanner(System.in);

    System.out.print("Enter the width of the Triangle: ");
    double base = input.nextDouble();
    System.out.print("Enter the height of the Triangle: ");
    double height = input.nextDouble();

    triangleObj.setBase(base);
    triangleObj.setHeight(height);
    triangleObj.getArea();
    System.out.println(triangleObj.resultMessage());
    }
}
