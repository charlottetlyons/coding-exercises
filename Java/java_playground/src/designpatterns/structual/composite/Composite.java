package src.designpatterns.structual.composite;

import java.util.ArrayList;
import java.util.List;

public class Composite implements Component {
    private List<Component> children = new ArrayList<Component>();

    public int operation() {
        int total = 0;
        for (Component child : children) {
            total += child.operation();
        }
        return total;
    }
    public void add(Component c) {
        children.add(c);
    }
    public void remove(Component c) {
        children.remove(c);
    }
}
