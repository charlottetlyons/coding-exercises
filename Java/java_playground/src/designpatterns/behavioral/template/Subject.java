package designpatterns.creational.template;

public class Subject {
    private TemplateA templateA = new TemplateA();
    private TemplateB templateB = new TemplateB();

    public Subject() {};

    public int runTemplates() {
        return templateA.execute() + templateB.execute();
    }
}
