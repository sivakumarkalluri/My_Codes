import java.util.*;
class Main1{
    public static void main(String []args){
        Scanner sc=new Scanner(System.in);
        System.out.println("eneter a");
        int a=sc.nextInt();
        if(a==1)
        {
            String name=sc.next();
            int year=sc.nextInt();
            String depa=sc.next();
            int per=sc.nextInt();
            System.out.println("Name : "+name);
            System.out.println("BirthYear : "+year);
            System.out.println("Department : "+depa);
            //int per=sc.nextInt();
            if(per<75)
            {
               System.out.println("Elligible : No");  
            }
            else{
                 System.out.println("Elligible : Yes");
            }
            
        }
        if(a==2)
        {
            String name=sc.next();
            int year=sc.nextInt();
            String sub=sc.next();
            float pere=sc.nextInt();
            int salary=sc.nextInt();
          System.out.println("Name : "+name);
          System.out.println("BirthYear : "+year);
          System.out.println("Salary : "+salary);
          System.out.println("Subject : "+sub);
         // System.out.println(pere/1000);
         
          double newsalary=((pere/1000)*salary)+salary;
          //newsalary=salary+newsalary;
          System.out.println("NewSalary : "+newsalary);  
        }
        if(a==3)
        {
            System.out.println("eneter name : ");

         String name=sc.next();
         System.out.println("eneter year");

         int year=sc.nextInt();
         System.out.println("eneter lab ");
         Scanner sb=new Scanner(System.in);

         String lab=sb.nextLine();
         System.out.println("eneter pe : ");

         float pe=sc.nextInt();
         System.out.println("eneter salary : ");

         int salary=sc.nextInt();
          System.out.println("Name : "+name);
          System.out.println("BirthYear : "+year);
           System.out.println("Old Salary : "+salary);
          System.out.println("Lab : "+lab);
          double newsalary=((pe/100)*salary) + salary;
          System.out.println("New salary : "+newsalary);
        }
        
    }
}