package src.designpatterns.behavioral.template;

public class Subject {
    public int runTemplates() {
        TemplateA templateA = new TemplateA();
        TemplateB templateB = new TemplateB();
        return templateA.execute() + templateB.execute();
    };
    
}
