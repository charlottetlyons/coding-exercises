package java_playground.src.designpatterns.creational.builder;

interface IBuilder {
    Product build();
}

class ProductBuilder implements IBuilder {
    private int value;

    public ProductBuilder() {};

    public ProductBuilder value(int v) {
        this.value = v;
        return this;
    }

    public Product build() {
        return new Product(value);
    }
}

class Product {
    private int value;

    public Product(int v) {
        this.value = v;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public int getValue() {
        return value;
    }
}
