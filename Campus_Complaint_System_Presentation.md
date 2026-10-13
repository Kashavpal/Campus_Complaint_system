# Campus Complaint System
## 32-Slide Presentation Outline

Repository: https://github.com/Kashavpal/Campus_Complaint_system

---

## Slide 1: Title Slide
Title: Campus Complaint System
Subtitle: Digital Complaint Management Platform for Universities
Presented by: [Your Name]
Department / Institution: [Your Department / University]
Date: [Insert Date]

---

## Slide 2: Introduction
- Universities and colleges handle many student and administrative complaints.
- Many issues are reported informally and are difficult to track.
- There is a need for a strong digital grievance management solution.
- The Campus Complaint System addresses this issue with a structured workflow.

---

## Slide 3: Problem Statement
- Students often face confusion on where to file complaints.
- Complaints are not always tracked properly.
- Manual systems create delays and poor visibility.
- Sensitive complaints need controlled access.
- Teachers and admins require a structured workflow for follow-up.
- Institutions need transparency and accountability.

---

## Slide 4: Objectives of the Project
- Create a digital complaint submission system.
- Support multiple user roles with access control.
- Track complaints from creation to resolution.
- Improve response time and issue visibility.
- Maintain accountability with audit logs.
- Provide secure and user-friendly complaint handling.

---

## Slide 5: Scope of the Project
- Student complaint submission
- Teacher complaint review and updates
- Admin oversight and assignment
- Complaint status tracking and deadlines
- Notification center and audit records
- Secure login, validation, and file handling
- Local deployment using Flask and SQLite

---

## Slide 6: Significance of the Project
- Improves efficiency in campus grievance handling.
- Creates transparency between students and administration.
- Reduces paperwork and miscommunication.
- Enables faster issue resolution.
- Helps administrators monitor recurring campus concerns.
- Builds trust in the complaint process.

---

## Slide 7: Target Users
- Students: submit complaints and track progress
- Teachers: review and update complaints
- Admins: manage users, assignments, and workflows
- Campus authorities: monitor complaint trends and overdue cases

---

## Slide 8: Technology Stack
Backend:
- Python
- Flask

Frontend:
- HTML
- CSS
- JavaScript
- Jinja templates

Database:
- SQLite

Security and utilities:
- Flask-WTF
- Flask-Limiter
- Werkzeug security
- OpenCV and NumPy
- Pillow (PIL)

---

## Slide 9: System Architecture
- Presentation layer: HTML templates, CSS, JS
- Application layer: Flask routes and logic
- Security layer: role checks, session validation, CSRF, headers
- Data layer: SQLite database
- File/verification layer: image upload and identity checks

This architecture keeps the project modular, simple, and maintainable.

---

## Slide 10: Project Modules
- app/__init__.py: app creation and configuration
- app/routes.py: major web routes and business logic
- app/db.py: schema creation and migration logic
- app/security.py: decorators and safe file handling
- app/verification.py: image verification logic
- app/templates: UI pages
- app/static: CSS, JS, UI assets

---

## Slide 11: Application Initialization
- Loads environment variables from .env
- Creates Flask application instance
- Sets database path and upload folder
- Initializes app database tables
- Ensures system admin exists
- Registers routes and security protections
- Adds global security headers

---

## Slide 12: Security Features
- CSRF protection with Flask-WTF
- Password hashing using Werkzeug
- Rate limiting with Flask-Limiter
- Secure session cookie settings
- HTTP security headers
- Route restrictions using login and role decorators
- File type validation for uploads

---

## Slide 13: Role-Based Access Control
Three user roles:
- Admin
- Student
- Teacher

Each role has access to different actions and dashboards.
- Students can submit and view their complaints.
- Teachers can process assigned complaints.
- Admins manage the system and monitor operations.

---

## Slide 14: User Management
- Admin-created accounts
- Student registration with roll number and department details
- Temporary password mechanism after first login
- Password-change enforcement for new users
- User profile and photo support
- Tracking of active/inactive users

---

## Slide 15: Complaint Data Model
Key fields in complaints include:
- complaint_code
- student_id
- department, year, section
- category and severity
- description
- incident date and location
- previous report and follow-up details
- status and assigned teacher
- hidden flags for resolved items
- timestamps and audit metadata

---

## Slide 16: Complaint Submission Flow
1. Student logs in.
2. Student fills complaint form.
3. System validates required fields.
4. Complaint is assigned a unique code.
5. Complaint is saved in database.
6. Admin/teacher receives notification or assignment.
7. Complaint moves through review and resolution.

---

## Slide 17: Validation Rules
- Description must meet minimum length requirement.
- Incident details such as date and location are required.
- File upload restrictions are enforced.
- Complaint data is checked before saving.
- Student and role rules are verified server-side.
- Visible and hidden complaint rules are enforced consistently.

---

## Slide 18: Complaint Categories and Severity
Severity levels:
- RED: highest priority
- YELLOW: medium urgency
- GREEN: standard priority
- BLUE: low urgency

Complaint categories correspond to the issue type or complaint domain.
Severity helps prioritize handling and escalation decisions.

---

## Slide 19: Severity and Escalation Rules
- Severity is linked to urgency and response expectations.
- Sensitive RED complaints are kept away from regular teacher flows.
- High-priority cases may require admin attention.
- Ageing complaints are identified and flagged as overdue.
- The system supports priority-driven resolution.

---

## Slide 20: Complaint Lifecycle
Complaint lifecycle includes:
- Submitted
- Assigned
- In progress
- Pending review
- Resolved
- Hidden from view after resolution

Each stage is tracked and recorded for accountability.

---

## Slide 21: Teacher Workflow
Teachers can:
- view assigned complaints
- read complaint details and attachments
- update status and notes
- maintain timeline of action
- resolve or escalate complaints

This helps teachers work in a focused and structured environment.

---

## Slide 22: Admin Workflow
Admins can:
- create user accounts
- review the complaint dashboard
- assign complaints
- manage escalations and overdue cases
- monitor issue trends
- secure admin access and reset credentials when needed

---

## Slide 23: Student Workflow
Students can:
- register and log in
- submit complaints
- view complaint status
- access notifications
- see complaint history
- hide resolved complaints from their personal dashboard

---

## Slide 24: Notifications and Communication
- Notifications are stored in the database.
- Alerts include complaint submission, assignment, and status updates.
- They are visible through the app navigation area.
- Notifications can be marked as read once opened.
- This improves communication without depending on email.

---

## Slide 25: Overdue Complaint Monitoring
- Complaints are checked against severity-based time limits.
- RED: 24 hours
- YELLOW: 72 hours
- GREEN: 7 days
- BLUE: 10 days
- Overdue complaints are flagged when dashboards are accessed.
- This supports accountability and timeframe compliance.

---

## Slide 26: Audit Trail and Logging
- Complaint updates are recorded in a dedicated table.
- Admin actions are logged in audit logs.
- Details include actor, action, target, time, and IP information.
- This supports transparency and institutional accountability.
- Audit logs are crucial for grievance monitoring and review.

---

## Slide 27: File Upload and Verification
- Images and attachments are validated before save.
- Allowed file types are restricted to secure formats.
- Temporary verification images are cleaned up after use.
- The system includes a face verification feature using OpenCV.
- Verification is educational/prototype-level and not a production biometric solution.

---

## Slide 28: Database Design
Core tables:
- users
- complaints
- complaint_updates
- audit_logs
- notifications

The database stores both operational and audit information.
This supports both complaint processing and historical tracking.

---

## Slide 29: Testing and Validation
The repository includes a static validation suite.
It checks:
- Python compilation
- database table existence
- required complaint columns
- overdue logic and escalation checks
- notification and role rules
- CSRF and security header configuration

---

## Slide 30: Setup and Deployment
Steps:
1. Create Python virtual environment.
2. Install requirements.
3. Configure .env variables.
4. Run the app with python run.py.
5. Open the application in the browser.

Additional support:
- Windows setup script
- Admin reset script for local recovery

---

## Slide 31: Strengths and Benefits
- Easy to deploy and run locally
- Lightweight and practical architecture
- Strong role-based access control
- Clear complaint workflow from submission to resolution
- Better accountability and faster response time
- Good foundation for a real institutional grievance system

---

## Slide 32: Conclusion and Future Scope
Conclusion:
- The Campus Complaint System is a practical, secure, and useful grievance platform.
- It solves a genuine institutional problem with a simple but effective design.
- It combines education, software engineering, and real-world problem solving.

Future improvements:
- Email/SMS integration
- Advanced reporting dashboards
- Better biometric verification under compliance standards
- PostgreSQL migration for larger deployments
- More robust analytics and export features

---

## Slide 33: Q&A / Thank You
Questions?
Thank You.

Suggested closing message:
“Thank you for your attention. This project demonstrates how software can improve transparency, accountability, and efficiency in campus complaint management.”

---

## Final Note
This deck is designed to be a polished project presentation with 33 slides, balancing technical depth and presentation clarity.

The content is based on the repository at:
https://github.com/Kashavpal/Campus_Complaint_system
