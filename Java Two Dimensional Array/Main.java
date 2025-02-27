import java.util.Arrays;
class Main {
    public static void main(String [] args) {
        TwoDimensionalArray tda = new TwoDimensionalArray(3, 3);
        tda.insertValueInTheArray(0, 0, 10);
        tda.insertValueInTheArray(0, 1, 10);
        tda.insertValueInTheArray(1, 2, 20);
        tda.insertValueInTheArray(2, 2, 20);
        tda.insertValueInTheArray(2, 0, 20);
        System.out.println(Arrays.deepToString(tda.arr));
        tda.deleteValueFromArray(1, 2);
        System.out.println(Arrays.deepToString(tda.arr));
        // tda.accessCell(0, 0);
        // tda.traverse2DArray();
        tda.searchingValue(20);
    }
}