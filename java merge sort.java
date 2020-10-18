public static void mergeSort(int[] arr, int beginI, int endI){
        if(beginI >= endI){ // recursion stop condition
            return;
        }

        mergeSort(arr, beginI, (endI+beginI)/2); // sorts left side of the array
        mergeSort(arr, ((endI+beginI)/2)+1, endI); // sorts right side of the array

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
            //System.out.println("arr["+j+"]"+":"+arr[j]);
        }
        //System.out.println("---------------");


    }
