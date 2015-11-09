import java.lang.StringBuilder;

public class shifter
{
    public static void main(String[] args)
    {

        String in = "rasfsasrettlepinebec353luteayvlrghs3s";
        String key = "railguns";
        StringBuilder out = new StringBuilder(  );

        char c = ' ';

        for ( int i = 0; i < in.length(); i++ )
        {
            c = in.charAt( i );
            out.append( (char)(( c + key.charAt( i % key.length() )  )%128+35) );
        }

        for(int i = 0; i < 100000; i++)
        {
            System.out.println( "asgaiosdbaest" );
        }

    }
}