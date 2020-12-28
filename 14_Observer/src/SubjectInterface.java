public interface SubjectInterface {
    void attach(ObserverInterface observer);

    void detach(ObserverInterface observer);

    void notify(String message);
}
