package java_playground.src.designpatterns.behavioral;

interface Target {
    void execute();
}

class Adapter implements Target {
    private Adaptee adaptee;

    public Adapter(Adaptee a) {
        this.adaptee = a;
    }

    @Override
    public void execute() {
        this.adaptee.doThingComplicated();
    }
}

class Adaptee {
    public void doThingComplicated() {
        System.err.println("something");
    }
}
