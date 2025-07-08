
    import java.util.ArrayList;
    import java.util.List;
    
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
    
        public int getQuantity() {
            return quantity;
        }
    
        @Override
        public String toString() {
            return name + " - Price: €" + price + ", Quantity: " + quantity + ", Total Value: €" + getTotalValue();
        }
    }
    
    class CashRegister {
        private List<Product> products;
    
        public CashRegister() {
            products = new ArrayList<>();
        }
    
        public void addProduct(Product product) {
            products.add(product);
        }
    
        public double getTotalValue() {
            return products.stream().mapToDouble(Product::getTotalValue).sum();
        }
    
        @Override
        public String toString() {
            StringBuilder sb = new StringBuilder();
            sb.append("Products in Cash Register:\n");
            for (Product product : products) {
                sb.append(product.toString()).append("\n");
            }
            sb.append("Total Value of All Products: €").append(getTotalValue());
            return sb.toString();
        }
    }
    
    public class testFile {
    
        public static void main(String[] args) {
    
            // Create and add 5 products
            CashRegister cr = new CashRegister();
            cr.addProduct(new Product("Book", 9.99, 3));
            cr.addProduct(new Product("Pen", 1.99, 10));
            cr.addProduct(new Product("Headphones", 29.99, 2));
            cr.addProduct(new Product("Notebook", 19.99, 5));
            cr.addProduct(new Product("Phone case", 5.99, 1));
    
            // Print the contents and total value
            System.out.println(cr);
          
}
}
