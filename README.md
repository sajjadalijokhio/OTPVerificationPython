# Email OTP Verification System

This is a simple Python script for generating and verifying OTPs (One-Time Passwords) via email using the SMTP protocol. It can be used in various applications where email-based OTPs are required for authentication.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You should have Python installed on your system.
- You should have a Gmail account to send OTP emails.
- Make sure to enable "Less secure apps" in your Gmail settings.
- Generate an "App Password" for your Gmail account for secure authentication.

## Installation

1. Clone the repository to your local machine:
2. Navigate to the project directory:
3. Open the Python script and make the following updates:

   - Replace `'your email'` with your Gmail email address.
   - Replace `'your app password'` with the App Password you generated for python app.
   - Update `'sender's email'` with the email address you want to appear as the sender.
   - Update `'receiver's email'` with the email address where you want to send the OTP.

## Usage

1. Run the script using your Python interpreter:
2. The script will generate a 6-digit OTP and send it to the specified email address.
3. Check the receiver's email for the OTP and enter it when prompted.
4. The script will verify the OTP. If it's correct, it will print "OTP Verified!"; otherwise, it will display "Sorry! Please Enter a Valid OTP."
