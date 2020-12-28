public class Client {
    public static void main(String[] args){
        SubjectInterface subject = new Subject();
        ObserverInterface a = new ObserverA();
        ObserverInterface b = new ObserverB();

        subject.attach(a);
        subject.attach(b);

        subject.notify("test");

    }
}
