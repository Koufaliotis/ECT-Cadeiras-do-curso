//chass register code
    
    import java.util.ArrayList;
    public class CashRegisterDemo {

        public static void main(String[] args) {
            // Create a CashRegister instance
            CashRegister cr = new CashRegister();
    
            // Add 5 products
            cr.addProduct(new Product("Book", 9.99, 3));
            cr.addProduct(new Product("Pen", 1.99, 10));
            cr.addProduct(new Product("Headphones", 29.99, 2));
            cr.addProduct(new Product("Notebook", 19.99, 5));
            cr.addProduct(new Product("Phone case", 5.99, 1));
    
            // List the content and total value
            cr.listProducts();
        }
    }
    //////////////////////////////////////////////////////////////////////
    class CashRegister {
        private ArrayList<Product> myProductLst = new ArrayList<>();
    
        // Method to add a Product to the list
        public void addProduct(Product product) {
            myProductLst.add(product);
    
            System.out.println("Added product: " + product.getName());
            System.out.println("Price: " + product.getPrice());
            System.out.println("Quantity: " + product.getQuantity());
            System.out.println("Total Value: " + product.getTotalValue());
        }
    
        // Method to list all products and their total value
        public void listProducts() {
            double grandTotal = 0.0;
    
            System.out.println("Products in the Cash Register:");
            for (Product product : myProductLst) {
                System.out.println("- " + product.getName() + " | Price: " + product.getPrice() + 
                                   " | Quantity: " + product.getQuantity() +
                                   " | Total Value: " + product.getTotalValue());
                grandTotal += product.getTotalValue();
            }
    
            System.out.println("Grand Total Value: " + grandTotal);
        }
    }
     
/////////////////////////////////////////////////////
