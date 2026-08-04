package designpatterns.creational.builder;

public class Product implements IProduct {

    private int id;
    private int age;
    
    public Product(int i, int a) {
        this.id = i;
        this.age = a;
    }

    @Override
    public int doThing() {
        return this.id + this.age;
    }

}
