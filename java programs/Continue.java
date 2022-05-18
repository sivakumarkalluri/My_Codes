public class Continue{
    public static void main(String[] args) {
        for(int i=0;i<10;i++){
            for(int j=0;j<10;j++){
                if (j==3){
                    System.out.println("this is break at i= "+i+" j = "+j);
                    break;}
                else{
                System.out.println("i -----> "+i);
                System.out.println("j -----> "+j);
                
                }
            }
        }
    }
}