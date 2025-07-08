import java.util.ArrayList;
class Product {
    private String name;
    private double price;
    private int quantity;

    public Product(String name, double price, int quantity) {
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }

    public double getTotalValue() {
        return price * quantity;
    }

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }

    public int  getQuantity() {
        return quantity;
    }
}


class CashRegister {
    String productName;
    Double productPrice;
    int quantity ;
    Object insertedProduct;
    ArrayList <String[]> myProductLst = new ArrayList<String[]>();
    String[] mixedArray = new String[4];
    
    

    public void addProduct(Product product){
       this.productName = product.getName();
       this.productPrice = product.getPrice();
       this.quantity = product.getQuantity();
       
       mixedArray[0] ="" + productName;
       mixedArray[1] = "" + productPrice;
       mixedArray[2] = "" +quantity;
       mixedArray[3]="" + quantity * productPrice;

       myProductLst.add(mixedArray);

        //System.out.println(productName);
        //System.out.println(productPrice);
        //System.out.println(quantity);
        //System.out.println(myProductLst);
        
        //resulucao no testFile2
    } 


     public String Bascet(){

        for(String[] Data : myProductLst){
            
                System.out.println("" + Data[0] + "   " + Data[1] + "   " + Data[2] + "   " + Data[3]);
                
            
        }
        return "";
    }

    // TODO: completar implementação da classe
    
}

public class CashRegisterDemo {

    public static void main(String[] args) {

        // Cria e adiciona 5 produtos
        CashRegister cr = new CashRegister();
        cr.addProduct(new Product("Book", 9.99, 3));
        cr.addProduct(new Product("Pen", 1.99, 10));
        cr.addProduct(new Product("Headphones", 29.99, 2));
        cr.addProduct(new Product("Notebook", 19.99, 5));
        cr.addProduct(new Product("Phone case", 5.99, 1));
        
        // TODO: Listar o conteúdo e valor total
        System.out.println(cr.Bascet());

    }
}