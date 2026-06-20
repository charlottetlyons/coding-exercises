package test.designpatterns.behavioral;

import src.designpatterns.behavioral.adapter.Adaptee;
import src.designpatterns.behavioral.adapter.Adapter;
import test.test.ITest;

public class AdapterTest implements ITest {
    @Override
    public boolean runTest() {
        Adaptee adaptee = new Adaptee();
        Adapter adapter = new Adapter(adaptee);
        return adapter.execute() == 89374432;
    }
};
