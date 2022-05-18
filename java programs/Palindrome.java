import java.util.*;
public class Palindrome{
    public static void main(String[] args) {
        String word ="mom";
        int word_length=word.length();
        int flag=0;
        for (int i=0;i<word_length;i++)
        {
            if(word.charAt(i)==word.charAt(word_length-1-i))
            flag=1;
            else
            flag=0;
            break;

        }
        if (flag==1){
            System.out.println("word is palindrome");
        }
        else
        System.out.println("not a palindrome");
        // System.out.println(word_length);
    }
}
// this is another method for finding palindrome or not
// import java.util.*;
// public class Palindrome{
//     public static void main(String[] args) {
//         String word ="moma";
//         String reverse="";
//         int word_length=word.length();
//         for (int i=word_length-1;i>=0;i--){
//             reverse+=word.charAt(i);
//         }
//         if (reverse.equals(word))
//         System.out.println(word+" is palindrome");
//         else
//         System.out.println(word+" is not a palindrome");
        

//         }
//         }
