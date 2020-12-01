import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DB_Connection{
    private static final String SQCONN = "jdbc:sqlite:agenziaMatrimoniale.db";
    private static Connection driver = null;

    public static Connection getConnection() throws SQLException {
        try {
            Class.forName("org.sqlite.JDBC");
            driver = DriverManager.getConnection(SQCONN);
            System.out.println("Connection opened with the database successfully");

        }catch (ClassNotFoundException | SQLException e){
            e.printStackTrace();
        }
        return  driver;
    }
}

