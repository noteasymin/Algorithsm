package com.jimin.study.goorm;

import java.util.*;

class Pair implements Comparable<Pair> {
    int bits;
    int num;

    public Pair(int bits, int num) {
        this.bits = bits;
        this.num = num;
    }

    public int compareTo(Pair o) {
        if (this.bits == o.bits) {
            return o.num - this.num;
        } else {
            return o.bits - this.bits;
        }
    }
}

public class day5 {
    public static void main() {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = sc.nextInt();

        ArrayList<Pair> pairs = new ArrayList<>();

        for (int i = 0; i < N; ++i) {
            int num = sc.nextInt();
            int bits = Integer.bitCount(num);
            pairs.add(new Pair(bits, num));
        }
        Collections.sort(pairs);

        System.out.println(pairs.get(K - 1).num);
    }
}
