class Student {
	static int StudentCount=2;
	int id=2;
	String name="Vinay";
	int age;
	char gender;
	static int[] Exam_Marks=new int[]{87,86,85,84,83};
	
	boolean InternationalStudent;
	double TutionFee=2000;
	double InternationalFee=3000;
	void compute(){
		int nextId=id+1;
		int value=2;
		StudentCount+=1;
		System.out.println("\nid --->"+id);
		System.out.println("nextId--->"+nextId);
		System.out.println("name---->"+name);
		System.out.println("age----->"+age);
		System.out.println("gender---->"+gender);
		if(InternationalStudent){
			TutionFee+=InternationalFee;
		}
		System.out.println("TutionFee--->"+TutionFee);
		System.out.println("StudentCount---->"+StudentCount);
	}
	static void Display_Marks(){
		System.out.println("Mid 1: "+Exam_Marks[0]);
		System.out.println("Mid 2: "+Exam_Marks[1]);
		System.out.println("Mid 3: "+Exam_Marks[2]);
		System.out.println("Mid 4: "+Exam_Marks[3]);
		System.out.println("Mid 5: "+Exam_Marks[4]);
		
	}
	public static void main(String args[]){
		Student S1=new Student();
		S1.id=(int)1000.0;
		S1.name="Siva";
		S1.age=21;
		S1.gender='M';
		S1.InternationalStudent=false;
		S1.compute();
		Student S2=new Student();
		S2.id=1002;
		S2.name="Ganesh";
		S2.age=19;
		S2.gender='F';
		S2.InternationalStudent=true;
		S2.compute();
		S2.Exam_Marks[0]=91;
		S2.Exam_Marks[1]=92;
		S2.Exam_Marks[2]=93;
		S2.Exam_Marks[3]=94;
		S2.Exam_Marks[4]=95;
		
		S2.Display_Marks();
		S2.Display_Marks();
	}
}
		
		
		
	
