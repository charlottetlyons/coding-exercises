package test.designpatterns.behavioral;

import src.designpatterns.behavioral.adapter.*;

import test.Test;

public class AdapterTest implements Test {
    @Override
    public boolean runTest() {
        Adaptee adaptee = new Adaptee();
        Adapter adapter = new Adapter(adaptee);
        return adapter.doThing() == 1;
    }
};
