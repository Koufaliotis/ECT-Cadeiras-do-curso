import java.util.HashMap;
import java.util.Scanner;
import java.util.TreeSet;
import java.io.File;
import java.io.FileWriter;
public class ConcertManager {
    private HashMap<Integer,Concert> consertList = new HashMap<>();
    public ConcertManager(){

    }
    
    public void addConcert(Concert c){
        int id = c.getId();
        consertList.put(id, c);
    }

    public void removeConcert(int id){
        consertList.remove(id);
    }

    public String getConcert(int id){
        for(int keys : consertList.keySet()){
            if(keys == id){
                return consertList.get(id).toString();
            }
        }
        return null;
    }

    public double calculateConcertCost(int id){
        //use calulator
        double lucro;
        Concert c;
        for(int keys : consertList.keySet()){
            if(keys == id){
                StandardConcertProfitCalculator calc = new StandardConcertProfitCalculator();
                c = consertList.get(id);
                lucro = calc.calculateConcertProfit(c);               
                return lucro; //must return the calculation
            }
        }
        return -1;

    }

    public void printAllConcerts(){
        for(int keys : consertList.keySet()){
            
            System.out.println(consertList.get(keys).toString());
            
        }
    }

    public void sortConcertsByCost(){//sortConcertsByProfit
        //compereTo in Concet
        TreeSet<Concert> myOrderedList = new TreeSet<>();
        for(int keys : consertList.keySet()){
            myOrderedList.add(consertList.get(keys));
        }

        for (Concert c : myOrderedList){
            System.out.println(c.toString() +" lucro"+calculateConcertCost(c.getId()));
        }

    }

    public void readFile(String file){
        String[] data;
        File myfile = new File("src\\" + file);
        //Scanner myreader = new Scanner(myfile)
        try (Scanner myreader = new Scanner(myfile)){
            while (myreader.hasNextLine()) {
                data = myreader.nextLine().split("; ");
                Concert c = new Concert(data[2], data[3], Double.parseDouble(data[1]));
                addConcert(c);             
            }  
        } catch (Exception e) {
            // TODO: handle exception
        }
    }

    public void writeFile(String fich){
        File myfile = new File("src\\" + fich);
        try(FileWriter myWriter = new FileWriter(myfile)) {
            for(int keys : consertList.keySet()){
            myWriter.write(consertList.get(keys).toString()+" lucro"+calculateConcertCost(keys) );
            }
        } catch (Exception e) {
            // TODO: handle exception
        }
        //
    }
    
}
