public class Primeornot{
    public static void main(String[] args) {
        int number=28;
        int flag=0;
        for(int i=2;i<number;i++)
        {
        if (number%i==0){
        flag=0;
        break;
        }
        else{
        flag=1;
        }}
        if(flag==1)
            System.out.println(number+" is a prime number ");
            else
            System.out.println(number+" is not a prime number");
        
    

    }
}