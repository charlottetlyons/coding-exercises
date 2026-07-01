package test.designpatterns.creational;

import src.designpatterns.creational.Singleton;
import test.ITest;

public class SingletonTest implements ITest {

    @Override
    public boolean runTest() {
        Singleton instanceA = Singleton.getInstance();
        Singleton instanceB = Singleton.getInstance();
        int hashA = System.identityHashCode(instanceA);
        int hashB = System.identityHashCode(instanceB);
        return hashA == hashB;
    }
    
}
