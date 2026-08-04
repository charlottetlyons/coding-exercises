package test.designpatterns.creational;

import designpatterns.creational.prototype.ConcretePrototype;
import designpatterns.creational.prototype.Prototype;
import test.ITest;

public class PrototypeTest implements ITest {

    @Override
    public boolean runTest() {
        ConcretePrototype prototype = new ConcretePrototype(4);
        Prototype clone = prototype.clone();
        return clone instanceof Prototype & prototype != clone;
    }
}
