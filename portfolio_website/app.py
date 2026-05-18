from flask import Flask, render_template, request, flash, redirect, url_for
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'zaki-portfolio-secret-2025'

# ============================================================
#   SIRF YAHAN APNI DETAILS BHARO — BAKI KUCH MAT CHHUAO
# ============================================================
SENDER_EMAIL    = "zakiulhusnain37405@gmail.com"   # Tumhari Gmail
SENDER_PASSWORD = "yyrh axcv ldvs edwv"            # Gmail App Password (16 digits)
RECEIVER_EMAIL  = "zakiulhusnain37405@gmail.com"   # Jahan mail aani chahiye
# ============================================================


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contact', methods=['POST'])
def contact():

    name         = request.form.get('name', '').strip()
    email        = request.form.get('email', '').strip()
    subject      = request.form.get('subject', '').strip()
    project_name = request.form.get('project_name', '').strip() or 'Not specified'
    budget       = request.form.get('budget', '').strip()       or 'Not specified'
    message      = request.form.get('message', '').strip()
    timestamp    = datetime.now().strftime('%d %B %Y, %I:%M %p')

    if not all([name, email, subject, message]):
        flash('Please fill all required fields.', 'error')
        return redirect(url_for('home') + '#contact')

    html_body = f"""
    <html>
    <body style="font-family:Arial,sans-serif;background:#f5f7fa;padding:30px;">
      <div style="max-width:580px;margin:0 auto;background:#fff;border-radius:12px;
                  box-shadow:0 4px 20px rgba(0,0,0,0.08);overflow:hidden;">

        <div style="background:#00a86b;padding:28px 32px;">
          <h2 style="color:#fff;margin:0;font-size:20px;">New Project Inquiry</h2>
          <p style="color:rgba(255,255,255,0.8);margin:6px 0 0;font-size:13px;">
            Portfolio Contact Form &mdash; {timestamp}
          </p>
        </div>

        <div style="padding:32px;">
          <table style="width:100%;border-collapse:collapse;font-size:14px;">
            <tr>
              <td style="padding:10px 0;color:#6b7280;width:140px;font-weight:600;">Name</td>
              <td style="padding:10px 0;color:#111827;font-weight:500;">{name}</td>
            </tr>
            <tr style="background:#f9fafb;">
              <td style="padding:10px 8px;color:#6b7280;font-weight:600;">Email</td>
              <td style="padding:10px 8px;">
                <a href="mailto:{email}" style="color:#00a86b;">{email}</a>
              </td>
            </tr>
            <tr>
              <td style="padding:10px 0;color:#6b7280;font-weight:600;">Subject</td>
              <td style="padding:10px 0;color:#111827;font-weight:500;">{subject}</td>
            </tr>
            <tr style="background:#f9fafb;">
              <td style="padding:10px 8px;color:#6b7280;font-weight:600;">Project Name</td>
              <td style="padding:10px 8px;color:#111827;">{project_name}</td>
            </tr>
            <tr>
              <td style="padding:10px 0;color:#6b7280;font-weight:600;">Budget</td>
              <td style="padding:10px 0;">
                <span style="background:#e6f9f0;color:#007a4e;padding:3px 10px;
                             border-radius:20px;font-size:13px;font-weight:600;">
                  {budget}
                </span>
              </td>
            </tr>
          </table>

          <div style="margin-top:24px;background:#f5f7fa;border-left:4px solid #00a86b;
                      padding:18px 20px;">
            <p style="margin:0 0 8px;font-weight:600;color:#111827;font-size:13px;">
              Message / Project Details
            </p>
            <p style="margin:0;color:#374151;font-size:14px;line-height:1.8;
                      white-space:pre-wrap;">{message}</p>
          </div>

          <div style="margin-top:28px;text-align:center;">
            <a href="mailto:{email}?subject=Re: {subject}"
               style="display:inline-block;background:#00a86b;color:#fff;
                      padding:13px 32px;border-radius:50px;font-size:14px;
                      font-weight:600;text-decoration:none;">
              Reply to {name} &rarr;
            </a>
          </div>
        </div>

        <div style="background:#f9fafb;padding:16px 32px;text-align:center;
                    border-top:1px solid #e5e7eb;">
          <p style="margin:0;color:#9ca3af;font-size:12px;">
            Sent via Zaki Ul Husnain's Portfolio Website
          </p>
        </div>

      </div>
    </body>
    </html>
    """

    try:
        msg = MIMEMultipart('alternative')
        msg['From']    = SENDER_EMAIL
        msg['To']      = RECEIVER_EMAIL
        msg['Subject'] = f"[Portfolio] {subject} — {name}"
        msg.attach(MIMEText(html_body, 'html'))

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())

        flash('success', 'success')

    except Exception as e:
        print(f"Email error: {e}")
        flash('error', 'error')

    return redirect(url_for('home') + '#contact')


if __name__ == '__main__':
    app.run(debug=True)