package java_playground.src.designpatterns.behavioral;

import java.util.ArrayList;
import java.util.List;

class Memento {
    private String state;

    public Memento(String s) {
        this.state = s;
    }

    public String getState() {
        return this.state;
    }
}

class Caretaker {
    private List<Memento> mementos = new ArrayList<Memento>();

    public void saveMemento(Memento m) {
        this.mementos.add(m);
    }

    public Memento getMemento(int index) {
        return this.mementos.get(index);
    }
}

class Originator {
    private String state;

    public String getState() {
        return this.state;
    }

    public void setState(String s) {
        this.state = s;
    }

    public Memento saveMemento() {
        return new Memento(this.state);
    }

    public void restoreMemento(Memento m) {
        this.state = m.getState();
    }
}
