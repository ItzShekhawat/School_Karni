import java.io.IOException;
import java.sql.*;
import java.util.Scanner;

public class Main {

    private static  int choise;
    private static Connection conn;

    public static void main(String[] args) throws SQLException {
        System.out.println("Programm Started...");
        Scanner console = new Scanner(System.in);
        

        do {
            System.out.println("Sondaggio gradimento libri");
            System.out.println("==========================");
            System.out.println("Premi 1 per visualizzare tutti i record.");
            System.out.println("Premi 2 per aggiungere nuovo record.");
            System.out.println("Premi 3 per cancellare un record.");
            System.out.println("Premi 4 per aggiungere dei voti.");
            System.out.println("Premi 5 per sovrascrivere i dati esistenti.");
            System.out.println("Premi 6 per uscire.");
            System.out.println("Immettere scelta:");
            try {
                choise = console.nextInt();
            } catch (Exception e) {
                System.out.println("Scelta non riconosciuta");
                System.out.println(e.toString());
            }
            switch (choise) {
                case 1:
                    // Print out the Title, the Author, and the vote number
                    view_Title_Author_nVoti();

                    break;

                case 2:

                    // Add a new row in the Voti table
                    addVoti();

                    break;

                case 3:

                    // Modify a Voti row
                    modifyVoti();

                    break;

                case 4:

                    //Eliminate a Row in Voti
                    eliminateVoti();

                    break;
            }
        } while (choise != 6);
    }

    // Starting with sql query -----------------------------------------------------------------------

    private static void view_Title_Author_nVoti() throws SQLException{
        Connection connect = dbConnection.getConnection();
        Statement statement = connect.createStatement();
        ResultSet result;

        try {
            statement = connect.createStatement();
            String query = "SELECT titolo, autore, nVoti FROM Libri INNER JOIN Voti ON Libri.id = Voti.id_libro;";
            result = statement.executeQuery(query);
            while (result.next()) {
                System.out.println(result.getString("nome") + "," + result.getString("autore") + "," + result.getString("nVoti"));
            }
        } catch (SQLException e) {
            System.out.println(e.toString());
        }
        // Closing the connection for others to use it
        connect.close();
    }

    private static void addVoti () throws SQLException {
        Connection connect = dbConnection.getConnection();
        Statement statement = connect.createStatement();
        // ResultSet result;

        try {
            statement = connect.createStatement();
            String query = "INSERT INTO Voti(id, nVoti, id_libro) VALUES(4, 8, 1);";
            statement.executeUpdate(query);

        } catch (SQLException e) {
            System.out.println(e.toString());
        }

        // Closing the connection for others to use it
        connect.close();
    }

    private static void modifyVoti () throws SQLException {
        Connection connect = dbConnection.getConnection();
        Statement statement = connect.createStatement();
        //ResultSet result = null;

        try {
            statement = connect.createStatement();
            String query = "UPDATE Voti SET nVoti = 9 WHERE id = 3;";
            statement.executeUpdate(query);

        } catch (SQLException e) {
            System.out.println(e.toString());
        }

        // Closing the connection for others to use it
        connect.close();
    }

    private static void eliminateVoti () throws SQLException {
        Connection connect = dbConnection.getConnection();
        Statement statement = connect.createStatement();
        //ResultSet result = null;

        try {
            statement = connect.createStatement();
            String query = "DELETE FROM Voti WHERE id = 4;";
            statement.executeUpdate(query);

        } catch (SQLException e) {
            System.out.println(e.toString());
        }

        // Closing the connection for others to use it
        connect.close();
    }
}
