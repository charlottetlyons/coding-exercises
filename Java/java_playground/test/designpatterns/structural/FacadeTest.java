package test.designpatterns.structural;

import src.designpatterns.structual.facade.Facade;
import src.designpatterns.structual.facade.SubsystemA;
import src.designpatterns.structual.facade.SubsystemB;
import src.designpatterns.structual.facade.SubsystemC;
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
