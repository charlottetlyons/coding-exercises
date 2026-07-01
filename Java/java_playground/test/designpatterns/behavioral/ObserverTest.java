package test.designpatterns.behavioral;

import src.designpatterns.behavioral.observer.Observer;
import src.designpatterns.behavioral.observer.ConcreteObserver;
import src.designpatterns.behavioral.observer.Subject;
import test.ITest;
import src.designpatterns.behavioral.observer.ConcreteSubject;

public class ObserverTest implements ITest {
    @Override
    public boolean runTest() {
        Observer observerA = new ConcreteObserver();
        Observer observerB = new ConcreteObserver();
        Subject subject = new ConcreteSubject();
        subject.add(observerA);
        subject.add(observerB);
        return subject.updateAll() == 20;
    }
}
