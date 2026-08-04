package test.designpatterns.behavioral;

import designpatterns.behavioral.observer.Observer;
import designpatterns.behavioral.observer.ConcreteObserver;
import designpatterns.behavioral.observer.Subject;
import test.ITest;

public class ObserverTest implements ITest {
    @Override
    public boolean runTest() {
        Observer observerA = new ConcreteObserver();
        Observer observerB = new ConcreteObserver();
        Subject subject = new Subject();
        subject.add(observerA);
        subject.add(observerB);
        return subject.updateAll() == 20;
    }
}
