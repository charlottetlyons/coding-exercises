package src.designpatterns.behavioral.state;

public class Context {
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