package src.designpatterns.creational;

interface Prototype {
    Prototype clone();
}

class ConcretePrototype implements Prototype {
    private int value;

    public ConcretePrototype(int v) {
        value = v;
    }

    public Prototype clone() {
        return new ConcretePrototype(value);
    }
}
