/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/

public class Sai
{
	public static void main(String[] args) {
	    int N=10;
	    int count=0;
	    int temp;
	    int digit;
	    for(int number=1; number<=N;number++){
	        int sum=0; 
	    temp=number;
		while(number>0) 
{  
digit = number % 10;  
sum = sum + digit;  
number = number / 10;  
}  
	        if (sum==temp){
	            count+=1;
	        }
	    }
	    System.out.println(count);
	}
}
