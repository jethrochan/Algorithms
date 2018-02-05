import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.lang.Math.*;

public class Rectangles {
    //NOTE: lb = lower bottom, rt = right top
    //rect 1//K: lb1.x L: lb1.y,      M: rt1.x N=rt1.y
    //rect 2//P: lb2.x Q: lb2.y       R: rt2.x S:rt2.y

    //find combined area.
    //add 2 original ones and subtract the findOverlapArea
  	public static boolean ifOverlap(double K, double L, double M, double N, double P, double Q, double R, double S)
    {
      //if left of
      if(R < K || M < P){ //ie lefts of both rect greater than the right of the other.
        return false;  }
      //if above
      if(S < L || N < Q){ //if someone's top most point less than your bottom most, they are lower than you.
        return false;
      }
      return true; //does overlap
    }//ifOverlap

    public static double  findOverlapArea(double K, double L, double M, double N, double P, double Q, double R, double S){

      //Rect 1
      double  rect1_xmax = M;
      double  rect1_ymax = N;

      double  rect1_xmin = K;
      double  rect1_ymin = L;
      //Rect 2
      double  rect2_xmax = R;
      double  rect2_ymax = S;

      double  rect2_xmin = P;
      double  rect2_ymin = Q;

      //min of the max extremities of that axis.
      double  base = Math.min(rect1_xmax, rect2_xmax) - Math.max(rect1_xmin, rect2_xmin);
      double  height = Math.min(rect1_ymax, rect2_ymax) - Math.max(rect1_ymin, rect2_ymin);

      if ((base >= 0) && (height >= 0)){
        return (base*height);
      }
      else{
        return 0;
      }

    }//findOverlapArea

    public static void main(String[] args) {

      double K = -4;
      double L = 1;
      double M = 2;
      double N = 6;
      double P = 0;
      double Q = -1;
      double R = 4;
      double S = 3;

      if (ifOverlap(K, L, M, N, P, Q, R, S)){
          System.out.println("Rectangles Overlap");
      }
      else{
          System.out.println("Rectangles Don't Overlap");
      }

      System.out.println(findOverlapArea(K, L, M, N, P, Q, R, S));

      double totalBeforeOverlap = Math.abs(N - L) * Math.abs(M - K) + Math.abs(P - R) * Math.abs(Q - S);
      System.out.println(totalBeforeOverlap);

      System.out.println(totalBeforeOverlap - findOverlapArea(K, L, M, N, P, Q, R, S));
    }//main

}//Rectangles
