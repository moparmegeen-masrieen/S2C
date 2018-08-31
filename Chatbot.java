import java.awt.*;
 import javax.swing.JOptionPane;
public class main {
 	public static void main(String[] args) {
		//THE AI FUNCTION PROCESSING UNIT
		ai("COMMAND","NAME");
	}
	public static String ai (String txt,String u) {
		//THE AI FUNCTION
		JOptionPane.showMessageDialog(null,"[INFO]:HELLO "+u+", WELCOME TO MORAD ALI AI PROGRAM !");
		if (txt == null) {
			JOptionPane.showMessageDialog(null,"[ERROR]:THE INPUT HAS NO STRING");
		}else if (txt == "hello" || txt == "hi" || txt == "greetings") {
			JOptionPane.showMessageDialog(null,"[REPLY]:HELLO "+u);
		}else if (txt == "how r u" || txt == "how are u" || txt == "how are you") {
			JOptionPane.showMessageDialog(null,"[REPLY]:GREAT THX :)");
		}else {
			JOptionPane.showMessageDialog(null,"[ERROR]:THE TEXT CANNOT BE UNDERSTANDED,PLEASE TRY AGAIN ! \n The text was :"+txt+"\n The name of user was:"+u);
		}
		return null;
	}
 }
