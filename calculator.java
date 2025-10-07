import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        while (true) {
            System.out.println("----------CALCULATOR----------");

            System.out.print("Write first number: ");
            int a = input.nextInt(); // Kullanıcının girdiği ilk sayı

            System.out.print("Write second number: ");
            int b = input.nextInt(); // Kullanıcının girdiği ikinci sayı

            System.out.print("Select the action you want to perform (+,-,*,/): ");
            String islem = input.next(); // Yapılacak işlem

            if (islem.equals("+")) {
                System.out.println("result: " + (a + b));
            } else if (islem.equals("-")) {
                System.out.println("result: " + (a - b));
            } else if (islem.equals("*")) {
                System.out.println("result: " + (a * b));
            } else if (islem.equals("/")) {
                System.out.println("result: " + ((float)a / b));
            } else {
                System.out.println("invalid transaction");
            }

            System.out.println("action completed.\n");
        }
    }
}
