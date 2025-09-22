package java_playground.src.designpatterns.behavioral.memento;

public class Originator {
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
