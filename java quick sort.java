public static void quickSort(int[] arr, int beginI, int endI){
        if(beginI>=endI){
            return;
        }
        int pivot = beginI;
        int temp;
        for(int i = beginI+1; i<endI+1; i++){
            if(arr[i] <= arr[pivot] && pivot < i){
                temp = arr[pivot+1];
                arr[pivot+1] = arr[i];
                arr[i] = temp;

                temp = arr[pivot];
                arr[pivot]=arr[pivot+1];
                arr[pivot+1] = temp;

                pivot++;
            }
        }
        quickSort(arr,beginI,pivot-1);
        quickSort(arr,pivot+1,endI);

    }
