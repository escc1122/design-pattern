import java.util.ArrayList;
import java.util.List;

public class Subject implements SubjectInterface {
    List<ObserverInterface> aaa = new ArrayList<ObserverInterface>();
    @Override
    public void attach(ObserverInterface observer) {
        aaa.add(observer);
    }

    @Override
    public void detach(ObserverInterface observer) {
        aaa.remove(observer);
    }

    @Override
    public void notify(String message) {
        for ( ObserverInterface bbb: aaa){
            bbb.update(message);
        }
    }
}
