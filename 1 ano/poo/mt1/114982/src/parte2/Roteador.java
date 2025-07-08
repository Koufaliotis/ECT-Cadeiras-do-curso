package parte2;
import java.util.ArrayList;
import java.util.Iterator;

public  class Roteador {
    private String nome;
    private ArrayList<Object> pacotesLST = new ArrayList<>(); 
    
    
    public Roteador(String nome){
      this.nome = nome;  
    }

    public void addPacote(Object pacote){
        //add to lst
        this.pacotesLST.add(pacote);
    }

    public boolean hasPacotes(){
        if (pacotesLST.isEmpty()==true){
            return false;
        }
        return true;
    }

    public void enviaPacote(){
        for(Object pacote : pacotesLST){
            
            System.out.println(pacote.toString());
            removePacote(pacote);
            //pacote.remove(pacote);
            //pacotesLST.remove(pacote);
        }
    }

    public void removePacote(Object pacot){
        Iterator<Object> iterator = pacotesLST.iterator();
        while (iterator.hasNext()) {
            if (iterator.next() == pacot) {
                iterator.remove(); // Safe removal
                break; // Remove only the first match
            }
        }
       
        // ArrayList<Object> pacotesLSTholder = pacotesLST;
        //int a = 0;
        //for (Object pacote : pacotesLSTholder){
            
          //  if (pacote == pacot) {
                
                //remove
            //    pacotesLST.remove(a);
           // }
           // a++;
    //    }
    }

    @Override
    public String toString() {
        return "Roteador " + nome + ", pacotesLST=" + pacotesLST + "]";
    }

    
}
