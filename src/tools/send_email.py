import smtplib
from email.mime.text import MIMEText
from pydantic import BaseModel, Field
import json
from ibm_watsonx_orchestrate.run import connections
from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission

#toggle this to true if you'd like to send a real email via gmail
USE_CACHED_RESPONSE = True


@tool(
    permission=ToolPermission.READ_ONLY,
    name="send_email_gmail",
    description="Send an email using Gmail."
)
def send_gmail_email(to_email: str, subject: str, body: str) -> str:
    """
    Sends an email via Gmail using an app password.
    If USE_CACHED_RESPONSE is True, returns a cached response instead of sending.

    Args:
        to_email (str): Recipient's email address.
        subject (str): Subject of the email.
        body (str): Body content of the email.

    Returns:
        str: Success or error message.
    """
    if USE_CACHED_RESPONSE:
        return (
            f'Email with subject "{subject}" '
            f'and body "{body}" '
            f'sent to {to_email}.'
        )

    # Retrieve Gmail credentials via Watson Orchestrate connection
    conn = connections.basic_auth("gmail")
    gmail_user = conn.username
    app_password = conn.password

    # Create MIME message
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = gmail_user
    msg["To"] = to_email

    # Send email via SMTP
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(gmail_user, app_password)
            smtp.send_message(msg)

        return (
            f'Email with subject "{subject}" '
            f'and body "{body}" '
            f'sent successfully to {to_email}!'
        )
    except Exception as e:
        return f"Error sending email: {e}"
