import javax.swing.*;
import java.awt.*;
/**
 * Created by Jake on 11/5/15.
 */
public class Display extends JFrame
{

    char[][] pic;
    public Display( char[][] picture )
    {
        this.setPreferredSize(new Dimension(320, 330));
        this.pack();
        this.setVisible(true);
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);
        pic = picture;
    }

    @Override
    public void paint( Graphics g )
    {
        super.paint( g );

        for(int i = 0; i < pic.length; i++ )
        {
            for ( int j = 0; j < pic[i].length; j++ )
            {
                if(pic[j][i] == 'x')
                {
                    g.fillRect( (j+2)*10, (i+3)*10, 10, 10 );
                }
            }
        }
    }
}
