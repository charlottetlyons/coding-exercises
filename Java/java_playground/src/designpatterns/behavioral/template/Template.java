package src.designpatterns.behavioral.template;

public abstract class Template {
    public int execute() {
        return stepOne() + stepTwo() + stepThree();
    };

    abstract int stepOne();
    abstract int stepTwo();
    abstract int stepThree();
}
