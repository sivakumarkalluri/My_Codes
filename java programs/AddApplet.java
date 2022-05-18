import java.awt.*;
import java.applet.*;
public class AddApplet extends Applet
{
	TextField t1,t2;	
	public void init()
	{
		t1=new TextField(10);
		add(t1);
		t1.setText("0");
		t2=new TextField(10);
		add(t2);
		t2.setText("0");
	}
	public void paint(Graphics g)
	{
		String str;
		int a,b,result;
		str=t1.getText();
		a=Integer.parseInt(str);
		str=t2.getText();
		b=Integer.parseInt(str);
		result=a+b;
		g.drawString("Value is:"+result,100,100);
	}
	public boolean action(Event e, Object o)
	{
		repaint();
		return true;
	}
}
