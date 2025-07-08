import java.time.LocalDateTime;

public class Concert implements Comparable<Concert>{
    private double Duracao;
    private String Local;
    private LocalDateTime data;
    private int id;
    private static int idInc = 0;
    public Concert(String Local,String data,double Duracao){
        String[] Data = data.split(" ");
        String[] date =Data[0].split("-"); 
        String hora[] =Data[1].split(":");
        //LocalDateTime Date = new (Duracao, Local, data)
        LocalDateTime Date = LocalDateTime.of(Integer.parseInt(date[0]), Integer.parseInt(date[1]), Integer.parseInt(date[2]),Integer.parseInt(hora[0]),Integer.parseInt(hora[1]));
        this.data = Date;
        this.Duracao= Duracao;
        this.Local= Local;
        this.id =idInc++;
    }
    public double getDuracao() {
        return Duracao;
    }
    public String getLocal() {
        return Local;
    }
    public LocalDateTime getData() {
        return data;
    }
    public int getId() {
        return id;
    }

//----------------------
    public void setDuracao(double duracao) {
        Duracao = duracao;
    }
    public void setLocal(String local) {
        Local = local;
    }
    public void setData(LocalDateTime data) {
        this.data = data;
    }
    public static void setIdInc(int idInc) {
        Concert.idInc = idInc;
    }
    @Override
    public String toString() {
        return "Concert [getDuracao()=" + getDuracao() + ", getLocal()=" + getLocal() + ", getData()=" + getData()
                + "getIdInc()=" + getId() + "]";
    }
    @Override
    public int compareTo(Concert c){
       int dateComp =this.data.compareTo(c.getData());
       if (dateComp != 0) {
        return dateComp;
       }
        return Integer.compare(this.id, c.getId());
    }    
}
