import json
import os

REPORT_PATH = "/workspace/report.json"


def load_report():
    assert os.path.exists(REPORT_PATH), "report.json not found"
    with open(REPORT_PATH, "r") as f:
        return json.load(f)


def test_report_file_exists():
    """Success Criterion 1"""
    assert os.path.exists(REPORT_PATH)


def test_report_has_required_keys():
    """Success Criterion 2"""
    report = load_report()
    required_keys = ["total_requests", "status_codes", "unique_ips"]

    for key in required_keys:
        assert key in report


def test_total_requests_correct():
    """Success Criterion 3"""
    report = load_report()
    assert report["total_requests"] == 10


def test_status_code_counts_correct():
    """Success Criterion 4"""
    report = load_report()
    expected_status = {
        "200": 6,
        "404": 2,
        "500": 2
    }
    assert report["status_codes"] == expected_status


def test_unique_ip_count_correct():
    """Success Criterion 5"""
    report = load_report()
    assert report["unique_ips"] == 4
