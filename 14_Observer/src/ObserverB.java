public class ObserverB implements ObserverInterface {
    @Override
    public void update(String message) {
        System.out.println(this.getClass().getName() + " : " + message);
    }
}
