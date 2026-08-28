# JARVIS STORE AI — Architecture V1

## 1. Vision

JARVIS is an AI-powered desktop assistant for store and
inventory management.

The long-term goal is to allow the user to interact with
JARVIS using natural language and voice to:

- search company inventory data
- calculate stock and material movement
- analyze daily/monthly/yearly data
- create Excel and PDF reports
- search and read files
- process documents and challans
- automate approved computer tasks
- provide system information
- use vision/OCR
- perform approved web tasks

JARVIS must be modular and extensible.

---

## 2. Core Architecture

User Interface
      |
      v
JARVIS Conversation Layer
      |
      v
AI/LLM Layer
      |
      v
Intent and Tool Router
      |
      +----------------+
      |                |
      v                v
Read Tools         Action Tools
      |                |
      v                v
Database          Computer/File APIs
      |
      v
Company Data

The AI does not directly control the database.
The AI requests approved tools.

---

## 3. Main Modules

### AI Brain

Responsible for:

- understanding user requests
- understanding Hindi, Hinglish and English
- selecting tools
- explaining results
- maintaining conversation context

The AI must never invent numerical inventory data.

### Tool System

Tools are controlled functions that perform specific tasks.

Examples:

- get_stock
- search_inventory
- get_incoming
- get_outgoing
- compare_periods
- calculate_inventory
- generate_excel
- generate_pdf
- search_files
- read_file
- system_info
- screenshot
- open_application

### Database

The database stores structured store information.

Main entities:

- materials
- transactions
- incoming
- outgoing
- purchases
- suppliers
- departments

### Calculation Engine

All important numerical calculations must be deterministic.

Examples:

- current stock
- total incoming
- total outgoing
- net movement
- percentage change
- period comparison
- averages
- low stock detection

### Reporting

JARVIS can generate:

- daily reports
- weekly reports
- monthly reports
- yearly reports
- material reports
- incoming reports
- outgoing reports
- stock reports

Export formats:

- Excel
- PDF
- CSV

---

## 4. Inventory Rules

Current stock should be calculated from validated transactions.

Basic concept:

Opening Stock + Incoming - Outgoing = Current Stock

The exact business rules can be extended later.

The system must validate:

- material exists
- quantity is valid
- date is valid
- transaction type is valid
- required fields are present

---

## 5. AI Safety Rules

JARVIS must not fabricate:

- stock numbers
- transaction numbers
- dates
- supplier information
- reports
- calculations

If information is unavailable, JARVIS must clearly say
that the information is unavailable.

AI-generated explanations must be based on actual tool results.

---

## 6. Read and Write Separation

Read operations:

- search inventory
- view stock
- view transactions
- calculate reports
- analyze data

Write operations:

- add incoming
- add outgoing
- edit records
- delete records
- import data

Write operations require validation.

Sensitive or destructive operations require explicit
user confirmation.

---

## 7. Memory

JARVIS will eventually have:

### Short-term memory

Conversation context.

### Long-term memory

Only useful non-sensitive preferences and application
context.

Company records remain in the database, not in AI memory.

---

## 8. Voice

Voice pipeline:

Microphone
   |
Speech-to-Text
   |
JARVIS
   |
Tool execution
   |
Response
   |
Text-to-Speech
   |
Speaker

Text chat must always remain available as an alternative.

---

## 9. Vision and OCR

Future JARVIS versions may process:

- screenshots
- invoices
- challans
- documents
- scanned material records

The system should extract structured information and show
a confirmation before creating database records.

---

## 10. Computer Control

Future Windows version may provide controlled tools for:

- opening applications
- opening files
- searching files
- taking screenshots
- reading screen content
- typing approved text
- interacting with approved applications

Dangerous actions such as:

- deleting files
- shutdown
- restart
- installing software
- changing important system settings

must require explicit confirmation.

---

## 11. Security

The production system should support:

- authentication
- role-based permissions
- audit logs
- secure secrets
- environment variables
- database backups

Possible roles:

- Admin
- Store Manager
- Store User
- View Only

Real company data must not be placed in a public GitHub
repository.

Secrets such as API keys and passwords must never be committed.

---

## 12. User Interface

Main sections:

- Dashboard
- JARVIS
- Inventory
- Incoming
- Outgoing
- Purchases
- Suppliers
- Reports
- Files
- System
- Settings

JARVIS should be the primary interface.

The user should be able to perform most common operations
through natural language.

---

## 13. Dashboard

Dashboard should show:

- current stock
- today's incoming
- today's outgoing
- low stock materials
- recent transactions
- important alerts

---

## 14. JARVIS Conversation

Example requests:

"August mein PCB kitna incoming hua?"

"July aur August compare karo."

"PCB001 ka current stock batao."

"Sabse zyada outgoing material kaunsa hai?"

"August ki Excel report banao."

"Low stock materials batao."

JARVIS should understand natural language rather than
requiring command syntax.

---

## 15. Audit Log

Important actions should be recorded.

Audit information:

- timestamp
- user
- request
- tool used
- action
- result
- status

This allows administrators to understand what JARVIS did.

---

## 16. Development Strategy

Development will happen in phases.

Phase 1:
Project foundation and database.

Phase 2:
Inventory CRUD and APIs.

Phase 3:
JARVIS AI and tool calling.

Phase 4:
Calculations and reports.

Phase 5:
Excel/PDF export.

Phase 6:
Voice.

Phase 7:
Vision/OCR.

Phase 8:
Windows computer control.

Phase 9:
Authentication and production security.

Phase 10:
Windows desktop packaging and deployment.

---

## 17. Development Principle

Do not build everything at once.

Each module must be:

- modular
- testable
- documented
- replaceable
- connected through clear interfaces

The system should be developed using AI-assisted coding,
but generated code must be tested before being trusted.

---

## 18. Current Development Environment

Initial development is being performed from an Android
phone using Termux and GitHub.

The final target is a Windows desktop application.

The architecture must therefore remain portable and
cloud/Git compatible during development.

---

## 19. Future Expansion

Possible future modules:

- advanced analytics
- anomaly detection
- scheduled reports
- notifications
- email integration
- barcode/QR scanning
- document processing
- supplier analytics
- forecasting
- local AI models
- multiple users
- hardware/system integrations

These modules must be added without rewriting the core
system.
