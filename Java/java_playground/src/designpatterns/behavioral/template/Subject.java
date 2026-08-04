package designpatterns.behavioral.template;

public class Subject {
    Template templateA = new TemplateA();
    Template templateB = new TemplateB();

    public int runTemplates() {
        return templateA.execute() + templateB.execute();
    }
    
}
