package src.designpatterns.behavioral.observer;

public interface Subject {
    int updateAll();
    void add(Observer o);
    void remove(Observer o);
}
