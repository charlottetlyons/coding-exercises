package test.designpatterns.behavioral;

import src.designpatterns.behavioral.state.*;
import test.Test;

public class StateTest implements Test {
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
