from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from datetime import datetime
from dotenv import load_dotenv
import psycopg

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


def generate_pdf_report():
    os.makedirs("reports", exist_ok=True)

    conn = psycopg.connect(DATABASE_URL)
    cursor = conn.cursor()

    cursor.execute("SELECT id, title, done FROM tasks")
    tasks = cursor.fetchall()

    filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    filepath = os.path.join("reports", filename)

    c = canvas.Canvas(filepath, pagesize=letter)

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, 750, "Task Report")

    c.setFont("Helvetica", 12)
    c.drawString(50, 725, f"Generated: {datetime.now()}")

    y = 690

    for task in tasks:
        status = "Done" if task[2] else "Pending"
        c.drawString(
            50,
            y,
            f"{task[0]}. {task[1]} - {status}"
        )
        y -= 20

    c.save()

    cursor.close()
    conn.close()

    return filename