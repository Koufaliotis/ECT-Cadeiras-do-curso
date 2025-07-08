
import java.time.LocalDateTime;

public class Transaction implements Comparable<Transaction> {//implements Comparable<Transaction>
    private static int idInc =0;
    private int id;
    private double horas;
    private String descrição;
    private LocalDateTime data; //<-----------------------------problem must be a class?
    
        //how to add id?????????    
    public Transaction(String descrição,String data,double horas){
        //create class here no 2025-05-28 05:00:00
        String[]timeSplit;
        String[] Date;
        String[] Time;
        timeSplit = data.split(" ");
        Date = timeSplit[0].split("-");
        Time = timeSplit[1].split(":");
        LocalDateTime date;
        if(Time.length == 3){
                      date = LocalDateTime.of(Integer.parseInt(Date[0]),
                                              Integer.parseInt(Date[1]),
                                              Integer.parseInt(Date[2]),
                                              Integer.parseInt(Time[0]),
                                              Integer.parseInt(Time[1]),
                                              Integer.parseInt(Time[2]));
        }
        else{         date = LocalDateTime.of(Integer.parseInt(Date[0]),
                                              Integer.parseInt(Date[1]),
                                              Integer.parseInt(Date[2]),
                                              Integer.parseInt(Time[0]),
                                              Integer.parseInt(Time[1]),
                                              0);}
        
        this.id =idInc++;
        this.horas = horas;
        this.descrição = descrição;
        this.data = date;
    }
    public int getID() {
        return id;
    }

    public double getHoras() {
        return horas;
    }

    public String getDescrição() {
        return descrição;
    }

    public LocalDateTime getDate() {
        return data;
    }

    public void setID(int id) {
        this.id = id;
    }

    public void setHoras(double horas) {
        this.horas = horas;
    }

    public void setDescrição(String descrição) {
        this.descrição = descrição;
    }

    public void setDate(LocalDateTime data) {//LocalDateTime
        this.data = data;

    }

    @Override
    public String toString() {
        return "Transaction [horas=" + horas + ", descrição=" + descrição + ", date=" + data.toString() + "]";
        
    }
    @Override
     public int compareTo(Transaction o) {//how to make this work
        //Compare by date first
        int dateCompare = this.data.compareTo(o.data);
        if (dateCompare != 0) {
            return dateCompare;
        }
        
         //If dates are equal, compare by calculated cost
        StandardTransactionCostCalculator calculator = new StandardTransactionCostCalculator();
        double cost1 = calculator.calculateTransactionCostByDate(this.data);
        double cost2 = calculator.calculateTransactionCostByDate(o.data);
        
        return Double.compare(cost1, cost2);
    //--------------------------------
    //public int compareTo(Transaction o) {
        
      //  int compareDateYear =Integer.compare(getDate().getYear(),o.getDate().getYear());  
        
        //if (compareDateYear != 0) {
          //  return compareDateYear;
        //}
              
//        int compareDateMonth = Integer.compare(getDate().getMonthValue(),o.getDate().getMonthValue());

  //      if (compareDateMonth != 0) {
    //        return compareDateMonth;
      //  }

        //int compareDateDay = Integer.compare(getDate().getDayOfMonth(),o.getDate().getDayOfMonth());
        
        //if (compareDateDay != 0) {
          //  return compareDateDay;
        //}
        //StandardTransactionCostCalculator calculator = new StandardTransactionCostCalculator();
        //double d1 = calculator.calculateTransactionCostByDate(getDate());
        //double d2 = calculator.calculateTransactionCostByDate(o.getDate());
        //double compareValeu = Double.compare(d1,d2);
        //if (compareValeu != 0){
        //    return Integer.parseInt(compareValeu + "");
        //}
        //return Integer.parseInt(compareValeu + "");
        //value
    }

    
}
