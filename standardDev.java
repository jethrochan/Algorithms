import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;

public class StandardDeviation {

    public static double calculateSD(double numArray[])
    {
        double sum = 0.0, standardDeviation = 0.0;

        for(double num : numArray) {
            sum += num;
        }

        double mean = sum/(numArray.length);

        for(double num: numArray) {
            standardDeviation += Math.pow(num - mean, 2);
        }//without sqrt, below, stddevvar / numArray.length = variance.

        return Math.sqrt(standardDeviation/(numArray.length));
    }//calculateSD

    public static void main(String[] args) {
        double[] numArray = { 1.1,1.2,1.3,1.3,1.3,1.3,1.3,1.3 };
        double SD = calculateSD(numArray);

        System.out.format("Standard Deviation = %.6f", SD);
    }//main

}
