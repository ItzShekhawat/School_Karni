import java.sql.*;
import java.util.Scanner;

public class esercizi{

    public void sqlite_connection() {
        return;
    }

    public void ex_1(Connection c){
        //  Per far diventare 3 il responsabile di PLFR
        Statement result = null;
        try{
            result = c.createStatement();
            result.executeUpdate("UPDATE SedeA SET CodR = 3 WHERE CodOperaio = 'PLFR';");


        } catch (SQLException throwables) {
            throwables.printStackTrace();
            System.out.println(throwables.getClass().getName() + " : " + throwables.getMessage());
        }

    }

    public void ex_2(Connection c){
        // Per eliminare il record dell'operaio  RSMR
        Statement result = null;
        try{
            result = c.createStatement();
            result.executeUpdate("DELETE FROM SedeB WHERE CodOperaio = 'RSMR';");

        } catch (SQLException throwables) {
            throwables.printStackTrace();
            System.out.println(throwables.getClass().getName() + " : " + throwables.getMessage());
        }

    }

    public void ex_3(Connection c){
        // Per aumentare di 30€ lo stipendio di tutti gli operai della SedeA dei responsabili
        Statement result = null;
        try{
            result = c.createStatement();
            result.executeUpdate("UPDATE SedeA SET Stipendio = Stipendio + 30.00;");

        } catch (SQLException throwables) {
            throwables.printStackTrace();
            System.out.println(throwables.getClass().getName() + " : " + throwables.getMessage());
        }
    }
    public void ex_4(Connection c){
        // Per reinserire la riga dell’operaio RSMR
        Statement result = null;
        try{
            result = c.createStatement();
            result.executeUpdate("INSERT INTO SedeB (CodOperaio, Sesso, Assunto_il, Stipendio, CodR) VALUES ('RSMR', 'F', '2011-05-05', 880.72, 2);");

        } catch (SQLException throwables) {
            throwables.printStackTrace();
            System.out.println(throwables.getClass().getName() + " : " + throwables.getMessage());
        }

    }

    public void ex_5(Connection c){
        // Codice e data assunzione degli operai/e della sede B del responsabile
        // il cui nome e cognome viene inserito da tastiera in ordine crescente di data di assunzione
        Statement result = null;
        Scanner scan= new Scanner(System.in);
        String name = scan.nextLine();
        String surname = scan.nextLine();
        ResultSet output = null;

        try{
            result = c.createStatement();
            output = result.executeQuery("SELECT SedeB.CodOperaio, SedeB.Assunto_il " +
                    "FROM SedeB, Responsabili " +
                    "WHERE SedeB.CodR = Responsabili.CodRep AND " +
                    "Responsabili.Nome = '" + name  + "' AND Responsabili.Cognome = '" + surname + "' ORDER BY Assunto_il ASC ;");
            while (output.next()){
                System.out.println(output.getString("CodOperaio")+ ", " + output.getString("Assunto_il"));
            }
        } catch (SQLException throwables) {
            throwables.printStackTrace();
            System.out.println(throwables.getClass().getName() + " : " + throwables.getMessage());
        }

    }
    public void ex_6(Connection c){
        // Lo stipendio massimo degli operai della sede A, quello minimo e quello medio

        Statement result = null;
        ResultSet output = null;

        try{
            result = c.createStatement();
            output = result.executeQuery("SELECT MAX(Stipendio) AS StipendioMassimo, MIN(Stipendio) AS StipendioMinimo, " +
                    "AVG(Stipendio) AS StipendioMedio FROM SedeB;");
            while(output.next()){
                System.out.println(output.getString("StipendioMassimo") + "," + output.getString("StipendioMinimo") +
                        "," + output.getString("StipendioMedio"));
            }
        } catch (SQLException throwables) {
            throwables.printStackTrace();
            System.out.println(throwables.getClass().getName() + " : " + throwables.getMessage());
        }

    }

    public void ex_7(Connection c){
        // Contare gli operai/e della sede B con responsabile di codice X inserito da tastiera

        Statement result = null;
        Scanner scan= new Scanner(System.in);
        String code = scan.nextLine();
        ResultSet output = null;

        try{
            result = c.createStatement();
            output = result.executeQuery("SELECT COUNT(*) AS NumeroOperai FROM SedeB WHERE SedeB.CodR = '" + code + " ;");

            output.next();
            System.out.println(output.getString("NumeroOperai"));
        } catch (SQLException throwables) {
            throwables.printStackTrace();
            System.out.println(throwables.getClass().getName() + " : " + throwables.getMessage());
        }

    }



}
