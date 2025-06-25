package designpatterns.behavioral.adapter;

import src.designpatterns.behavioral.adapter.Target;

public class Adapter implements Target {
    private Adaptee adaptee;
    
    public Adapter(Adaptee a) {
        this.adaptee = a;
    }

    public int doThing() {
        return this.adaptee.doThingComplicated();
    }
}
