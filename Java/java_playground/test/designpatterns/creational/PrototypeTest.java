package test.designpatterns.creational;

import src.designpatterns.creational.prototype.ConcretePrototype;
import src.designpatterns.creational.prototype.Prototype;
import test.ITest;

public class PrototypeTest implements ITest {

    @Override
    public boolean runTest() {
        Prototype prototype = new ConcretePrototype(4);
        Prototype clone = prototype.clone();
        return prototype.equals(clone) & prototype != clone;
    }
}
