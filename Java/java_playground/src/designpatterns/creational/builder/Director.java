package designpatterns.creational.builder;

public class Director {
    public void runBuilder() {
        ProductBuilder productBuilder = new ProductBuilder();

        Product result = productBuilder.name("Charlotte").value(1).build();
        
        System.out.println(result.getName());
    }
}
