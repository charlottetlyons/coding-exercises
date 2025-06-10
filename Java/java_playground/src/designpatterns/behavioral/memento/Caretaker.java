package designpatterns.behavioral.memento;

public class Caretaker {
    private List mementos = new ArrayList();

    public saveMemento(String state) {
        this.mementos.add(new Memento(state));
    }

    public Memento get(int index) {
        this.mementos.get(index);
    }
}
