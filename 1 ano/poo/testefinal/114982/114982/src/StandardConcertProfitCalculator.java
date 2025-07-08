public class StandardConcertProfitCalculator implements IConcertProfitCalculator {

    public StandardConcertProfitCalculator(){
        
    }
    public double calculateConcertProfit(Concert c){
        int hora =c.getData().getHour();
        String local =c.getLocal().split(",")[1];
        double lucro;

        if(local.equals("Portugal")||local.equals("Espanha")){
            lucro = 1500 * hora;
            lucro = 2*(lucro);
            return lucro;
        }  
        lucro = (1500 + 800) * hora;
        return lucro;
    }

    
}
