import java.util.HashMap;
import java.util.HashSet; 
import java.util.List;
import java.util.Scanner;
import java.util.TreeSet;
import java.io.File;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Comparator;


public class TransactionManager {

    HashMap<Integer,Transaction> trasactionsLst = new HashMap<Integer,Transaction>(); 
    public TransactionManager(){

    }
    public void addTransaction(Transaction t){
        trasactionsLst.put(t.getID(), t);        
    }

    public void removeTransaction(int id){

        for(int keys : trasactionsLst.keySet()){
            if (keys == id) {
                trasactionsLst.remove(id);
                System.out.println("Transaction removed");
            }
        }

    }

    public String getTransaction(int id){

        for(int keys : trasactionsLst.keySet()){
            if (keys == id) {
                Transaction t = trasactionsLst.get(id);
                return t.toString();
            }
            
        }
        return "the trandaction doesnt exist";
    }

    public double calculateTransactionCost(int id){
        for(int keys : trasactionsLst.keySet()){
            if (keys == id) {
                Transaction t = trasactionsLst.get(id);
                StandardTransactionCostCalculator calculator = new StandardTransactionCostCalculator();
                double custo = calculator.calculateTransactionCost(t); //tem de ser aredondado
                return custo;
            }
            
        }
        return -1;
    }

    public void printAllTransactions(){
        Transaction t;
        for(int keys : trasactionsLst.keySet()){
            
            t = trasactionsLst.get(keys);
            System.out.println(t.toString() +" custo: " +calculateTransactionCost(keys));
        }
            
    }

    public void sortTransactionsByCost(){
        //List<Transaction> myOrderdList = new ArrayList<>(trasactionsLst.values());
        TreeSet<Transaction> myOrderdList = new TreeSet<>(); 
        //List<Transaction> myOrderdList = new List<>();
        Transaction t;
        for(int keys : trasactionsLst.keySet()){
            t = trasactionsLst.get(keys);
            myOrderdList.add(t);
        }
        
    
        //Collection.sort(myOrderdList);
        for(Transaction tran  : myOrderdList){
            System.out.println(tran.toString() +" custo: " +calculateTransactionCost(tran.getID()));
        }
        
            //sort by colllection first day then cost;

    }
    
    public void readFile(String file){
        File myFile = new File("src\\" + file);
        String Line;
        String[] data;
        boolean firstLine = true;
        try (Scanner myReader = new Scanner(myFile)){
            
            while (myReader.hasNextLine()) {
                Line = myReader.nextLine();
                data= Line.split("; ");
                if (firstLine) {
                    //skip
                    firstLine = false;
                }
                else{
                    //System.out.println(""+data[0] +" "+data[1]+" "+data[2]+" "+data[3]   );
                    Transaction t = new Transaction(data[2], data[3], Double.parseDouble(data[1]));
                    addTransaction(t);
                }
                
            }
            
        } catch (Exception e) {
            System.out.println("cant acess file");
            // TODO: handle exception
        }
    }

    public void writeFile(String file){
        //missing for now
        //File myFile = new File(file);
        
        Transaction t;
        try (FileWriter myWriter = new FileWriter("src\\" +file)){
            
            for (int keys : trasactionsLst.keySet()){
                t = trasactionsLst.get(keys);
                myWriter.write(t.getID() + "; " +t.getDescrição() + "; " + t.getDate() + "; " + t.getHoras() + "\n");
            }
        } catch (Exception e) {
            // TODO: handle exception
        }
    }
}
