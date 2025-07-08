package parte2;

public class TCP extends Pacote {
    private String endreço;
    private String destino;
    private String menssagem; 
    public TCP(String endreço,String destino,String menssagem){
        this.endreço = endreço;
        this.destino = destino;
        this.menssagem = menssagem;
    }
    @Override
    public String toString() {
        return "TCP source:" + endreço + ", destination:" + destino + ", menssagem-> " + menssagem + "]\n";
    }
    
    
    public void removePacoteLines() {
        endreço = null;
        destino = null;
        menssagem = null;
        
    }
    
}
