package designpatterns.creational.builder;

public class Product {
    private String name;
    private int value;

    public Product(String n, int v) {
        this.name = n;
        this.value = v;
    }

    public String getName() {
        return name;
    }

    public int getValue() {
        return value;
    }
}
