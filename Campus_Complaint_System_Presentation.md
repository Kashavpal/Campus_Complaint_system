# Campus Complaint System
# Detailed Presentation Content for PowerPoint

Repository: https://github.com/Kashavpal/Campus_Complaint_system

---

## Slide 1: Title Slide
Title: Campus Complaint System
Subtitle: A Role-Based Digital Complaint Management Platform for Educational Institutions
Presented by: [Your Name]
Course / Department: [Your Department / University Name]
Date: [Insert Date]

Visual suggestion:
- University campus image
- dashboard screenshot of complaint system
- icon set for students, teachers, admin, complaint tickets

---

## Slide 2: Introduction
- Universities and colleges often rely on informal complaint channels.
- Students and staff may face delays, lack of accountability, and poor visibility.
- The Campus Complaint System solves this by creating a structured digital workflow.
- It helps manage complaints from the moment they are submitted until they are resolved.

Key idea:
A complaint management system is not just a form; it is a complete workflow for communication, escalation, accountability, and monitoring.

---

## Slide 3: Problem Statement
Problems in a traditional complaint system:
- No centralized database for complaint records
- Students do not know whom to contact
- Complaints are often lost, delayed, or ignored
- There is no status tracking after submission
- Teachers and administrators have no consistent workflow
- Sensitive complaints need restricted access and escalation
- No proper historical record exists for audits and accountability

Impact of the problem:
- Poor trust in the grievance mechanism
- Delayed issue resolution
- Lack of transparency
- Difficulty in identifying recurring campus problems

---

## Slide 4: Objectives of the Project
Main objectives:
- Create a digital complaint submission portal for students
- Support role-based access for admin, student, and teacher
- Track complaint status from submission to closure
- Enable secure authentication and user identity checks
- Provide automated notifications and overdue tracking
- Maintain audit logs for compliance and accountability
- Deliver a lightweight, easy-to-use system with minimal deployment complexity

Secondary objectives:
- Improve grievance response efficiency
- Sort complaints by urgency and category
- Support secure complaint handling in a campus environment

---

## Slide 5: Scope of the Project
This project covers:
- User registration and role assignment
- Complaint creation and validation
- Complaint assignment and updates
- Severity and category classification
- Overdue monitoring and alert generation
- Secure login and role restrictions
- Student and teacher dashboard views
- Notification center and audit system
- Temporary identity verification for registration and complaint validation

Scope is limited to:
- a university complaint workflow
- local deployment using Flask and SQLite
- educational/prototype environment rather than enterprise-grade biometric systems

---

## Slide 6: Project Significance
Why this project matters:
- Improves transparency between students and campus administration
- Helps educational institutions respond faster to serious issues
- Reduces manual paperwork and unstructured communication
- Encourages accountability by recording who did what and when
- Provides a scalable template for grievance management in institutions

This project is especially relevant in colleges and universities where complaints involve academics, facilities, harassment, safety, administrative issues, and student support.

---

## Slide 7: Functional Requirements
Functional requirements include:
- Student registration with roll number and photo
- Admin account creation and reset support
- Complaint entry with fields such as category, severity, incident date, location, and description
- Complaint status updates by teachers and admins
- Secure login and password change enforcement
- Role-based access restrictions
- Complaint visibility controls for resolved items
- Notification features for assignments and updates
- Overdue detection based on severity and time thresholds

These requirements ensure the system is realistic and practical for campus use.

---

## Slide 8: Non-Functional Requirements
Non-functional requirements:
- Security: CSRF protection, password hashing, secure session handling
- Reliability: database-backed records and audit logs
- Performance: quick in-app dashboard loading and minimal response delay
- Usability: simple UI and clean, responsive design
- Maintainability: modular Flask architecture
- Data integrity: validation of uploaded data and complaint records
- Privacy: limited access to sensitive complaints and proper file handling

These attributes are necessary for a credible institutional system.

---

## Slide 9: Technology Stack
Frontend:
- HTML
- CSS
- JavaScript
- Jinja templates for dynamic rendering

Backend:
- Python
- Flask web framework

Database:
- SQLite

Security libraries:
- Flask-WTF (CSRF protection)
- Flask-Limiter (rate limiting)
- Werkzeug security (password hashing)

Image and verification:
- OpenCV
- NumPy
- PIL (Python Imaging Library)

Additional:
- .env configuration
- SQLite auto-migration support

---

## Slide 10: System Architecture Overview
The application follows a simple layered architecture:
1. Presentation layer: HTML templates + CSS + JS
2. Application layer: Flask routes and business logic
3. Security layer: login/session checks, role validation, headers, CSRF
4. Data layer: SQLite database tables for users, complaints, audit log, notifications
5. File handling layer: upload storage, image validation, verification image processing

Key modules:
- app/__init__.py: app initialization, config, security hooks
- app/routes.py: endpoints for login, dashboard, complaints, admin and teacher actions
- app/db.py: schema definition and database setup
- app/security.py: login/role decorators and safe file handling
- app/verification.py: face similarity verification logic

---

## Slide 11: Application Initialization and Configuration
The app is created through Flask app factory pattern:
- Loads environment variables from .env
- Creates Flask app instance
- Sets app config values such as secret key, database path, upload folder
- Initializes database tables on startup
- Ensures admin user exists
- Registers routes and security middleware
- Adds global security headers after responses

Important security settings include:
- SESSION_COOKIE_HTTPONLY
- X-Frame-Options: DENY
- Referrer-Policy: no-referrer
- Content-Security-Policy

These settings reduce the risk of common web vulnerabilities.

---

## Slide 12: User Roles and Access Control
The system supports three user types:

1. Admin
- Creates user accounts
- Manages platform-wide visibility
- Reviews complaint escalations
- Resets admin access safely
- Monitors overdue and touch-critical complaints

2. Student
- Submits complaints
- Views complaint history
- Provides complaint metadata
- Can hide resolved complaints from personal view

3. Teacher
- Receives assignments
- Updates resolution status
- Adds notes and status transitions
- Works within restricted complaint access rules

Access control is enforced by decorators and session-based role checks.

---

## Slide 13: Role-Based Security Model
Security mechanisms:
- login_required decorator ensures logged-in access
- role_required decorator restricts route access
- Session checks prevent unauthorized browsing
- Password hashing ensures stored credentials are non-readable
- CSRF protection reduces cross-site request forgery risk
- Rate limiting prevents abuse of public endpoints

This is crucial because a complaint system contains sensitive information and institutional actions.

---

## Slide 14: User Management System
Functional capabilities:
- Admin-created accounts
- Student registration with roll number and department metadata
- Teacher and admin role separation
- Temporary password enforcement after first login
- Password change requirement when account is newly created
- Active/inactive user handling through user records

The database stores:
- username
- password hash
- role
- full name
- roll number
- department
- year
- section
- original photo
- must_change_password

---

## Slide 15: Complaint Data Model
The complaint record stores:
- complaint_code: unique complaint identifier
- student_id: student who submitted the complaint
- department, year, section: campus metadata
- category: complaint domain
- severity: RED / YELLOW / GREEN / BLUE
- description: complaint text
- attachment: optional uploaded document
- incident_date and incident_location
- previous_report: past reports information
- follow_up_details: additional continuation details
- status: submitted, in progress, resolved, etc.
- assigned_teacher_id: assigned case owner
- student_hidden and admin_hidden: visibility controls
- overdue_notified_at: time tracking for escalations
- created_at and updated_at timestamps

This model ensures the complaint is complete, auditable, and tracked over time.

---

## Slide 16: Complaint Categories and Severity Levels
Categories may correspond to academic, administrative, infrastructure, safety, or service categories depending on the platform setup.

Severity model:
- RED: critical, sensitive, urgent, high-impact complaints
- YELLOW: moderate urgency
- GREEN: standard complaints
- BLUE: low priority complaints

Key property:
The severity is category-driven and immutable for the complaint lifecycle.

This helps prioritize support and escalation appropriately.

---

## Slide 17: Complaint Submission Process
The complaint process generally includes:
1. Student logs in
2. Student enters complaint information
3. Validation confirms minimum description length and required metadata
4. System creates unique complaint code
5. Complaint is stored in SQLite database
6. Notification is sent to relevant parties
7. Admin or teacher reviews complaint and assigns workflow owner

This process provides transparency and a formal complaint history.

---

## Slide 18: Complaint Validation Rules
Validation rules implemented in the project include:
- Complaint description must be at least 50 characters
- Required incident details like date and location
- Optional previous report details and follow-up details
- Student must be bound to roll number and proper department metadata
- Uploads must be valid image or allowed attachment types
- Form inputs are checked server-side to reduce tampering

Examples of validation logic:
- file type validation
- minimum length checks
- numeric/date checks where necessary
- role-based route protection

---

## Slide 19: Complaint Workflow and Status Flow
Complaint status is updated throughout lifecycle:
- Submitted
- Assigned
- In Progress
- Pending Review
- Resolved
- Hidden / archived from user view (soft delete behavior)

Teacher or admin updates progress and notes.
Complaint updates are logged in complaint_updates table, which preserves the history of actions.

This creates a timeline of actions and decisions, improving accountability.

---

## Slide 20: Complaint Timeline and Audit Trail
The observed project adds strong audit and timeline features:
- Every complaint update is stored in complaint_updates
- Admin actions are recorded in audit_logs
- Important system events are captured, including complaint creation, assignment, and status changes
- Notification entries track what messages were shown to users

Audit logs include:
- actor_id
- action
- target_type
- target_id
- ip_address
- created_at

This makes the system suitable for institutional accountability.

---

## Slide 21: Teacher Assignment and Escalation Model
Once complaint is submitted:
- Admin or system workflow decides complaint owner
- Teacher is assigned to a complaint
- Complaints with sensitive red severity may be kept out of regular teacher flow
- High-priority complaints may need faster review or admin intervention

This gives the project a proper escalation model instead of a flat queue.

---

## Slide 22: Overdue Complaint Monitoring
One of the advanced features is overdue detection.
- Complaints are tracked against service target windows
- Severity-based targets are used:
  - RED: 24 hours
  - YELLOW: 72 hours
  - GREEN: 7 days
  - BLUE: 10 days
- If the deadline is exceeded, the complaint is marked overdue
- Overdue notifications are generated when relevant dashboards are opened

Result:
The system helps ensure grievances are not forgotten and promotes faster response.

---

## Slide 23: Notification System
The application includes in-app notification features:
- Complaint submitted
- New complaint submitted to admin/teacher
- Complaint assigned
- Complaint status updated
- Overdue complaint notifications

Notifications are stored in the notifications table and shown in top navigation.
A notification is marked as read when opened.

This improves responsiveness without requiring external email gateway integration.

---

## Slide 24: Soft-delete / Hidden Complaints
The project includes a modern improvement:
- Resolved complaints can be hidden from student or admin views
- The records are not physically deleted
- Audit trail and complaint history remain preserved
- This is a soft-delete pattern rather than permanent removal

This is useful because institutional complaint records are often required for later review or legal/compliance reasons.

---

## Slide 25: Secure File Uploads and Attachments
The project validates uploaded files tightly:
- Allowed image types: jpg, jpeg, png, webp
- Allowed attachments: image types + pdf
- Invalid files are rejected
- Uploaded files are stored in designated folders
- Temporary verification images are removed after use
- Files are handled safely to prevent invalid content

This is important for an institutional environment where users may upload sensitive evidence.

---

## Slide 26: Image Verification Module
The app includes verification logic in app/verification.py.
- It loads an original reference image and candidate image
- Uses OpenCV face detection to detect a face in each image
- Compares facial features using histogram correlation
- Returns a similarity score
- Accepts verification only if score reaches a threshold (0.72 in the implementation)

Important note:
This is described in the README as an educational prototype and not a production biometric solution.

This is a useful prototype because it demonstrates identity verification, but real deployment would require stronger governance and biometric standards.

---

## Slide 27: Database Design Details
The SQLite schema contains tables for:
- users
- complaints
- complaint_updates
- audit_logs
- notifications

Main relationships:
- users.id links to complaint.student_id and complaint.assigned_teacher_id
- complaints.id links to complaint_updates.complaint_id and notifications.complaint_id
- audit logs track actions externally without altering complaint logic

This ensures a normalized and easy-to-maintain database design.

---

## Slide 28: Student User Journey
The student experience includes:
- Registration and profile creation
- Uploading a profile photo
- Accessing secure login
- Setting a new password upon first login
- Creating a complaint with required details
- Monitoring complaint progress
- Viewing notifications
- Hiding resolved complaints if desired

This creates a clear and user-friendly complaint pipeline.

---

## Slide 29: Teacher User Journey
The teacher experience includes:
- Login and dashboard access
- Viewing assigned complaints
- Reviewing details, attachments, and prior updates
- Updating complaint status and notes
- Escalating or resolving cases
- Working under complaint priority and sensitive-case rules

This makes teacher workflow focused and efficient.

---

## Slide 30: Admin User Journey
Admin responsibilities:
- Create or manage system users
- Monitor complaint queue and severity levels
- Assign complaints to teachers
- Observe overdue issues and urgent cases
- Maintain legal/audit visibility over complaints
- Reset temporary admin access safely without revealing current password

Administration is the central governance layer of the system.

---

## Slide 31: Security and Privacy Considerations
Project-specific security measures:
- Hashed passwords
- Session protection
- CSRF tokens
- Rate-limited requests
- Safe file upload validation
- X-Frame-Options and other HTTP security headers
- Role restrictions on sensitive actions
- Temporary verification image cleanup

Privacy considerations:
- Sensitive complaints are kept out of normal teacher workflow where necessary
- Personal data is restricted through public-facing access controls
- Resolved complaints can be hidden while preserving the record for auditing

---

## Slide 32: Testing and Validation
The repository includes a static validation script: tests/test_project_static.py.

It verifies:
- all Python files compile
- required database tables exist
- complaint schema includes important fields
- unresolved complaint cap rules are removed
- incident details are required
- overtime/overdue rules are implemented
- notifications exist
- red-case logic exists for restricted teacher assignment
- CSRF and security headers are configured

This provides a lightweight but meaningful quality check framework.

---

## Slide 33: Setup and Run Guide
Project setup flow:
1. Create virtual environment: python -m venv .venv
2. Activate environment
3. Install dependencies: pip install -r requirements.txt
4. Create .env from .env.example
5. Set secret key and temporary admin password
6. Run: python run.py
7. Open: http://127.0.0.1:5000

Windows setup:
- Use setup_windows.bat for automatic environment and service startup

Admin password reset:
- Use python reset_admin.py to restore default admin account access when needed

---

## Slide 34: Strengths of the Project
Main strengths:
- Simple and understandable architecture
- Lightweight deployment
- Good role-based access control
- Strong complaint lifecycle management
- Severity-based prioritization and overdue monitoring
- In-app notifications and audit capability
- Security-focused design for a prototype system
- Good fit for university demonstration and academic projects

This project demonstrates good software engineering thinking despite being lightweight.

---

## Slide 35: Limitations and Future Enhancements
Current limitations:
- SQLite may not scale for large institutions
- No direct email/SMS integration yet
- Verification feature is educational and not production-grade biometric technology
- No advanced analytics dashboard currently
- No multi-language support or mobile app interface

Possible future improvements:
- Add dashboard analytics and reports
- Integrate email/SMS alerts
- Add real biometric or stronger identity verification under compliance rules
- Add API support for campus integrations
- Add export to PDF/Excel reports
- Add role-specific dashboards and charts
- Upgrade to PostgreSQL for larger-scale institutional deployment

---

## Slide 36: Business and Social Impact
The project can positively impact student life and campus governance by:
- creating a formal and transparent complaint path
- reducing administrative confusion and backlog
- improving accountability for issue resolution
- helping institutions act on recurring problems faster
- creating better trust between students and administrators

This is especially valuable in institutions where complaints are often ignored or delayed due to manual systems.

---

## Slide 37: Why This Project Is Relevant
This project is relevant because it combines:
- web application development
- database design
- security engineering
- role-based access control
- business process modeling
- verification systems
- real-world problem solving

It is a strong example of how software can be used to improve institutional services and support student welfare.

---

## Slide 38: Conclusion
The Campus Complaint System is a practical and effective digital solution for complaint handling in educational institutions.

It provides:
- a structured complaint workflow
- secure user management
- role-based access control
- automated escalation and tracking
- notification support
- auditable records
- a scalable learning platform for future upgrades

In summary, the project is not only a complaint system; it is a complete case-management workflow designed to improve trust, efficiency, and accountability.

---

## Slide 39: Final Q&A Slide
Questions?
Thank You.

Possible discussion points:
- Deployment in real educational institutions
- Scaling to larger user bases
- Security hardening for production deployment
- Additional analytics and reporting features
- Integration with student information systems

---

## Presentation Notes for Speaker
When presenting this project, the speaker should highlight:
- the problem being solved
- the role-based architecture
- the complaint lifecycle and auditability
- the security and privacy design
- the deadline-based escalation features
- the educational/prototype nature of verification logic

Suggested storytelling order:
1. Problem in campus grievance handling
2. Need for a digital system
3. Our solution and features
4. Technical architecture
5. Security, validation, and data design
6. Project impact and future growth

---

## Recommended Slide Count
For a detailed academic presentation, use 30–40 slides.
For a concise project demo, use 12–15 slides.
For a final-year viva, 20–25 slides is ideal.

---

## Project Summary in One Paragraph
The Campus Complaint System is a Flask-based web application designed to streamline complaint management within a university or college environment. It supports multiple user roles, ensures secure authentication and input validation, tracks complaint status and escalation, stores audit logs, and provides a structured workflow that improves accountability and responsiveness. The project combines practical software engineering principles with a real-world institutional problem, making it highly relevant for academic demonstration and future institutional deployment.

---

## Short Project Tagline
“Digitalizing campus grievance management with secure, structured, and accountable complaint handling.”

This content is now significantly more detailed and suitable for a full presentation deck.
