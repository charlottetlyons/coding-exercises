import java.util.HashMap;

import test.Test;
import test.designpatterns.behavioral.AdapterTest;
import test.designpatterns.behavioral.StateTest;

public class TestRunner {
    public static void main(String[] args) {
        HashMap<String, Test> tests = new HashMap<String, Test>();
        StateTest stateTest = new StateTest();
        AdapterTest adapterTest = new AdapterTest();
        
        tests.put("State", stateTest);
        tests.put("Adapter", adapterTest);

        tests.forEach((name, test) -> {
            String result = name.concat(": ").concat(test.runTest() ? "\u001B[32mPass\u001B[0m" : "\u001B[31mFail\u001B[0m");  
            System.out.println(result);
        });
    }
}

