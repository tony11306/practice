public static void insertionSort(int[] arr, int beginI, int endI){
        if(beginI == endI){
            return;
        }
        int temp;
        int j;
        for (int i = beginI+1; i < endI+1; i++) {
            temp = arr[i];
            j = i-1;
            while(j>=0 && temp < arr[j] ){
                arr[j+1] = arr[j];
                j--;
            }
            arr[j+1] = temp;
        }
    }
