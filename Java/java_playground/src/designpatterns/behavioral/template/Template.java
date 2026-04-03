package java_playground.src.designpatterns.behavioral.template;

abstract class Template {
    public final void execute() {
        stepOne();
        stepTwo();
        stepThree();
    };

    abstract void stepOne();
    abstract void stepTwo();
    abstract void stepThree();
}

class TemplateA extends Template {
    @Override
    void stepOne() {
        System.out.println("Template A: Step 1");
    }
    @Override
    void stepTwo() {
        System.out.println("Template A: Step 2");
    }
    @Override
    void stepThree() {
        System.out.println("Template A: Step 3");
    }
}

class TemplateB extends Template {
    @Override
    void stepOne() {
        System.out.println("Template B: Step 1");
    };
    @Override
    void stepTwo() {
        System.out.println("Template B: Step 2");
    };
    @Override
    void stepThree() {
        System.out.println("Template B: Step 3");
    };
}

class Main {
    public static void main(String[] argv) {
        TemplateA templateA = new TemplateA();
        TemplateB templateB = new TemplateB();
        templateA.execute();
        templateB.execute();
    }
}