package java_playground.src.designpatterns.structual;

class SubsystemA {
    public void operationA() {};
}
class SubsystemB {
    public void operationB() {};
}
class SubsystemC {
    public void operationC() {};
}

class Facade {
    private SubsystemA subsystemA;
    private SubsystemB subsystemB;
    private SubsystemC subsystemC;

    public Facade() {
        subsystemA = new SubsystemA();
        subsystemB = new SubsystemB();
        subsystemC = new SubsystemC();
    }

    public void operation() {
        subsystemA.operationA();
        subsystemB.operationB();
        subsystemC.operationC();
    }
}

class Client {
    public static void main(String[] args) {
        Facade facade = new Facade();
        facade.operation();
    }
}