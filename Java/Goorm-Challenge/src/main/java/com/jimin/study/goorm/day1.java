package com.jimin.study.goorm;

import java.util.Scanner;

public class day1 {
    public static void main() {
        Scanner sc = new Scanner(System.in);
        int W = sc.nextInt();
        int R = sc.nextInt();
        System.out.println((int)(W * (1 + (double)R / 30)));
    }
}
