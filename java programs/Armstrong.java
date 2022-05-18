public class Armstrong{
    public static void main(String[] args) {
        int number=154;
        int temp=number;
        int remainder,sum=0;
        while(temp!=0){

            remainder=temp%10;
            sum+=remainder*remainder*remainder;
            temp=temp/10;
            
        }
        if (sum==number)
        System.out.println(number+" is armstrong number");
        else
        System.out.println(number+" is not a armstrong number");
        
    }
}