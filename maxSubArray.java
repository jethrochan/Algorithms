import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;

public class Kadane{

  static int kadane(int arr[]){
    int currentMax, globalMax;
    currentMax = globalMax = arr[0];

    for(int i = 1; i < arr.length; i++){ //i must start at 1
      if (arr[i] <= currentMax + arr[i]) {
        currentMax = currentMax + arr[i];
      }//if
      else{
        currentMax = arr[i];
      }

      if (currentMax > globalMax) {
        globalMax = currentMax;
      }//if
    }//for

    return globalMax;

  }//fib()

  public static void main (String args[])
  {
    int inputArr[] = {11, -1, -6, 16, -5, -100, 12};
    System.out.println(kadane(inputArr));
    //use assert here.
  }

}
