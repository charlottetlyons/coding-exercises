package src.designpatterns.behavioral.state;

public class ConcreteStateA implements State {

    public ConcreteStateA() {};

    @Override
    public int handle() {
        return 10;
    };
}