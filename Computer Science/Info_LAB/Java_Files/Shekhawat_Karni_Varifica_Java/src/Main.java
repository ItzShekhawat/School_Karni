import java.io.IOException;
import java.sql.*;
import java.util.Scanner;
import java.util.Vector;

public class Main {

    private static int choise;
    private  static Vector<Integer> vec_M = new Vector<Integer>(3);
    private  static Vector<Integer> vec_F = new Vector<Integer>(3);



    public static void main(String[] args) throws SQLException {
        //System.out.println("Programm Started...");
        Scanner console = new Scanner(System.in);

        do {
            System.out.println("Start Programm");
            System.out.println("==========================");
            System.out.println("Visualizzare candidati ordinati per sesso e nome, eventualmente incolonnati.");
            System.out.println("Generare i record per i possibili abbinamenti uomo-donna");
            System.out.println("Modificare abbinamenti per immissione giudizi (uno solo oppure entrambi)");
            System.out.println("cancellare abbinamenti con media giudizi < 50% oppure un giudizio < 25%");
            System.out.println("tramite una query parametrizzata trova e visualizza le coppie con una media giudizi al di sopra di un valore imputabile a tastiera.");
            System.out.println("Premi 6 per uscire.");
            System.out.println("Immettere scelta:");
            try {
                choise = console.nextInt();
            } catch (Exception e) {
                System.out.println("No Such option");
                System.out.println(e.toString());
            }
            switch (choise) {
                case 1:

                    Ordine_Candidati();

                    break;

                case 2:
                    record_make();
                    break;

                case 3:



                    break;

                case 4:



                    break;

                case 5 :


                    break;
            }
        } while (choise != 6);


    }

    private static void Ordine_Candidati() throws SQLException {
        Connection connect = DB_Connection.getConnection();
        Statement statement = connect.createStatement();
        ResultSet result;

        try {
            statement = connect.createStatement();
            String query = "SELECT id, nome, sesso FROM Candidati GROUP BY sesso, nome;";
            result = statement.executeQuery(query);
            while (result.next()) {
                if (result.getString("sesso") == "M"){
                    vec_M.add(Integer.parseInt(result.getString("id")));
                }else {
                    vec_F.add(Integer.parseInt(result.getString("id")));
                }
                System.out.println(result.getString("id")+ ","+result.getString("nome") + "," + result.getString("sesso"));
            }
        } catch (SQLException e) {
            System.out.println(e.toString());
        }
        // Closing the connection for others to use it
        connect.close();
    }

    private static void record_make() throws SQLException{
        Connection connect = DB_Connection.getConnection();
        Statement statement = connect.createStatement();
        //ResultSet result;

        try {

            for (int m = 0; m< vec_M.size(); m++){
                for (int f = 0 ; f < vec_F.size(); f++){
                    statement = connect.createStatement();
                    String query1 = "INSERT INTO Abbinamenti (id_1, id_2, giudizio_1, giudizio_2) VALUES(vec_M[m], vec_F[f], 60, 80);";
                    statement.executeUpdate(query1);
                    String query2 = "INSERT INTO Abbinamenti (id_1, id_2, giudizio_1, giudizio_2) VALUES(vec_M[m], vec_F[f], 70, 80);";
                    statement.executeUpdate(query2);
                    String query3 = "INSERT INTO Abbinamenti (id_1, id_2, giudizio_1, giudizio_2) VALUES(vec_M[m], vec_F[f], 80, 10);";
                    statement.executeUpdate(query3);

                }
            }

        }catch (SQLException e){
            System.out.println(e.toString());
        }

        connect.close();

    }

    private static void modifyChange() throws  SQLException{
        Connection connect = DB_Connection.getConnection();
        Statement statement = connect.createStatement();
        //ResultSet result;

        try {
            statement = connect.createStatement();
            String query = "UPDATE Abbinamenti";
            statement.executeUpdate(query);


        }catch (SQLException e){
            System.out.println(e.toString());
        }
        connect.close();

    }





}