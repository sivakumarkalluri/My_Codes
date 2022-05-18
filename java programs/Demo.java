// import java.util.*;
interface Rectangle{
	void area();
	void perimeter();
}
class Child implements Rectangle{
	
		
		int side=4;
		
		public void area() {
			System.out.println("area of square is : "+(side*side));
			
		}
		public void perimeter() {
			System.out.println("perimeter of square is "+(4*side));

			
		}

	}

class Demo{
	public static void main(String[] args) {
		Child obj1=new Child();
		obj1.area();
		obj1.perimeter();
	}
}