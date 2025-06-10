package designpatterns.behavioral.memento;

public class Originator {
    private String state;

    public void setState(String state) {
        this.state = state;
    }

    public String getState() {
        return this.state;
    }

    public Memento saveState() {
        return new Memento(this.state);
    }

    public void restoreState(Memento m) {
        this.value = m.getMemento();
    }
}
