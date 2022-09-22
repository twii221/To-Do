// java program to reverse a word

import java.io.*;
import java.util.Scanner;

class REV {
	public static void main (String[] args) {
		
		String str= "REVERSE", nstr="";
		char ch;
		
	System.out.print("Original word: ");
	System.out.println("REVERSE"); 
		
	for (int i=0; i<str.length(); i++)
	{
		ch= str.charAt(i);
		nstr= ch+nstr; 
	}
	System.out.println("Reversed word: "+ nstr);
	}
}


