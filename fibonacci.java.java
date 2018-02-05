import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;

public class TestClass{

  static int fib(int input){
    if (input <= 1){
      return input;
    }
    else{
      input = fib(input - 1) + fib(input - 2);
      return input;
    }
  }//fib

  public static void main (String args[])
  {
    int n = 9;
    System.out.println(fib(n));
  }

}
