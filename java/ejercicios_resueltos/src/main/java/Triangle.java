// Static method can be called without creating objects
// Public method must be called by creating objects

public class Triangle {
    // Attributes
    double base;
    double height;
    double area;

    // Constructor. Is called when an object of a class is created
    public Triangle(){
        area = 0;
    }

    public double getBase() {
        return base;
    }

    public void setBase(double base) {
        this.base = base;
    }

    public double getHeight() {
        return height;
    }

    public void setHeight(double height) {
        this.height = height;
    }

    public double getArea() {
        area = (base * height) / 2;
        setArea(area);
        return area;
    }

    public void setArea(double area) {
        this.area = area;
    }

    public String resultMessage() {
        return "Area of triangle with base " + base + " and height " + height + " is: " + area;
    }
}
