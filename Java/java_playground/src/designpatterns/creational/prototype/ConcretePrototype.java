package designpatterns.creational.prototype;

public class ConcretePrototype implements Prototype {

    private int state;

    public ConcretePrototype(int s) {
        this.state = s;
    }

    @Override
    public Prototype clone() {
        return new ConcretePrototype(this.state);
    }
}
