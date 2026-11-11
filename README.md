# SE_Lab_PES1UG24CS373
# Alumni Mentorship & Mock Interview Platform (Lab 1-3)

**Course:** Software Engineering Labs
**Problem Statement:** #06 — Campus & Academic Operations
**Target Stakeholders:** Student Mentee, Alumni Mentor

A platform connecting students with alumni mentors through intelligent domain matching, availability-based session booking, mock interviews, and structured post-interview scorecards.

---

## Lab 1: Requirements Engineering & UML Use-Case Modelling

**File:** `lab1/LAB 1.pdf`

Contains:
- **Requirements Table** — 5 Functional Requirements (FR-001–FR-005) and 2 Non-Functional Requirements (NFR-001–NFR-002), each with ID, Type, Description, Priority, Acceptance Criteria, and Rationale.
- **UML Use-Case Diagram** — Actors: Student Mentee, Alumni Mentor. Includes an `«include»` relationship (Book Mentorship Session → Send Calendar Invite) and an `«extend»` relationship (Reschedule Session → Book Mentorship Session).
- **Use-Case Flow Specification** — One-page flow for *Book Mentorship Session* (UC-02), covering Preconditions, Postconditions, Main Success Scenario, and an Alternate Flow (slot already booked).

---

## Lab 2: Agile Planning — Epics, User Stories & Sprint Simulation

**File:** `lab2/Lab2.pdf`

### Epics (3)
| Epic | Description | Stories | Points |
|---|---|---|---|
| Epic 1: Mentor Discovery & Booking | Enable students to find, filter, and book sessions with alumni mentors based on domain expertise and availability | 4 | 14 |
| Epic 2: Mentor Management, Feedback & Privacy | Allow alumni mentors to manage schedules, conduct interviews, provide structured feedback, and ensure data privacy | 4 | 19 |
| Epic 3: Notifications & Data Privacy | Automated reminders for students and mentors; user data protection | 4 | 16 |
| **Total** | | **12** | **49** |

### User Stories (12)
Written in standard "As a / I want to / So that" format, covering mentor search and filtering (AMP-4, AMP-5), one-click booking (AMP-6, AMP-7), mentor availability management (AMP-8, AMP-9), mock interview scorecards (AMP-10, AMP-11), automated reminders (AMP-12, AMP-13), and data privacy/soft-deletion (AMP-14, AMP-15). Each story is sized using Fibonacci story points (3–8) and assigned a priority (High/Medium).

### Sprint Simulation
- **Sprint 1:** 22 points — completed
- **Sprint 2:** 18 points — completed
- **Sprint 3:** 9 points — completed
- Tracked via Jira board (To Do → In Progress → Done) with burndown charts for each sprint

### Reflection
Covers estimation accuracy, backlog prioritization, sprint alignment, and team velocity (sustainable at ~15–22 points/sprint), based on the burndown chart trends.

---

## Lab 3: Component Modelling & Architectural Pattern Selection

**File:** `lab3/LAB3.pdf`

### Architecture Selected
**Layered Architecture** (Presentation → Business → Data)

### Components (5)
| Component | Responsibility |
|---|---|
| User Interface Component | Student & mentor web/app interactions |
| Matching & Booking Component | Domain matching, session booking, availability management |
| Interview & Scorecard Component | Mock interview session handling, scorecard recording |
| Notification & Calendar Sync Component | Calendar invites and reminders |
| Database Component | Stores profiles, availability, sessions, scorecards; enforces soft-deletion |

### Interfaces (4)
1. User Interface ↔ Matching & Booking — *Search / book / set availability*
2. Matching & Booking ↔ Interview & Scorecard — *Handoff at session start*
3. Matching & Booking ↔ Notification & Calendar Sync — *Trigger invite on booking*
4. Matching & Booking ↔ Database — *Persist / retrieve data*

Contains:
- **Component Diagram** — subsystem grouping (Presentation, Platform Services), ports, ball-and-socket interface notation.
- **Written Justification** — architecture selection, two scenario-specific reasons, one security advantage, one performance benefit.

---
# Balloon Pop (Lab 4- Vibe coding)

A simple Balloon Pop game built using **Python and Pygame**.

## Features

* Fixed balloon click detection.
* Added 3 balloon types:

  * Normal: +10
  * Bonus: +25
  * Penalty: -10
* Added 3 lives; missing a balloon costs 1 life.
* Added a 30-second countdown timer.
* Added game-over and restart functionality.
* Added visual indicators for score, lives, and time.
* Added videos.
* Please check the link to the forked repository - https://github.com/ridhima-jain45/05_balloon_pop

## Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the game:

```bash
python main.py
```

Press **R** after game over to restart.

# Lab 5 – Static Code Analysis

## Overview
This lab focuses on using static code analysis tools to identify and fix code quality, security, and formatting issues in a Python application.

The application used for analysis is a **Movie Theater Seat Reservation System** (`theater_system.py`), which supports seat reservations, releasing seats, generating ticket codes, and saving/loading reservation data.

## Tools Used
- **Pylint** – Checks code quality, naming conventions, documentation, and potential programming errors.
- **Bandit** – Identifies potential security vulnerabilities in Python code.
- **Flake8** – Checks Python code for formatting and style violations.

## Work Performed
1. Created a Python virtual environment and installed the required analysis tools.
2. Ran Pylint, Bandit, and Flake8 on the original application to identify issues.
3. Recorded the initial analysis results in separate report files.
4. Fixed the identified issues, including:
   - Mutable default arguments.
   - Bare exception handling.
   - Weak MD5 hashing.
   - Overly permissive file permissions.
   - Missing docstrings and incorrect naming conventions.
   - File-handling and formatting issues.
5. Ran all three tools again to verify the corrections.
6. Saved the final analysis results in separate report files.

## Final Results
- **Pylint:** 10.00/10
- **Bandit:** No issues identified.
- **Flake8:** 0 violations.

## Repository Contents
- `theater_system.py` – Corrected Python application.
- `CodeCoverageTest_...` – Not applicable to this lab.
- `pylint_report_before.txt` and `pylint_report_after.txt`
- `bandit_report_before.txt` and `bandit_report_after.txt`
- `flake8_report_before.txt` and `flake8_report_after.txt`
- `issues.md` – Summary of identified issues and their fixes.

## Commits
The fixes were committed separately to maintain a clear history of the changes made for Pylint, Bandit, and Flake8.

## Conclusion
The lab provided practical experience in static code analysis and demonstrated how automated tools can improve Python code quality, security, readability, and consistency.

# Lab 6 – Code and Branch Coverage Analysis

## Objective
To analyse the code and branch coverage of the Bookstore Trade-In application using Python's `pytest` and `coverage` tools.

## Work Completed

1. Analysed the existing `bookstore_trade_in.py` application and identified its functions and decision branches.
2. Created separate Python test files for code coverage and branch coverage.
3. **Code Coverage:** Created `CodeCoverageTest_application.py` with test cases covering input validation, book formats, conditions, payouts, rejection scenarios, and scanner calibration.
4. **Branch Coverage:** Created `BranchCoverageTest_application.py` with test cases to exercise both outcomes of conditional statements and different execution paths.
5. Executed the tests using `pytest` and measured coverage using the `coverage` package.
6. Recorded before-and-after coverage results using terminal screenshots.
7. Maintained separate Git commits for the code coverage and branch coverage test files.

## Final Results

| Metric | Before | After |
|---|---:|---:|
| Code Coverage | 49% | 100% |
| Branch Coverage | 45% | 100% |

- Code coverage: **13 tests passed**
- Branch coverage: **29 tests passed**
- Total branches covered: **40 out of 40**
- Partial branches remaining: **0**

## Commands Used

**Code Coverage:**
```bash
python -m coverage erase
python -m coverage run --source=bookstore_trade_in -m pytest -v CodeCoverageTest_application.py
python -m coverage report -m
```

**Branch Coverage:**
```bash
python -m coverage erase
python -m coverage run --branch --source=bookstore_trade_in -m pytest -v BranchCoverageTest_application.py
python -m coverage report -m
```

## Files

- `bookstore_trade_in.py` – Application under test.
- `CodeCoverageTest_application.py` – Code coverage test cases.
- `BranchCoverageTest_application.py` – Branch coverage test cases.
- `README.md` – Lab work summary.

## Conclusion

Successfully achieved 100% code coverage and 100% branch coverage for the Bookstore Trade-In application through separate and comprehensive test suites.

# Lab 7 – Fuzzing for Input Validation Bugs

## Objective
To explore fuzz testing using the Hypothesis library, identify input validation bugs, and improve application robustness through defensive programming.

## Tools Used
- Python 3.12
- Hypothesis
- Pytest

## Files
- `processor.py` – Python application containing three functions for ISBN formatting, depreciation calculation, and condition multiplier lookup. Updated with input validation and error handling.
- `test_processor.py` – Hypothesis-based fuzz tests for all three functions.

## Implementation
1. Installed Hypothesis and Pytest.
2. Executed the original application.
3. Used Hypothesis to generate unexpected inputs and identify bugs.
4. Fixed the identified issues using defensive input validation.
5. Re-ran the application and all fuzz tests.

## Run the Tests

Install dependencies:

```bash
pip install hypothesis pytest
```

Run the application:

```bash
python processor.py
```

Run the tests:

```bash
python -m pytest test_processor.py -q
```

## Result
All three Hypothesis tests passed successfully after fixing the application.

**Final Test Result:** `3 passed`

## Learning Outcome
Learned how property-based fuzz testing helps identify unexpected input validation bugs and how defensive programming improves application reliability.
