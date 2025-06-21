package java_playground.src.designpatterns.behavioral.memento;

import java.util.ArrayList;
import java.util.List;

public class Caretaker {
    private List<Memento> mementos = new ArrayList();

    public void saveMemento(Memento m) {
        mementos.add(m);
    }

    public Memento getMemento(int index) {
        return this.mementos.get(index);
    }
}
