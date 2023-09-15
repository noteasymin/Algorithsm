package com.jimin.study.goorm;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class day4 {
    public static void main() {
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.nextLine());

        String[] arrStr = sc.nextLine().split(" ");
        ArrayList<Integer> arr = new ArrayList<>();
        for (String s : arrStr) {
            arr.add(Integer.parseInt(s));
        }

        int maxIndex = arr.indexOf(Collections.max(arr));

        ArrayList<Integer> left = new ArrayList<>(arr.subList(0, maxIndex));
        ArrayList<Integer> right = new ArrayList<>(arr.subList(maxIndex, n));

        Collections.sort(left);
        Collections.sort(right, Collections.reverseOrder());

        ArrayList<Integer> sortedArr = new ArrayList<>();
        sortedArr.addAll(left);
        sortedArr.addAll(right);

        if (sortedArr.equals(arr)) {
            int sum = sortedArr.stream().mapToInt(Integer::intValue).sum();
            System.out.println(sum);
        } else {
            System.out.println(0);
        }
    }
}
