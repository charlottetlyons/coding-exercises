package src.designpatterns.behavioral.adapter;

public class Adapter implements ITarget {
    private Adaptee adaptee;

    public Adapter(Adaptee a) {
        this.adaptee = a;
    }

    @Override
    public int execute() {
        return this.adaptee.doThingComplicated();
    }
}