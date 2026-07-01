package test.designpatterns.structural;

import src.designpatterns.structual.composite.*;
import test.ITest;

public class CompositeTest implements ITest {

    @Override
    public boolean runTest() {
        Composite root = new Composite();
        Leaf childA = new Leaf();
        Leaf childB = new Leaf();

        root.add(childA);
        root.add(childB);

        return root.operation() == 20;
    }
    
}
