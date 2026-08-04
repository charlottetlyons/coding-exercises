package test.designpatterns.behavioral;

import designpatterns.behavioral.template.Subject;
import test.ITest;

public class TemplateTest implements ITest {

    @Override
    public boolean runTest() {
        Subject subject = new Subject();
        return subject.runTemplates() == 21;
    }
    
}
