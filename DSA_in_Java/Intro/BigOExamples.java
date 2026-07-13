package DSA_in_Java.Intro;

public class BigOExamples {
    // Time complexity: 
    // Time complexity: O(1)
    public static int getFirstElement(int[] arr){
        return arr[0]; 
    }

    // Time complexity: O(log n)
    public static int binarySerach(int[] arr, int target){
        int left = 0; 
        int right = arr.length - 1; 
        
        while (left <= right){
            int mid = (left + right) / 2; 
            if (arr[mid] == target){
                return mid; 
            } else if (arr[mid] > target){
                right = mid - 1; 
            } else {
                left = mid + 1; 
            }
        }
        return -1; 
    }

    // Time complexity: O(n)
    public static int linearSearch(int[] arr, int target){
        for (int i = 0; i < arr.length; i++){
            if (arr[i] == target){
                return i; 
            } 
        }
        return -1;
    }

    // Do the merge sort
    // Time complexity: O(nlogn)

    // Time complexity: O(n^2):
    public static void printPairs(int arr[]){
        for (int i = 0; i < arr.length; i++){
            for (int j = 0; j < arr.length ; j++){
                System.out.println(arr[i] + ", " + arr[j]); 
            }
        }
    }

    // Time complexity: O(n^3):
    public static void printTriplets(int arr[]){
        for (int i = 0; i < arr.length; i++){
            for (int j = 0; j < arr.length ; j++){
                for (int k = 0; k < arr.length; k++){
                    System.out.println(arr[i] + ", " + arr[j] + ", " + arr[k]); 
                }
            }
        }
    }

    // Time complexity: O(2^n):
    public static int fib(int n){
        if (n <= 1){
            return n; 
        }
        return fib(n-1) + fib(n-2); 
    }

    // --------------------------------------------
    // Space complexity: 

}