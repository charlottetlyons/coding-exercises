package src.designpatterns.behavioral.observer;

import java.util.ArrayList;
import java.util.List;

public class ConcreteSubject implements Subject {
    private List<Observer> observers = new ArrayList<Observer>();

    @Override
    public int updateAll() {
        int total = 0;
        for (Observer observer : observers) {
            total += observer.update();
        }
        return total;
    }

    @Override
    public void add(Observer o) {
        observers.add(o);
    };

    @Override
    public void remove(Observer o) {
        observers.remove(o);
    };
}
