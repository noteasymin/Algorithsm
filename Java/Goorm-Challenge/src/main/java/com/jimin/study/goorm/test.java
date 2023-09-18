package com.jimin.study.goorm;

public class test {
    public static int[][] solution(int n, int m, int[] fold, int[][] cut) {
        int[][] paper = new int[n][m];

        // 색종이를 가로 방향으로 fold[0]번, 세로 방향으로 fold[1]번 접기
        for (int i = 0; i < Math.abs(fold[0]); i++) {
            paper = foldHorizontal(paper);
        }
        for (int i = 0; i < Math.abs(fold[1]); i++) {
            paper = foldVertical(paper);
        }

        // cut 배열에 따라 색종이를 잘라냄
        for (int[] c : cut) {
            int row = c[0] - 1;
            int col = c[1] - 1;
            if (row >= 0 && row < n && col >= 0 && col < m) {
                paper[row][col] = 0;
            }
        }
        System.out.println(paper);
        return paper;
    }

    // 가로로 색종이 접는 함수
    private static int[][] foldHorizontal(int[][] paper) {
        int n = paper.length;
        int m = paper[0].length;
        int[][] folded = new int[n][m / 2];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m / 2; j++) {
                folded[i][j] = paper[i][j] + paper[i][m - j - 1];
            }
        }

        return folded;
    }

    // 세로로 색종이 접는 함수
    private static int[][] foldVertical(int[][] paper) {
        int n = paper.length;
        int m = paper[0].length;
        int[][] folded = new int[n / 2][m];

        for (int i = 0; i < n / 2; i++) {
            for (int j = 0; j < m; j++) {
                folded[i][j] = paper[i][j] + paper[n - i - 1][j];
            }
        }

        return folded;
    }
}