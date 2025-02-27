public class TwoDimensionalArray {
    int arr[][] = null;

    // Constructor
    public TwoDimensionalArray(int numberOfRows, int numberOfColumns) {
        this.arr = new int[numberOfRows][numberOfColumns];
        for (int row = 0; row < numberOfRows; row++) {
            for (int col = 0; col < numberOfColumns; col++) {
                arr[row][col] = Integer.MIN_VALUE;
            }
        }
    }

    // Inserting into the Array
    public void insertValueInTheArray(int row, int col, int value) {
        try {
            if (arr[row][col] == Integer.MIN_VALUE) {
                arr[row][col] = value;
                System.out.println("The value is successfully inserted");
            } else {
                System.out.println("The cell is already occupied");
            }

        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("invalid Index for 2D Array");
        }
    }

    public void accessCell(int row, int col) {
        System.out.println("\nAccessing Row#" + row +", Col#" + col);
        try {
            System.out.println("Cell Value is: " + arr[row][col]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Index does not exist");
        }
    }

    public void traverse2DArray() {
        for (int row = 0; row < arr.length; row++) {
            for (int col = 0; col < arr[0].length; col++) {
                System.out.print(arr[row][col] + "  ");
            }
            System.out.println();
        }
    }

    public void searchingValue(int value) {
        for (int row = 0; row < arr.length; row++) {
            for (int col = 0; col < arr[0].length; col++) {
                if (arr[row][col] == value) {
                    System.out.println("Value is found at row: " + row + " Col: " + col);
                    return;
                }
            }
        }
        System.out.println("The Value is not found");
    }

    public void deleteValueFromArray(int row, int col) {
        try {
            arr[row][col] = Integer.MIN_VALUE;
            System.out.println("Successfully deleted");
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Index does not exist");
        }
    }
}