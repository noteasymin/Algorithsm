package org.backjoon;
import java.io.*;


public class AplusB3 {

	public static void main(String[] args) {
		
		
	    try {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    BufferedWriter bw = new BufferedWriter(new FileWriter("bufferedWriter.txt"));
		int T =Integer.parseInt(br.readLine());
		
		
		for(int i = 0; i < T ; i++)
		{
			int A =Integer.parseInt(br.readLine());
			int B =Integer.parseInt(br.readLine());
			bw.write(A);
			bw.flush();
			bw.close();
		}
		
		
	    }
	    catch(IOException e) {
	    	e.printStackTrace();
	    	System.out.println(e.getMessage());
	    }
	}

}
