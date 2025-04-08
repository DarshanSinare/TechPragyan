# FormEasy: "Smart Form Filling with Saved Details & Documents"

## Overview
Smart Form Filling is an automation solution that streamlines online form submissions by retrieving and auto-filling user data and uploading relevant documents. The system eliminates repetitive manual entries, reduces errors, and enhances productivity.

## Team Details
- **Team Name**: ClickLess Crew  
- **Team Leader**: Hase Chaitanya  
- **Team Members**: Sinare Darshan, Naik Krishna, Daule Suyog, Mandlik Sahil  
- **College**: Amrutvahini College of Engineering, Sangamner  

## Problem Statement
Filling online forms and uploading documents is time-consuming, repetitive, and error-prone. Users frequently enter the same details for job applications, banking KYC, university admissions, and government forms. This project aims to:
- **Save Time & Effort**: Automates repetitive tasks.
- **Eliminate Human Errors**: Reduces typos and incorrect document uploads.
- **Enhance Scalability**: Useful for enterprises, banks, and government automation.

## Proposed Solution
A web-based form-filling system that:
- Accepts a **form link (URL)** as input.
- Retrieves **user data and documents** from a database.
- **Auto-fills the form** with stored details.
- **Uploads necessary documents**.
- Allows users to **cross-check before submission**.

### Key Features
- **Automated Form Filling**: Extracts user data and fills forms with one click.
- **Auto Document Upload**: Attaches relevant documents.
- **User Review Option**: Ensures accuracy before final submission.
- **Error Reduction**: Uses pre-verified data.
- **Productivity Enhancement**: Ideal for large-scale form submissions.

## Technical Approach
### Technology Stack:
- **Frontend**: Python Library Tkinter.
- **Backend**: Python.
- **Database**: File Management System.
- **Automation**: Selenium.

### System Architecture:
- A **client-server model** where a database stores user data & documents.
- Uses **retrieval logic** to match form requirements with stored details.

## Workflow
1. User submits a **form link**.
2. System **fetches stored data** from the database.
3. **Auto-fills form fields**.
4. **Uploads required documents**.
5. User **reviews and edits** before final submission.
6. **Confirms submission** and receives a success message.

## Impact & Benefits
### For Individuals
- Faster job applications, university admissions, and government form submissions.
- Eliminates the hassle of entering the same details multiple times.

### For Businesses
- Streamlines HR, finance, and compliance processes.
- Helps banks and government agencies process bulk applications efficiently.

### For Government Services
- Reduces paperwork and enhances e-governance efficiency.

## Future Scope
- **AI-Powered Smart Autofill**: Uses machine learning to recognize form fields dynamically.
- **OCR-Based Document Extraction**: Auto-fills forms using scanned documents.
- **API Integration**: Connects with banking, HR, and government databases.
- **SaaS Model for Enterprises**: Allows seamless integration into business workflows.

## Conclusion
Smart Form Filling automates data entry and document uploads, ensuring efficiency, accuracy, and a hassle-free user experience. This innovation can be seamlessly integrated across multiple platforms, improving productivity for individuals and enterprises alike.

---

### Installation & Setup
#### Prerequisites
- Python 3.x
- Selenium WebDriver
- Google Chrome & ChromeDriver

#### Install Dependencies
```sh
pip install selenium flask 
```

#### Run the Application
```sh
python app.py
```

#### Usage
1. Enter **form URL**.
2. Input **user details** and upload necessary documents.
3. Click **'Fill Form'** to automate form submission.
4. Receive **confirmation and preview** of submitted data.


