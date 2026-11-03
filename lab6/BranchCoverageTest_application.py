
import pytest

from bookstore_trade_in import (
    process_book_buybacks,
    inspect_scanner_calibration
)


def test_invalid_batches_type():
    with pytest.raises(ValueError):
        process_book_buybacks("invalid", 5.0)


def test_negative_bonus():
    with pytest.raises(ValueError):
        process_book_buybacks([], -5.0)


def test_valid_empty_batches():
    result = process_book_buybacks([], 5.0)
    assert result["status"] == "ZERO_CREDIT"


def test_unapproved_batch():
    batches = [
        {"intake_approved": False, "format": "textbook"}
    ]
    result = process_book_buybacks(batches, 0.0)
    assert result["status"] == "ZERO_CREDIT"


def test_textbook_format():
    batches = [
        {
            "intake_approved": True,
            "format": "textbook",
            "books": [{"condition": "good"}]
        }
    ]
    result = process_book_buybacks(batches, 0.0)
    assert result["total_payout"] == 40.0


def test_hardcover_format():
    batches = [
        {
            "intake_approved": True,
            "format": "hardcover",
            "books": [{"condition": "good"}]
        }
    ]
    result = process_book_buybacks(batches, 0.0)
    assert result["total_payout"] == 15.0


def test_paperback_format():
    batches = [
        {
            "intake_approved": True,
            "format": "paperback",
            "books": [{"condition": "good"}]
        }
    ]
    result = process_book_buybacks(batches, 0.0)
    assert result["total_payout"] == 8.0


def test_unsupported_format():
    batches = [
        {
            "intake_approved": True,
            "format": "magazine",
            "books": [{"condition": "good"}]
        }
    ]
    result = process_book_buybacks(batches, 0.0)
    assert result["status"] == "ZERO_CREDIT"


def test_empty_books():
    batches = [
        {
            "intake_approved": True,
            "format": "paperback",
            "books": []
        }
    ]
    result = process_book_buybacks(batches, 0.0)
    assert result["status"] == "ZERO_CREDIT"


def test_missing_pages():
    batches = [
        {
            "intake_approved": True,
            "format": "paperback",
            "books": [{"missing_pages": 2}]
        }
    ]
    result = process_book_buybacks(batches, 0.0)
    assert result["status"] == "ZERO_CREDIT"


def test_no_missing_pages():
    batches = [
        {
            "intake_approved": True,
            "format": "paperback",
            "books": [{"missing_pages": 0}]
        }
    ]
    result = process_book_buybacks(batches, 0.0)
    assert result["total_payout"] == 8.0


def test_counterfeit_paperback():
    batches = [
        {
            "intake_approved": True,
            "format": "paperback",
            "books": [{"counterfeit": True}]
        }
    ]
    result = process_book_buybacks(batches, 0.0)
    assert result["status"] == "ZERO_CREDIT"


def test_counterfeit_textbook():
    batches = [
        {
            "intake_approved": True,
            "format": "textbook",
            "books": [
                {"counterfeit": True},
                {"condition": "mint"}
            ]
        }
    ]
    result = process_book_buybacks(batches, 0.0)
    assert result["status"] == "ZERO_CREDIT"


def test_mint_condition():
    batches = [
        {
            "intake_approved": True,
            "format": "paperback",
            "books": [{"condition": "mint"}]
        }
    ]
    result = process_book_buybacks(batches, 0.0)
    assert result["total_payout"] == 10.0


def test_poor_condition():
    batches = [
        {
            "intake_approved": True,
            "format": "paperback",
            "books": [{"condition": "poor"}]
        }
    ]
    result = process_book_buybacks(batches, 0.0)
    assert result["total_payout"] == 3.2


def test_other_condition():
    batches = [
        {
            "intake_approved": True,
            "format": "paperback",
            "books": [{"condition": "good"}]
        }
    ]
    result = process_book_buybacks(batches, 0.0)
    assert result["total_payout"] == 8.0


def test_store_credit_enabled():
    batches = [
        {
            "intake_approved": True,
            "format": "paperback",
            "payout_in_credit": True,
            "books": []
        }
    ]
    result = process_book_buybacks(batches, 5.0)
    assert result["total_payout"] == 5.0


def test_store_credit_disabled():
    batches = [
        {
            "intake_approved": True,
            "format": "paperback",
            "payout_in_credit": False,
            "books": [{"condition": "good"}]
        }
    ]
    result = process_book_buybacks(batches, 5.0)
    assert result["total_payout"] == 8.0


def test_audit_rejected():
    batches = [
        {
            "intake_approved": True,
            "format": "paperback",
            "books": [
                {"missing_pages": 1},
                {"missing_pages": 1},
                {"missing_pages": 1},
                {"missing_pages": 1},
                {"missing_pages": 1}
            ]
        }
    ]
    result = process_book_buybacks(batches, 0.0)
    assert result["status"] == "AUDIT_REJECTED"


def test_audit_not_rejected():
    batches = [
        {
            "intake_approved": True,
            "format": "paperback",
            "books": [{"condition": "good"}]
        }
    ]
    result = process_book_buybacks(batches, 0.0)
    assert result["status"] == "COMPLETED"


def test_zero_credit():
    result = process_book_buybacks([], 0.0)
    assert result["status"] == "ZERO_CREDIT"


def test_completed_payout():
    batches = [
        {
            "intake_approved": True,
            "format": "paperback",
            "books": [{"condition": "good"}]
        }
    ]
    result = process_book_buybacks(batches, 0.0)
    assert result["status"] == "COMPLETED"


def test_scanner_empty_matrix():
    assert inspect_scanner_calibration([]) == "NO_DATA"
    assert inspect_scanner_calibration(None) == "NO_DATA"


def test_scanner_empty_device():
    assert inspect_scanner_calibration([[]]) == "CALIBRATED"


def test_scanner_error_below_threshold():
    assert inspect_scanner_calibration([[4, 3, 5]]) == "CALIBRATED"


def test_scanner_single_high_error():
    assert inspect_scanner_calibration([[6, 2]]) == "CALIBRATED"


def test_scanner_two_consecutive_high_errors():
    assert inspect_scanner_calibration([[6, 7]]) == "RECALIBRATE"


def test_scanner_error_streak_reset():
    assert inspect_scanner_calibration([[6, 2, 7]]) == "CALIBRATED"


def test_scanner_multiple_devices():
    assert inspect_scanner_calibration([[6], [2, 3]]) == "CALIBRATED"
