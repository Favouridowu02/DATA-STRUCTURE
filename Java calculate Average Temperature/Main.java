import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        System.out.print("How many Days' temperature? ");
        int numDays = console.nextInt();
        int[] temps = new int[numDays];
        // record temperature and find average
        int sum = 0;
        for (int i = 1; i <= numDays; i++) {
            System.out.print("Day " + i + "'s high temp: ");
            temps[i - 1] = console.nextInt();
            sum += temps[i - 1];
        }
        double average = sum / numDays;
        // counts days above average
        int above = 0;
        for (int i = 0; i < temps.length; i++) {
            if (temps[i] > average) {
                above++;
            }
        }
        System.out.println();
        System.out.println("Average Temp = " + average);
        System.out.println(above + " Days Above Average");
    }
}