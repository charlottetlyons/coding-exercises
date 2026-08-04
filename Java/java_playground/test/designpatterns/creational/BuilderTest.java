package test.designpatterns.creational;

import designpatterns.creational.builder.IProduct;
import designpatterns.creational.builder.ProductBuilder;
import test.ITest;

public class BuilderTest implements ITest {

    @Override
    public boolean runTest() {
        ProductBuilder productBuilder = new ProductBuilder();
        productBuilder.id(1).age(20);
        IProduct product = productBuilder.build();
        return product.doThing() == 21;
    }
    
}
