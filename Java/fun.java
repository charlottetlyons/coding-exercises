import java.util.ArrayList;

import test.Test;
import test.designpatterns.behavioral.StateTest;

public class fun {
    public static void main(String[] args) {
        ArrayList<Test> tests = new ArrayList<Test>();
        StateTest stateTest = new StateTest();
        tests.add(stateTest);

        for (Test test : tests) {
            System.out.println(test.runTest());
        }
    }
}

