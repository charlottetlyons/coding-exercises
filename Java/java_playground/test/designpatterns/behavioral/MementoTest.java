package test.designpatterns.behavioral;

import src.designpatterns.behavioral.memento.Caretaker;
import src.designpatterns.behavioral.memento.Originator;
import test.test.ITest;

public class MementoTest implements ITest {
    @Override
    public boolean runTest() {
        Originator originator = new Originator();
        Caretaker caretaker = new Caretaker();
        
        originator.setState("test1");
        caretaker.saveMemento(originator.saveMemento());
        originator.setState("test2");
        boolean result1 = originator.getState() == "test2";
        originator.restoreMemento(caretaker.getMemento(0));
        return result1 && originator.getState() == "test1";
    }
};
