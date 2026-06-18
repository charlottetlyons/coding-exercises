package java_playground.src.designpatterns.behavioral;

public interface State {
    int handle();
}

class ConcreteStateA implements State {
    @Override
    public int handle() {
        return 10;
    };
}

class ConcreteStateB implements State {
    @Override
    public int handle() {
        return 20;
    };
}

class Context {
    private State state;

    public Context(State s) {
        this.state = s;
    }

    public void setState(State s) {
        this.state = s;
    }

    public int doThing() {
        return this.state.handle();
    }
}