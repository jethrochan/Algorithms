import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.lang.Math.*;

public class MainClass
{
  static String inputStr = "abba";

  public static boolean isPalindrome(String inputPalin){
   	  char [] input = inputPalin.toCharArray();
      int strLen = inputPalin.length();

      for(int i = 0; i < inputPalin.length(); i++){
        if(input[i] != input[inputPalin.length() - 1 - i])
          return false;
      }

      return true;
  }

  // arguments are passed using the text field below this editor
  public static void main(String[] args)
  {
    System.out.println(isPalindrome(inputStr));
    System.out.println(isPalindrome("defg"));
    System.out.println(isPalindrome("madamamadam"));
  }
}
