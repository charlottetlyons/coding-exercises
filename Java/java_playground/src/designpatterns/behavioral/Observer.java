package src.designpatterns.behavioral;

import java.util.ArrayList;
import java.util.List;

interface Observer {
    void update();
}

interface Subject {
    void attach(Observer o);
    void detach(Observer o);
    void updateAll();
}

class ObserverA implements Observer {
    @Override
    public void update() {
        System.out.println("Observer A notified");
    }
}

class ObserverB implements Observer {
    @Override
    public void update() {
        System.out.println("Observer B notified");
    }
}

class ConcreteSubject implements Subject { 
    private List<Observer> observers = new ArrayList<Observer>();

    @Override
    public void attach(Observer o) {
        observers.add(o);
    };

    @Override
    public void detach(Observer o) {
        observers.remove(o);
    };

    @Override
    public void updateAll() {
        for (Observer observer : observers) {
            observer.update();
        }
    };
}
