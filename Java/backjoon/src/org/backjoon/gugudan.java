import java.util.Scanner;
package org.backjoon;

public class gugudan {

	public static void main(String[] args) {
		int N;
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        
        for(int i; i<10; i++)
        {
            System.out.println(N +" * " + i " = " + N*i);
        }

	}

}
