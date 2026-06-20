import java.util.HashMap;

import test.designpatterns.behavioral.AdapterTest;
import test.designpatterns.behavioral.MementoTest;
import test.designpatterns.behavioral.StateTest;
import test.test.ITest;

public class TestRunner {
    public static void main(String[] args) {
        System.out.println("Configuring tests...");
        HashMap<String, ITest> tests = new HashMap<String, ITest>();

        AdapterTest adapterTest = new AdapterTest();
        MementoTest mementoTest = new MementoTest();
        StateTest stateTest = new StateTest();
        
        tests.put("Adapter", adapterTest);
        tests.put("Memento", mementoTest);
        tests.put("State", stateTest);

        System.out.println("Running...");
        tests.forEach((name, test) -> {
            String result = name.concat(": ").concat(test.runTest() ? "\u001B[32mPass\u001B[0m" : "\u001B[31mFail\u001B[0m");  
            System.out.println(result);
        });
        System.out.println("DONE");
    }
}

