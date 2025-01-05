package src.designpatterns.behavioral.state;

public class ConcreteStateB implements State {
    
    public ConcreteStateB() {}

    @Override
    public int handle() {
        return 20;
    }
}