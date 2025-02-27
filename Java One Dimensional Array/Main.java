class Main {
    public static void main(String[] args) {
        SingleDimensionArray sda = new SingleDimensionArray(10);
        sda.insert(0, 0);
        sda.insert(1, 10);
        sda.insert(3, 50);
        sda.insert(1, 70);
        sda.insert(9, 30);

    //     var firstElement = sda.arr[0];
    //     System.out.println(firstElement);
    //     System.out.println("Array traversal");
    //     sda.traverseArray();
        // sda.searchInArray(20);
        // sda.searchInArray(50);

    sda.deleteValue(30);
    System.out.println(sda.arr[9]);
    }
}