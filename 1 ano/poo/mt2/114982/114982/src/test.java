import java.time.LocalDateTime;

public class test {
    public static void main(String[] args) {
        LocalDateTime date1 = LocalDateTime.of(2025, 5, 28, 5, 0,1);
        //LocalDateTime date = new LocalDateTime.of(2025, 5, 28, 0, 0);
        //LocalDateTime date = new LocalDateTime.now("2025-05-28 05:00:00");
        System.out.println("day of the year: "+date1.getDayOfYear());
        System.out.println("day of the weak: " + date1.getDayOfWeek());
        System.out.println(date1.toString());
    }
}
