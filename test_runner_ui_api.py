import os
import subprocess


def run_pytest(parallel=False):
    # Load configuration
    ui_tests_path = "test/api_and_ui"
    reports_dir = "reports"
    os.makedirs(reports_dir, exist_ok=True)

    # Base command using the virtual environment's Python
    base_cmd = ["venv\\Scripts\\python.exe", "-m", "pytest", ui_tests_path]

    html_report = os.path.join(reports_dir, "report.html")

    non_parallel_cmd = base_cmd + [f"--html={html_report}"]
    try:
        subprocess.run(non_parallel_cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(e.returncode)


if __name__ == "__main__":
    run_pytest(parallel=False)
