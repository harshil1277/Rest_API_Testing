import os
import subprocess
import random
import pandas as pd
import matplotlib.pyplot as plt

def check_and_kill_tmux_sessions():
    """Check if there is a running tmux session and kill it if found."""
    sessions = subprocess.run(["tmux", "ls"], capture_output=True, text=True)
    if "no server running" not in sessions.stderr:
        for line in sessions.stdout.splitlines():
            session_name = line.split(":")[0]
            subprocess.run(["tmux", "kill-session", "-t", session_name])

def start_service_and_run(tool, port):
    """Activate virtualenv, start the service, and run the testing tool."""
    os.system("source venv/bin/activate")
    subprocess.run(["python3", "run_small.py", tool, str(port)])

def generate_coverage_report(port):
    """Generate coverage report and return the path of the CSV file."""
    subprocess.run(["python3", "report_small.py", str(port)])
    return f"data/{tool}/res.csv"

def plot_coverage(csv_path):
    """Generate and save plot for the first column vs. row number."""
    df = pd.read_csv(csv_path, header=None)
    plt.figure()
    plt.plot(df.index[:6] + 1, df.iloc[:6, 0], marker='o', label='Line Coverage')
    plt.xlabel("Minute")
    plt.ylabel("Coverage (%)")
    plt.title("Line Coverage vs. Time")
    plt.legend()
    plt.grid(True)
    output_path = os.path.join(os.path.dirname(csv_path), "coverage_plot.png")
    plt.savefig(output_path)
    plt.close()
    return output_path

def main(tool, service):
    # Kill any running tmux sessions to avoid conflicts
    check_and_kill_tmux_sessions()

    # Randomly select a port number for this run
    port = random.randint(10000, 60000)

    # Start the service and run the tool
    start_service_and_run(tool, port)

    # Generate the coverage report and locate the CSV file
    csv_path = generate_coverage_report(port)

    # Plot the first column (line coverage) and save it
    plot_path = plot_coverage(csv_path)

    # Stop the service
    subprocess.run(["python3", "stop_service.py", service])

    print(f"CSV report saved at: {csv_path}")
    print(f"Coverage plot saved at: {plot_path}")

# Get tool and service name as inputs
if __name__ == "__main__":
    tool = input("Enter the tool name: ")
    service = input("Enter the service name: ")
    main(tool, service)

