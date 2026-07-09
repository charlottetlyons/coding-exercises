package src.designpatterns.structual.facade;

public class Facade {
    private SubsystemA subsystemA;
    private SubsystemB subsystemB;
    private SubsystemC subsystemC;

    public Facade(SubsystemA a, SubsystemB b, SubsystemC c) {
        subsystemA = a;
        subsystemB = b;
        subsystemC = c;
    }

    public int execute() {
        return subsystemA.operationsA() + subsystemB.operationsB() + subsystemC.operationsC();
    }
}
