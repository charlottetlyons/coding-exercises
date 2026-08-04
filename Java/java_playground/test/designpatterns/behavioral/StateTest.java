package test.designpatterns.behavioral;

import designpatterns.behavioral.state.ConcreteStateA;
import designpatterns.behavioral.state.ConcreteStateB;
import designpatterns.behavioral.state.Context;
import test.ITest;

public class StateTest implements ITest {
    @Override
    public boolean runTest() {
        boolean resultA;
        boolean resultB;

        ConcreteStateA stateA = new ConcreteStateA();
        ConcreteStateB stateB = new ConcreteStateB();
        Context context = new Context(stateA);
        resultA = context.doThing() == 10;
        context.setState(stateB);
        resultB = context.doThing() == 20;
        return resultA && resultB;
    }
};
