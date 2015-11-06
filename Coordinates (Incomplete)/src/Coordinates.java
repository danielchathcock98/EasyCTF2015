/**
 * Created by Jake on 11/5/15.
 */

import java.io.File;
import java.util.Scanner;

public class Coordinates
{

    static int k = 0;

    public static void main(String args[])
    {
        try
        {
            char[][] picture = new char[ 31 ][ 31 ];

            for(int i = 0; i < picture.length; i++)
            {
                for ( int j = 0; j < picture[i].length; j++ )
                {
                    picture[i][j] = ' ';
                }
            }
//            Scanner in = new Scanner( new File("/Users/Jake/IdeaProjects/EasyCTF/src/qr.txt") );
            Scanner in = new Scanner( new File("./qr.txt") );

            String coords = in.nextLine();
            for(String i : coords.split( "\\(" ))
            {
                if(i.length() > 1)
                {
                    int x = Integer.parseInt( i.substring( 0, i.indexOf( "," ) ) );
                    int y = Integer.parseInt( i.substring( i.indexOf( " " )+1, i.indexOf( ")" ) ) );
                    picture[x][y] = 'x';
                    k++;
                }
            }

            for(int i = 0; i < picture.length; i++)
            {
                for ( int j = 0; j < picture[i].length; j++ )
                {
                    System.out.print(picture[i][j]);
                }
                System.out.println();

            }

            // Just inverting picture to get right colors (cause Java graphics is hard)
            for (int i = 0; i < picture.length; i++)
            {
                for (int j = 0; j < picture[i].length; j++)
                {
                    if (picture[i][j] == 'x')
                    {
                        picture[i][j] = ' ';
                    }
                    else
                    {
                        picture[i][j] = 'x';
                    }
                }
            }
            Display out = new Display( picture );


        }
        catch ( Exception ex )
        {
            ex.printStackTrace();
        }



    }
}
