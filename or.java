
// read a number check if a no. is divisible by 7 or last digit is 5
import java.util.Scanner;

public class or {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter a number");
        int n = sc.nextInt();

        if (n % 7 == 0 || n % 10 == 5) {
            System.out.println("divisible by 7 or last digit is 5");
        } else {
            System.out.println("not ");
        }

    }
}
