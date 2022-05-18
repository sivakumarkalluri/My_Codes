public class cts1{
    public static void main(String[] args) {
        int arr[]=new int[]{3,2,5,4,9,1,0};;
       // arr[]=
        sortArray(7,arr);
        

    }
   public void sortArray(int len, int[] arr)
{
    for(int i=0;i<len;i++){
        System.out.println(arr[i]);
    }
    // int i, max, location, temp, j,k;
    // if(len/2 == 0)//error in this line
    // {
    // for(i=0;i<len;i++)
    // {
    //     max=arr[i];
    //     location = i;
    //     for(j=i;j<len;j++)
    //     if(max<arr[j])//error in this line
    //     {
    //         max=arr[j];
    //         location = j;
            
    //     }
    //     temp=arr[i];
    //     arr[i]=arr[location];
    //     arr[location]=temp;
    // }
    // }
    // else
    // {
    //     for(i=0;i<len;i++)
    // {
    //     max=arr[i];
    //     location = i;
    //     for(j=i;j<len;j++) if(max>arr[j])//error in this line
    //     {
    //         max=arr[j];
    //         location = j;
            
    //     }
    //     temp=arr[i];
    //     arr[i]=arr[location];
    //     arr[location]=temp;
    // }
    // }
}
}