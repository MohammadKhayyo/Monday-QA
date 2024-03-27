import subprocess
from Utils.configurations import ConfigurationManager


def run_pytest(parallel=False):
    # Directory where all tests are located
    ui_tests_path = "Tests/test_ui/End_to_End"

    # Basic command with the path to UI tests
    cmd = ["pytest", ui_tests_path, "--html=report.html"]

    # If parallel execution is enabled, modify the command to run with xdist
    if parallel:
        # Runs all tests except those marked as 'serial'
        cmd.extend(["-n", "8", "-m", "not serial"])
        subprocess.run(cmd)

        # Now run the serial tests without xdist
        cmd = ["pytest", ui_tests_path, "-m", "serial", "--html=report_serial.html"]
    else:
        # Optionally, use a different report name for serial tests
        cmd.extend(["--html=report_serial.html"])

    # Execute the pytest command
    subprocess.run(cmd)


if __name__ == "__main__":
    config_manager = ConfigurationManager()
    settings = config_manager.load_settings()
    is_parallel = settings['parallel']
    run_pytest(parallel=is_parallel)
