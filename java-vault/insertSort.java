import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    static void printArray(int [] arr){
        for(int i=0;i<arr.length;i++)
            System.out.print(arr[i]+" ");
        System.out.print("\n");
    }

    static void insertionSort2(int n, int[] arr) {
        for(int i=1;i<arr.length;i++){
            int num = arr[i];
            for(int j=i-1;j>=0;j--){
                //System.out.println("i: " + i +"j:" + j + "arr[j]:"+arr[j]+"arr[j-1]:"+arr[j-1]);
                if (num < arr[j]){
                    arr[j+1] = arr[j];
                    arr[j] = num;
                }
            }
            printArray(arr);
        }        
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] arr = new int[n];
        for(int arr_i = 0; arr_i < n; arr_i++){
            arr[arr_i] = in.nextInt();
        }
        insertionSort2(n, arr);
        in.close();
    }
}
