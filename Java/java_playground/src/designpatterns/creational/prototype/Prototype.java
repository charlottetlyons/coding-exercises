package designpatterns.creational.prototype;
public interface Prototype {
    Prototype clone();
}

class ConcretePrototype implements Prototype {
    private int value;

    public ConcretePrototype(int v) {
        value = v;
    }

    @Override
    public Prototype clone() {
        return new ConcretePrototype(value);
    }
}
