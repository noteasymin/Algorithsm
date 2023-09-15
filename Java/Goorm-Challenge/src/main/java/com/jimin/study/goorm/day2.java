package com.jimin.study.goorm;
import java.util.Scanner;
public class day2 {
    public static void main() {
        Scanner sc = new Scanner(System.in);
        int N;
        N = Integer.parseInt(sc.nextLine());

        String[] time = sc.nextLine().split(" ");
        int currentHour = Integer.parseInt(time[0]);
        int currentMinute = Integer.parseInt(time[1]);
        for (int i = 0; i < N; i++)
        {
            int costMinute = Integer.parseInt(sc.nextLine());
            int tempMinute = currentMinute + costMinute;
            int resultMinute = tempMinute % 60;
            int resultHour = (currentHour + tempMinute / 60) % 24;
            currentHour = resultHour;
            currentMinute = resultMinute;
        }
        System.out.println(currentHour + " " + currentMinute);
    }
}
