package org.backjoon;

import java.util.Scanner;

public class chapter1Last {
	public static void main(String[] args) {
	int a,b;
	int ans;
    Scanner sc = new Scanner(System.in);
    a = sc.nextInt();
    b = sc.nextInt();
    
    String number = String.valueOf(b);
    
    char[] digits = number.toCharArray();
    
    for(int i = 2; i>=0; i--){
    	ans = a*(digits[i]-'0');
        System.out.println(ans);
    }
    System.out.println(a*b);
}
}