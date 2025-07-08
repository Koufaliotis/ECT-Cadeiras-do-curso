package parte2;

public class Parte2 {
    public static Pacote[] geraPacotes() {
        Pacote[] out = new Pacote[5];
        out[0] = new TCP("1.1.1.1","2.2.2.2", "Olá! :)");
        out[1] = new TCP("2.2.2.2","1.1.1.1", "Olá! :)");
        out[2] = new UDP("2.2.2.2","1.1.1.1", "Olá! :)");
        out[3] = new UDP("2.2.2.2","1.1.1.1", "Olá! :)");
        out[4] = new UDP("2.2.2.2","1.1.1.1", "Tudo bem?");
        return out;
    }

    public static void main(String[] args) {
        // --------------------------------------------------------
        // Run #1
        // --------------------------------------------------------
        Pacote[] pacotes = geraPacotes(); //function up
        Pacote p1 = pacotes[0];
        Pacote p2 = pacotes[1];
        Pacote p3 = pacotes[2];
        Pacote p4 = pacotes[3];
        Pacote p5 = pacotes[4];

        Roteador router1 = new Roteador("Aveiro-UA");
        router1.addPacote(p1);
        router1.addPacote(p2);
        router1.addPacote(p3);
        router1.addPacote(p4);
        router1.addPacote(p5);

        System.out.println(router1);
        while(router1.hasPacotes()) {
            router1.enviaPacote();
           // break; //temp
        }
        System.out.println(router1);

        // --------------------------------------------------------
        // Run #2
        // --------------------------------------------------------
        pacotes = geraPacotes();
        p1 = pacotes[0];
        p2 = pacotes[1];
        p3 = pacotes[2];
        p4 = pacotes[3];
        p5 = pacotes[4];

        router1.addPacote(p1);
        router1.addPacote(p2);
        router1.addPacote(p3);
        router1.removePacote(p3);
        router1.addPacote(p4);
        router1.addPacote(p5);

        System.out.println(router1);
        while(router1.hasPacotes()) {
            router1.enviaPacote();
        }
        System.out.println(router1);
    }
}

