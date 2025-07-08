import java.time.LocalDateTime;
import java.util.ArrayList;
public class StandardTransactionCostCalculator implements ITransactionCostCalculator {

    public StandardTransactionCostCalculator(){}

    public double calculateTransactionCost(Transaction t){
        double custo;
        LocalDateTime date = t.getDate();
        ArrayList<String> days2X6 = new ArrayList<>();
        days2X6.add("MONDAY");
        days2X6.add("TUESDAY");
        days2X6.add("THERSDAY");
        days2X6.add("WEDNESDAY");
        days2X6.add("FRAIDAY"); 
        //costo
        if(days2X6.contains(date.getDayOfWeek())){//usar date
            custo = 50*t.getHoras();
            //desconto de quinta feira
            if (date.getDayOfWeek().equals("WEDNESDAY")) {
                custo = custo - custo*0.1;
                return custo;
            }
            return custo;
        }
        else{//fim de semana
            custo = 2*(50*t.getHoras());
            return custo;
        }
    }
    public double calculateTransactionCostByDate(LocalDateTime date){
        double custo;
        ArrayList<String> days2X6 = new ArrayList<>();
        days2X6.add("MONDAY");
        days2X6.add("TUESDAY");
        days2X6.add("THERSDAY");
        days2X6.add("WEDNESDAY");
        days2X6.add("FRAIDAY"); 
        //costo
        if(days2X6.contains(date.getDayOfWeek())){//usar date
            custo = 50*date.getHour();
            //desconto de quinta feira
            if (date.getDayOfWeek().equals("WEDNESDAY")) {
                custo = custo - custo*0.1;
                return custo;
            }
            return custo;
        }
        else{//fim de semana
            custo = 2*(50*date.getHour());
            return custo;
        }
    }
}
