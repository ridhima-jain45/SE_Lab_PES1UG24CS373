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

```
