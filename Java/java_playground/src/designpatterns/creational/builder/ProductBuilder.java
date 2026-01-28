package designpatterns.creational.builder;

public class ProductBuilder implements IBuilder {
    private String name = "DEFAULT";
    private int value = 0;

    public void clear() {
        this.name = "DEFAULT";
        this.name = 0;
    }

    public ProductBuilder name(String name) {
        this.name = name;
        return this;
    }

    public ProductBuilder value(int value) {
        this.value = value;
        return this;
    }

    @Override
    public Product build() {
        return new Product(this.name, this.value);
    }
}
