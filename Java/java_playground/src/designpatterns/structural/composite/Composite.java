package designpatterns.structural.composite;

import java.util.ArrayList;
import java.util.List;

public class Composite implements Component {

    private List<Component> children = new ArrayList<Component>();

    @Override 
    public int operation() {
        int total = 0;
        for(Component child : children) {
            total += child.operation();
        }
        return total;
    }

    public void add(Component c) {
        this.children.add(c);
    }

    public void remove(Component c) {
        this.children.remove(c);
    }
    
}
