public class Fibonacii{
    public static void main(String[] args) {
        int fib1=0,fib2=1,fib3;
        int n=5;
        for(int i=0;i<n;i++)
        {
            fib3=fib1;
            System.out.println(fib3+" ");
            fib3=fib1+fib2;
            fib1=fib2;
            fib2=fib3;
        }

    }
}