package com.company;
import java.util.*;
import java.io.*;


public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the length of your array:");
        int arrLength = scanner.nextInt();
        int[] arr = new int[arrLength];

        System.out.println("Enter the element in your array respectively:");
        for (int i = 0; i < arrLength; i++) {
            arr[i] = scanner.nextInt();
        }

        mergeSort(arr,0,arrLength-1);
        for (int i = 0; i < arrLength; i++) {
            System.out.print(arr[i]+" ");
        }

    }


    public static void mergeSort(int[] arr, int beginI, int endI){
        if(beginI == endI){
            return;
        }
        System.out.printf("left array:%d to %d / right array:%d to %d\n", beginI, (endI+beginI)/2,((endI+beginI)/2)+1, endI);
        System.out.printf("dealing with (%d , %d)\n",beginI, endI);


        System.out.println("Sorting left side of the array...");
        mergeSort(arr, beginI, (endI+beginI)/2); // sorts left side of the array
        System.out.printf("%d to %d array completed\n",beginI, (endI+beginI)/2);

        System.out.printf("dealing with (%d , %d)\n",((endI+beginI)/2)+1, endI);
        System.out.println("Sorting right side of the array...");
        mergeSort(arr, ((endI+beginI)/2)+1, endI); // sorts right side of the array
        System.out.printf("%d to %d array completed\n",((endI+beginI)/2)+1, endI);

        int[] tempArr = new int[endI-beginI+1]; // stores the sorted array temporarily
        int leftIndex = beginI; // the left array's index
        int rightIndex = ((endI+beginI)/2)+1; // the right array's index
        int i = 0; // the tempArr's index
        while(i <= endI-beginI){
            if(leftIndex == ((endI+beginI)/2)+1 || (rightIndex != endI+1 && arr[rightIndex] <= arr[leftIndex])){
                tempArr[i] = arr[rightIndex];
                rightIndex++;
            }
            else{
                tempArr[i] = arr[leftIndex];
                leftIndex++;
            }
            i++;

        }
        for(int j = beginI;j<=endI;j++){ // overwrite the original array
            arr[j] = tempArr[j-beginI];
            System.out.println("arr["+j+"]"+":"+arr[j]);
        }


    }
}
