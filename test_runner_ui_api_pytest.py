import os
import subprocess
from Utils.configurations import ConfigurationManager


def run_pytest(parallel=False):
    # Load configuration
    config = ConfigurationManager().load_settings()

    ui_tests_path = "Tests/demo"
    reports_dir = "reports"
    os.makedirs(reports_dir, exist_ok=True)

    # Update python_path to use Anaconda's python executable
    # Assuming the Anaconda environment is named 'myenv' and Anaconda is installed in its default location
    python_path = "C:\\ProgramData\\Anaconda3\\envs\\myenv\\python.exe"

    # Base command using Anaconda environment's Python
    base_cmd = [python_path, "-m", "pytest", ui_tests_path]

    html_report = os.path.join(reports_dir, "report.html")

    if parallel:
        parallel_cmd = base_cmd + ["-n", "3", "-m", "not serial", f"--html={html_report}"]
        try:
            subprocess.run(parallel_cmd, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Tests failed with return code {e.returncode}. Continuing the build...")

    try:
        serial_html_report = os.path.join(reports_dir, "report_serial.html")
        serial_cmd = base_cmd + ["-m", "serial", f"--html={serial_html_report}"]
        subprocess.run(serial_cmd, check=True)
    except subprocess.CalledProcessError as e:
        if e.returncode == 5:  # No tests were collected
            print("No serial tests were found.")
        else:
            print(e.returncode)
    else:
        non_parallel_cmd = base_cmd + [f"--html={html_report}"]
        try:
            subprocess.run(non_parallel_cmd, check=True)
        except subprocess.CalledProcessError as e:
            print(e.returncode)


if __name__ == "__main__":
    config_manager = ConfigurationManager()
    settings = config_manager.load_settings()
    is_parallel = settings['parallel']
    run_pytest(parallel=is_parallel)
