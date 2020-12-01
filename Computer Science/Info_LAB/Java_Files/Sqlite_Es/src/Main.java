import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.*;

class SQLiteJDBC {
    public static void main(String[] args) {
        Connection c = null;

        try {
            Class.forName("org.sqlite.JDBC");
            c = DriverManager.getConnection("jdbc:sqlite:fabbrica.db");
        } catch ( Exception e ) {
            System.err.println( e.getClass().getName() + ": " + e.getMessage() );
            System.exit(0);
        }
        System.out.println("Connection opened with the database successfully");

        esercizi start = new esercizi();
        start.ex_1(c);
    }
}
