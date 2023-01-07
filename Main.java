import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;

public class Main {
    public static boolean isVowel(String let){
        String[] vowels = {"a","e", "i" , "o", "u", "y"};
        for(String vowel : vowels)
        {
            if(let.equals(vowel))
            {
                return true;
            }
        }
        return false;


    }
    public static String pigLatin(String str)
    {
        String firstLet = str.substring(0,1);
        if(!(firstLet.equals("y")) && isVowel(firstLet)){
            return str + "-hay";
        }
        else
        {
            int firstVow = 0;
            boolean found = false;
            for(int i = 1; i < str.length() && !found; i++)
            {
                if(isVowel(str.substring(i, i+1)))
                {
                    firstVow = i;
                    found = true;
                }

            }
            return str.substring(firstVow) + str.substring(0,firstVow) + "-ay" + " ";
        }
    }
    public static void pigLatinFile(String inFile, String outFile) throws FileNotFoundException {
        Scanner fscan = new Scanner(new File(inFile));
        PrintWriter fwrite = new PrintWriter(new File(outFile));
        while (fscan.hasNextLine()) {
            String line = fscan.nextLine();
            Scanner lineScanner = new Scanner(line);
            String pigLatinLine = "";
            while (lineScanner.hasNext()) {
                pigLatinLine = pigLatinLine + pigLatin(lineScanner.next() + "");
            }
            fwrite.println(pigLatinLine);
        }
        fwrite.close();

    }



    public static void main(String[] args) throws FileNotFoundException{
	   pigLatinFile("test2.txt", "testOut.txt");
    }
}
