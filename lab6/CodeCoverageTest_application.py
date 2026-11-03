
import pytest

from bookstore_trade_in import (
    process_book_buybacks,
    inspect_scanner_calibration
)


def test_invalid_inputs():
    with pytest.raises(ValueError):
        process_book_buybacks("not a list", 5.0)

    with pytest.raises(ValueError):
        process_book_buybacks([], -1.0)


def test_all_formats_and_conditions():
    batches = [
        {
            "intake_approved": True,
            "format": "textbook",
            "books": [
                {"condition": "mint"},
                {"condition": "poor"},
                {"condition": "good"}
            ]
        },
        {
            "intake_approved": True,
            "format": "hardcover",
            "books": [{"condition": "good"}]
        },
        {
            "intake_approved": True,
            "format": "paperback",
            "books": [{"condition": "good"}]
        },
        {
            "intake_approved": True,
            "format": "magazine",
            "books": []
        }
    ]

    result = process_book_buybacks(batches, 5.0)

    assert result["total_payout"] == 129.0
    assert result["status"] == "COMPLETED"


def test_unapproved_batch_is_skipped():
    batches = [
        {
            "intake_approved": False,
            "format": "textbook",
            "books": [{"condition": "mint"}]
        }
    ]

    result = process_book_buybacks(batches, 5.0)

    assert result["total_payout"] == 0.0
    assert result["status"] == "ZERO_CREDIT"


def test_missing_pages_are_rejected():
    batches = [
        {
            "intake_approved": True,
            "format": "paperback",
            "books": [
                {"missing_pages": 2, "condition": "good"},
                {"missing_pages": 0, "condition": "good"}
            ]
        }
    ]

    result = process_book_buybacks(batches, 0.0)

    assert result["total_payout"] == 8.0
    assert result["status"] == "COMPLETED"


def test_counterfeit_non_textbook():
    batches = [
        {
            "intake_approved": True,
            "format": "paperback",
            "books": [
                {"counterfeit": True},
                {"counterfeit": False, "condition": "good"}
            ]
        }
    ]

    result = process_book_buybacks(batches, 0.0)

    assert result["total_payout"] == 8.0
    assert result["status"] == "COMPLETED"


def test_counterfeit_textbook_stops_batch():
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

    assert result["total_payout"] == 0.0
    assert result["status"] == "ZERO_CREDIT"


def test_store_credit_bonus():
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
    assert result["status"] == "COMPLETED"


def test_audit_rejection():
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

    assert result["total_payout"] == 0.0
    assert result["status"] == "AUDIT_REJECTED"


def test_empty_batches_and_empty_books():
    assert process_book_buybacks([], 5.0)["status"] == "ZERO_CREDIT"

    result = process_book_buybacks(
        [{"intake_approved": True, "books": []}],
        0.0
    )

    assert result["status"] == "ZERO_CREDIT"


def test_scanner_no_data():
    assert inspect_scanner_calibration([]) == "NO_DATA"
    assert inspect_scanner_calibration(None) == "NO_DATA"


def test_scanner_calibrated():
    assert inspect_scanner_calibration([[], [2, 5, 3, 4]]) == "CALIBRATED"


def test_scanner_error_streak_resets():
    readings = [[6, 3, 7, 2, 6]]
    assert inspect_scanner_calibration(readings) == "CALIBRATED"


def test_scanner_requires_recalibration():
    readings = [[2, 6, 7, 1]]
    assert inspect_scanner_calibration(readings) == "RECALIBRATE"
