package test.designpatterns.behavioral;

import designpatterns.behavioral.memento.Caretaker;
import designpatterns.behavioral.memento.Originator;
import src.designpatterns.behavioral.adapter.*;

import test.Test;

public class AdapterTest implements Test {
    @Override
    public boolean runTest() {
        Originator originator = new Originator();
        Caretaker caretaker = new Caretaker();
        
        originator.setState("test1");
        caretaker.saveMemento(originator.saveState());
        originator.saveState("test2");
        boolean result1 = originator.getState() == "test2";
        originator.restoreState(caretaker.get(0));
        return result1 && originator.getState() == "test1";
    }
};
