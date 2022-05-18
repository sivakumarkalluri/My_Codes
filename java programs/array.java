class demo
{
int grades[]=new int[5];

void reading()
{
int i;
for(i=0;i<=4;i++)
grades[i]=i+1;
}
void display()
{
for(int i=0;i<=4;i++)
System.out.println("grades["+i+"] ="+grades[i]);
}
void sum()
{
int sum=0;
for(int i=0;i<=4;i++)
//{
sum=sum+grades[i]; 
//}
System.out.println("sum is "+sum);
}
void max()
{
int max=grades[0];
for(int i=1;i<=4;i++)
if(max<grades[i])
max=grades[i];
System.out.println("maximum is "+max);
}
}
class array
{
public static void main(String args[])
{
demo a=new demo();
a.reading();
a.display();
a.sum();
a.max();
}}
