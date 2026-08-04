package test.designpatterns.structural;

import designpatterns.structural.facade.Facade;
import designpatterns.structural.facade.SubsystemA;
import designpatterns.structural.facade.SubsystemB;
import designpatterns.structural.facade.SubsystemC;
import test.ITest;

public class FacadeTest implements ITest {

    @Override
    public boolean runTest() {
        SubsystemA subsystemA = new SubsystemA();
        SubsystemB subsystemB = new SubsystemB();
        SubsystemC subsystemC = new SubsystemC();
        Facade facade = new Facade(subsystemA, subsystemB, subsystemC);
        return facade.execute() == 60;
    }
    
}
