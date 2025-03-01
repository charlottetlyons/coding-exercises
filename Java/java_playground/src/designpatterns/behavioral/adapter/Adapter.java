package designpatterns.behavioral.adapter;

public class Adapter implements Target {
    private Adaptee adaptee;

    public Adapter(Adaptee a) {
        this.adaptee = a;
    }
    
    @Override
    public doThing() {
        return this.adaptee.doThingComplicated();
    }
}
