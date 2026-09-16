// Utó irat, 3 órája szopok ezzel és közel sincs a vége XD
//tutorial vid: https://www.geeksforgeeks.org/java/ways-to-read-input-from-console-in-java/
// Másik tutorial oldal: https://www.w3schools.com/java/

import java.util.Scanner;
//keret = int(input("keret normál ára:"))
//lencse = int(input("lencse normál ára:"))
//year_curr = int(input("Jelenlegi év :"))
//birth_year = int(input("születési év :"))

//        int keret = ;
//        int lencse = ;
//        int year_curr = ;
//        int birth_year = ;

//print(f"Ön a szemüvegkeret árából, ami {keret} Ft, {year_curr-birth_year}% kedvezményt kap! \n A szemüveglencse ára: {lencse} Ft \n ---------------------------- \n Szemüveg vételára : {round(keret*(1-((year_curr-birth_year)/100))+lencse)}")

public class idk {

    public static void main(String[]args) {
        Scanner s = new Scanner(System.in);
        System.out.println("keret normál ára: ");
        int keret = s.nextInt();
        System.out.println("lencse normál ára: ");
        int lencse = s.nextInt();
        System.out.println("Jelenlegi év: ");
        int year_curr = s.nextInt();
        System.out.println("születési év: ");
        int birth_year = s.nextInt();

        System.out.println("Ön a szemüvegkeret árából, ami " + keret + "Ft, " + (year_curr - birth_year) + "% kedvezményt kap!\n" +  "A szemüveglencse ára: " + lencse + "Ft\n" + "----------------------------\n" + "A szemüveg vételára:" + Math.round((keret*(1-((year_curr-birth_year)/100.0))+lencse))   );
    s.close();
    }

}

//VÉGE!!! MEGUTÁLTAM AZ ÉLETEMET IS EZEK UTÁN.
