package com.jimin.study.goorm;

import java.util.Scanner;

public class day3 {
    public static void main() {
        Scanner sc = new Scanner(System.in);
        int T = Integer.parseInt(sc.nextLine());
        int answer = 0;

        for (int i = 0; i < T; i++) {
            String[] calc = sc.nextLine().split(" ");
            int left = Integer.parseInt(calc[0]);
            int right = Integer.parseInt(calc[2]);
            String op = calc[1];

            if (op.equals("+")) {
                answer += left + right;
            } else if (op.equals("-")) {
                answer += left - right;
            } else if (op.equals("/")) {
                answer += left / right;
            } else if (op.equals("%")) {
                answer += left % right;
            }


        }
        System.out.println(answer);
    }
}