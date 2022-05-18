public class Arrays{
    public static void main(String[] args) {
      int array[]=new int[]{9,2,0,1,7,6,9,3,2,1,2,6,0};
      int output[]=new int[10];
      int count=0;
      for(int p=0;p<array.length-1;p++){
          for(int k=p+1;k<array.length;k++){
              if (array[p]>array[k]){
                  int temp=array[p];
                  array[p]=array[k];
                  array[k]=temp;
              }
          }

      }
      for(int item:array){
          System.out.println(item);
      }
      for(int i=0;i<a.length;)
    //   System.out.println(output.length);
      
    //   for(int i=0;i<array.length;i++)
    //      {
    //          int result=0;
    //           for(int j=0;j<output.length;j++){
    //               if(array[i]!=output[j]){
                  
    //               result=1;}
    //               else{
    //               result=0;
    //               break;}
    //           }
    //           if(result==1){
                 
    //               output[count]=array[i];
    //               count++;
    //           }}
    //           for(int item:output){
    //               if(item==0){
    //               System.out.println(item);}
    //           }



    }
}