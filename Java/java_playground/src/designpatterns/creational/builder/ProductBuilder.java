package java_playground.src.designpatterns.creational.builder;

public class ProductBuilder implements IProductBuilder {
    private String name = "DEFAULT";
    private int value = 0;

    public ProductBuilder() {};

    public ProductBuilder name(String n) {
        this.name = n;
        return this;
    }

    public ProductBuilder value(int v) {
        this.value = v;
        return this;
    }

    @Override
    public Product build() {
        return new Product(this.name, this.value);
    }
}
