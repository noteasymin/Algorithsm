package org.backjoon;

import java.util.Scanner;

public class year {

	public static void main(String[] args) {
		int H,M;
        Scanner sc = new Scanner(System.in);
        H = sc.nextInt();
        M = sc.nextInt();
        
        if(H == 0) {
        	H = 24;
        }
        
        if(M >= 45) {
        	M = M - 45;
        }
        
        else {
        	
        	H = H - 1;
        	M = M + 15;
        }
        
        if(H == 24) {
        H = 0;
        System.out.printf("%d %d",H,M);
        }
            }
	}

