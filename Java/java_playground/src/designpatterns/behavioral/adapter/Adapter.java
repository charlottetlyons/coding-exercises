package java_playground.src.designpatterns.behavioral.adapter;

interface Target {
    void execute();
}

class Adapter extends Target {
    private Adaptee adaptee;

    public Adapter(Adaptee a) {
        this.adaptee = a;
    }

    @Override
    void execute() {
        this.adaptee.doTHing
    }
}

class Adaptee {
    public void doThingComplicated() {
        System.err.println("something");
    }
}
