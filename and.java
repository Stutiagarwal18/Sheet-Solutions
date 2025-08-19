
// check if a no. is divisible by 3 and last digit is 4 

import java.util.Scanner;

public class and {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter a number");
        int n = sc.nextInt();
        if (n % 3 == 0 && n % 10 == 4) {
            System.out.println("divisible by 3 and last digit is 4");
        } else {
            System.out.println("not ");
        }

    }
}
