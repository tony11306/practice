public static void selectionSort(int[] arr, int beginI, int endI){
        int minValueIndex;
        int temp;
        if(endI-beginI+1 == 1){
            return;
        }
        for(int i = beginI ; i < endI+1 ; i++){
            minValueIndex = i;
            for(int j = i + 1 ; j < endI+1 ; j++){
                if(arr[j] < arr[minValueIndex]){
                    minValueIndex =j;
                }
            }
            temp = arr[i];
            arr[i]=arr[minValueIndex];
            arr[minValueIndex] = temp;
        }
    }
