package designpatterns.behavioral.template;

public abstract class Template {
    public int execute() {
        int total = 0;
        total += stepOne() + stepTwo() + stepThree();
        return total;
    };
    
    abstract int stepOne();
    abstract int stepTwo();
    abstract int stepThree();
}
