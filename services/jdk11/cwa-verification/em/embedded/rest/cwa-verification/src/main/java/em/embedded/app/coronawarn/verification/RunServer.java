package em.embedded.app.coronawarn.verification;


import app.coronawarn.verification.VerificationApplication;
import org.evomaster.client.java.controller.EmbeddedSutController;
import org.evomaster.client.java.controller.InstrumentedSutStarter;
import org.evomaster.client.java.controller.api.dto.AuthenticationDto;
import org.evomaster.client.java.controller.api.dto.SutInfoDto;
import org.evomaster.client.java.controller.db.DbCleaner;
import org.evomaster.client.java.controller.problem.ProblemInfo;
import org.evomaster.client.java.controller.problem.RestProblem;
import org.springframework.boot.SpringApplication;
import org.springframework.context.ConfigurableApplicationContext;
import org.springframework.jdbc.core.JdbcTemplate;

import java.sql.Connection;
import java.sql.SQLException;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

/**
 * Class used to start/stop the SUT. This will be controller by the EvoMaster process
 */
public class RunServer extends EmbeddedSutController {

    public static void main(String[] args) {

        int port = 40101;
        if (args.length > 0) {
            port = Integer.parseInt(args[0]);
        }

        RunServer controller = new RunServer(port);
        controller.startSut();
    }


    private ConfigurableApplicationContext ctx;
    private Connection connection;


    public RunServer() {
        this(40101);
    }

    public RunServer(int port) {
        setControllerPort(port);
    }

    @Override
    public String startSut() {

        ctx = SpringApplication.run(VerificationApplication.class, new String[]{
                "--server.port=50116",
                "--spring.profiles.active=local,external,internal",
                "--management.server.port=-1",
                "--server.ssl.enabled=false",
                "--spring.datasource.url=jdbc:h2:mem:testdb;DB_CLOSE_DELAY=-1;"
        });

        if (connection != null) {
            try {
                connection.close();
            } catch (SQLException e) {
                throw new RuntimeException(e);
            }
        }
        JdbcTemplate jdbc = ctx.getBean(JdbcTemplate.class);

        try {
            connection = jdbc.getDataSource().getConnection();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

        return "http://localhost:" + getSutPort();
    }

    protected int getSutPort() {
        return (Integer) ((Map) ctx.getEnvironment()
                .getPropertySources().get("server.ports").getSource())
                .get("local.server.port");
    }


    @Override
    public boolean isSutRunning() {
        return ctx != null && ctx.isRunning();
    }

    @Override
    public void stopSut() {
        ctx.stop();
    }

    @Override
    public String getPackagePrefixesToCover() {
        return "app.coronawarn.verification.";
    }

    @Override
    public void resetStateOfSUT() {
        DbCleaner.clearDatabase_H2(connection, List.of("DATABASECHANGELOG"));
    }

    @Override
    public ProblemInfo getProblemInfo() {
        String schema = new Scanner(RunServer.class.getResourceAsStream("/api-docs.json"), "UTF-8").useDelimiter("\\A").next();

        return new RestProblem(
                null, //"http://localhost:" + getSutPort() + "/api/docs",
                null,
                schema
        );
    }

    @Override
    public SutInfoDto.OutputFormat getPreferredOutputFormat() {
        return SutInfoDto.OutputFormat.JAVA_JUNIT_5;
    }

    @Override
    public List<AuthenticationDto> getInfoForAuthentication() {
        return null;
    }

    public Connection getConnection() {
        return connection;
    }



}
