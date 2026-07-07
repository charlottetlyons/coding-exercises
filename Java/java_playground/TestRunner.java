import java.util.HashMap;

import test.ITest;
import test.designpatterns.behavioral.AdapterTest;
import test.designpatterns.behavioral.MementoTest;
import test.designpatterns.behavioral.ObserverTest;
import test.designpatterns.behavioral.StateTest;
import test.designpatterns.behavioral.TemplateTest;
import test.designpatterns.creational.PrototypeTest;
import test.designpatterns.creational.SingletonTest;
import test.designpatterns.structural.CompositeTest;

public class TestRunner {
    public static void main(String[] args) {
        System.out.println("Configuring tests...");
        HashMap<String, ITest> tests = new HashMap<String, ITest>();

        AdapterTest adapterTest = new AdapterTest();
        CompositeTest compositeTest = new CompositeTest();
        MementoTest mementoTest = new MementoTest();
        ObserverTest observerTest = new ObserverTest();
        PrototypeTest prototypeTest = new PrototypeTest();
        SingletonTest singletonTest = new SingletonTest();
        StateTest stateTest = new StateTest();
        TemplateTest templateTest = new TemplateTest();
        
        tests.put("Adapter", adapterTest);
        tests.put("Composite", compositeTest);
        tests.put("Memento", mementoTest);
        tests.put("Observer", observerTest);
        tests.put("Prototype", prototypeTest);
        tests.put("Singleton", singletonTest);
        tests.put("State", stateTest);
        tests.put("Template", templateTest);

        System.out.println("Running...");
        tests.forEach((name, test) -> {
            String result = name.concat(": ").concat(test.runTest() ? "\u001B[32mPass\u001B[0m" : "\u001B[31mFail\u001B[0m");  
            System.out.println(result);
        });
        System.out.println("DONE");
    }
}

