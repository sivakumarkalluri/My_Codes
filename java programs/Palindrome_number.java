public class Palindrome_number{
    public static void main(String[] args) {
        int number=132232;
        int remainder,sum=0;
        int temp=number;
        while(temp!=0){
            remainder=temp%10;
            sum=sum*10+remainder;
            temp=temp/10;
        }
        if(sum==number)
        System.out.println(number+" is a plaindrome number");
        else
        System.out.println(number+" is not a palindrome number");
    }
}