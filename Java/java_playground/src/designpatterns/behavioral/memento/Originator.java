package designpatterns.behavioral.memento;

public class Originator {
    private String state;

    public String getState() {
        return this.state;
    }

    public void setState(String s) {
        this.state = s;
    }

    public Memento saveStateMemento() {
        return new Memento(this.state);
    }

    public void restoreState(Memento m) {
        this.state = m.getState();
    }
}
