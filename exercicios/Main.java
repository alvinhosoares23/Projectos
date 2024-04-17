import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);
        int C = leitor.nextInt(); // número de casos de teste

        // Limpeza do buffer para garantir que não haja problemas de leitura
        leitor.nextLine();

        for (int i = 0; i < C; i++) {
            String[] input = leitor.nextLine().split(" ");
            String nome = input[0]; // primeiro nome da pessoa
            int N = Integer.parseInt(input[1]); // força aplicada em Newtons

            // Verifica se o nome é "Thor" e se a força aplicada é maior ou igual a 20
            if (nome.equals("Thor") && N >= 20) {
                System.out.println("Thor conseguiu levantar o Mjölnir"); // Thor conseguiu levantar o Mjölnir
            } else if (nome.equals("Hulk") && N >= 40) {
                System.out.println("Hulk também conseguiu levantar algo pesado"); // Hulk também conseguiu levantar algo pesado
            } else {
                System.out.println("Não conseguiu levantar"); // Não conseguiu levantar
            }
        }
    }
}