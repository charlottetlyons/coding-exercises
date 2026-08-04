package designpatterns.creational.builder;

public class ProductBuilder implements IBuilder {
    private int id;
    private int age;
    
    public IProduct build() {
        return new Product(this.id, this.age);
    };

    public ProductBuilder id(int i) {
        this.id = i;
        return this;
    }
    
    public ProductBuilder age(int a) {
        this.age = a;
        return this;
    }
}
