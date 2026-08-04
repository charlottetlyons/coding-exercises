package designpatterns.behavioral.observer;

import java.util.ArrayList;
import java.util.List;

public class Subject {
    private List<Observer> observers = new ArrayList<Observer>();

    public int updateAll() {
        int total = 0;
        for (Observer observer : observers) {
            total += observer.update();
        }
        return total;  
    }

    public void add(Observer o) {
        observers.add(o);
    }

    public void remove(Observer o) {
        observers.remove(o);
    }
}
