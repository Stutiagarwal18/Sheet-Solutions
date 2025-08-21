
// check if last digit of no. is 4 or not

import java.util.Scanner;

public class lastDigit {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter a number");
        int n = sc.nextInt();
        int lastDigit = n % 10;
        if (lastDigit == 4) {
            System.out.println("last digit is 4");
        } else {
            System.out.println("not 4");
        }

    }
}
