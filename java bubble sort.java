public static void bubbleSort(int[] arr, int beginI, int endI){
        int maxIndex = endI+1;
        int temp;
        while(maxIndex > beginI){
            maxIndex--;
            for(int i = beginI;i < maxIndex; i++){
                if(arr[i]>arr[i+1]){
                    temp = arr[i];
                    arr[i]=arr[i+1];
                    arr[i+1]=temp;
                }
            }
        }
    }
