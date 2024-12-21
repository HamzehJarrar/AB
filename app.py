from flask import Flask, render_template, request, session, redirect, url_for, make_response
import qrcode
import os
import json
import pandas as pd
from fpdf import FPDF
from datetime import datetime, timedelta


app = Flask(__name__)
app.secret_key = 'your_secret_key'

qr_directory = os.path.join(app.static_folder, 'qr_codes')

if not os.path.exists(qr_directory):
    os.makedirs(qr_directory)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    subject = request.form['subject']
    section = request.form['section']
    
    if subject and section:
        session['subject'] = subject
        session['section'] = section

        student_url = url_for('student', subject=subject, section=section, _external=True)

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(student_url)
        qr.make(fit=True)

        qr_image_path = f"qr_codes/{subject}_{section}.png"
        img = qr.make_image(fill='black', back_color='white')
        img.save(os.path.join(qr_directory, f"{subject}_{section}.png"))

        return render_template('index.html', qr_image_path=qr_image_path, show_download=False)

    return "Please provide both subject and section!"

@app.route('/stop', methods=['POST'])
def stop():
    return render_template('index.html', show_download=True)

@app.route('/download_excel')
def download_excel():
    students = session.get('students', [])
    if not students:
        return "No attendance data available to download."

    df = pd.DataFrame(students)

    subject = session.get('subject', 'Unknown_Subject')
    section = session.get('section', 'Unknown_Section')
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  
    excel_file_name = f"attendance_{subject}_{section}_{timestamp}.xlsx"
    excel_file_path = os.path.join(qr_directory, excel_file_name)

    df.to_excel(excel_file_path, index=False)

    session['students'] = []  

    return redirect(url_for('static', filename=f'qr_codes/{excel_file_name}'))

    students = session.get('students', [])
    if not students:
        return "No attendance data available to download."

    df = pd.DataFrame(students)

    subject = session.get('subject', 'Unknown_Subject')
    section = session.get('section', 'Unknown_Section')
    timestamp = datetime.now().strftime("%d-%m")  
    excel_file_name = f"attendance_{subject}_{section}_{timestamp}.xlsx"
    excel_file_path = os.path.join(qr_directory, excel_file_name)

    df.to_excel(excel_file_path, index=False)

    session['students'] = [] 

    return redirect(url_for('static', filename=f'qr_codes/{excel_file_name}'))

    students = session.get('students', [])
    if not students:
        return "No attendance data available to download."

    df = pd.DataFrame(students)

    subject = session.get('subject', 'Unknown_Subject')
    section = session.get('section', 'Unknown_Section')
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  
    excel_file_name = f"attendance_{subject}_{section}_{timestamp}.xlsx"
    excel_file_path = os.path.join(qr_directory, excel_file_name)

    df.to_excel(excel_file_path, index=False)

    return redirect(url_for('static', filename=f'qr_codes/{excel_file_name}'))

    students = session.get('students', [])
    if not students:
        return "No attendance data available to download."

    df = pd.DataFrame(students)

    subject = session.get('subject', 'Unknown_Subject')
    section = session.get('section', 'Unknown_Section')
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    excel_file_name = f"attendance_{subject}_{section}_{timestamp}.xlsx"
    excel_file_path = os.path.join(qr_directory, excel_file_name)

    df.to_excel(excel_file_path, index=False)

    return redirect(url_for('static', filename=f'qr_codes/{excel_file_name}'))

@app.route('/download_pdf')
def download_pdf():
    students = session.get('students', [])
    if not students:
        return "No attendance data available to download."

    pdf = FPDF()
    pdf.set_left_margin(10)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Attendance Report", ln=True, align="C")
    pdf.ln(10)

    for student in students:
        pdf.cell(200, 10, txt=f"Name: {student['name']}, ID: {student['id']}, Subject: {student['subject']}, Section: {student['section']}", ln=True)

    subject = session.get('subject', 'Unknown_Subject')
    section = session.get('section', 'Unknown_Section')
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  
    pdf_file_name = f"attendance_{subject}_{section}_{timestamp}.pdf"
    pdf_file_path = os.path.join(qr_directory, pdf_file_name)

    pdf.output(pdf_file_path)

    session['students'] = []  

    return redirect(url_for('static', filename=f'qr_codes/{pdf_file_name}'))

    students = session.get('students', [])
    if not students:
        return "No attendance data available to download."

    pdf = FPDF()
    pdf.set_left_margin(10)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Attendance Report", ln=True, align="C")
    pdf.ln(10)

    for student in students:
        pdf.cell(200, 10, txt=f"Name: {student['name']}, ID: {student['id']}, Subject: {student['subject']}, Section: {student['section']}", ln=True)

    subject = session.get('subject', 'Unknown_Subject')
    section = session.get('section', 'Unknown_Section')
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    pdf_file_name = f"attendance_{subject}_{section}_{timestamp}.pdf"
    pdf_file_path = os.path.join(qr_directory, pdf_file_name)

    pdf.output(pdf_file_path)

    return redirect(url_for('static', filename=f'qr_codes/{pdf_file_name}'))
    students = session.get('students', [])

    pdf = FPDF()
    pdf.set_left_margin(10)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Attendance Report", ln=True, align="C")
    pdf.ln(10)

    for student in students:
        pdf.cell(200, 10, txt=f"Name: {student['name']}, ID: {student['id']}, Subject: {student['subject']}, Section: {student['section']}", ln=True)

    pdf_file_path = os.path.join(qr_directory, 'attendance.pdf')
    pdf.output(pdf_file_path)

    return redirect(url_for('static', filename=f'qr_codes/attendance.pdf'))

@app.route('/student/<subject>/<section>', methods=['GET'])
def student(subject, section):
    return render_template('student.html', subject=subject, section=section)

@app.route('/submit_attendance', methods=['POST'])
def submit_attendance():
    student_name = request.form['student_name']
    student_id = request.form['student_id']
    subject = request.form['subject']
    section = request.form['section']

    last_attendance_time = request.cookies.get(f'attendance_{student_id}')
    
    now = datetime.now()

    if last_attendance_time:
        last_attendance_time = datetime.strptime(last_attendance_time, "%Y-%m-%d %H:%M:%S")
        if now - last_attendance_time < timedelta(minutes=30):
            return "You have already submitted attendance recently. Please wait"

    students = session.get('students', [])
    students.append({'name': student_name, 'id': student_id, 'subject': subject, 'section': section})
    session['students'] = students

    response = make_response("Attendance Submitted Successfully!")
    response.set_cookie(f'attendance_{student_id}', now.strftime("%Y-%m-%d %H:%M:%S"), max_age=900)  # الكوكيز صالح لمدة 15 دقيقة بس

    return response



if __name__ == '__main__':
    app.run(debug=True)
