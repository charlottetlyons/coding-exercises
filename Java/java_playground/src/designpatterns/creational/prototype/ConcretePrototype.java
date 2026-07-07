package src.designpatterns.creational.prototype;

public class ConcretePrototype implements Prototype {
    private int value;

    public ConcretePrototype(int v) {
        this.value = v;
    }

    @Override
    public Prototype clone() {
        return new ConcretePrototype(this.value);
    }

    @Override
    public boolean equals(Object object) {
        ConcretePrototype other = (ConcretePrototype) object;
        return this.value == other.value;
    }
}
