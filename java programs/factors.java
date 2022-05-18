public class factors{
    public static void main(String[] args) {
        int number=54;
        int factors[]=new int[100];
        
        int factor_count=0;
        for(int i=1;i<number;i++)
        {
            if (number%i==0){
            factors[factor_count]=i;
            factor_count+=1;
            
            }

        }
        for(int k:factors)
        {
            if (k==0){
                break;}
                else{
                    
        System.out.print(k);
        
        
        
        System.out.print(",");}
        }
        System.out.println("Number of factors for "+number+" is " +factor_count);
    

    }
}