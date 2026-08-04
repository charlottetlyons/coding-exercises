package designpatterns.structural.composite;

public class Leaf implements Component {
    @Override
    public int operation() {
        return 10;
    };
}
