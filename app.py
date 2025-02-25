from flask import Flask, render_template, request, send_file
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create uploads folder if it doesn't exist

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Extract data from the form
        nom = request.form['nom']
        prenom = request.form['prenom']
        date_naissance = request.form['date_naissance']
        lieu_naissance = request.form['lieu_naissance']
        adresse = request.form['adresse']
        nationalite = request.form['nationalite']
        situation_familiale = request.form['situation_familiale']
        email = request.form['email']
        tel = request.form['tel']
        stage = request.form['stage']
        travail = request.form['travail']
        licence = request.form['licence']
        diplome = request.form['diplome']
        bac = request.form['bac']
        arabe = request.form['arabe']
        francais = request.form['francais']
        anglais = request.form['anglais']
        sport = request.form['sport']
        lecture = request.form['lecture']
        caracteristiques = request.form['caracteristiques']

        # Handle photo upload
        if 'photo' in request.files:
            photo = request.files['photo']
            if photo.filename != '':
                photo_path = os.path.join(app.config['UPLOAD_FOLDER'], photo.filename)
                photo.save(photo_path)
            else:
                photo_path = None
        else:
            photo_path = None

        # Generate PDF
        pdf_path = generate_pdf(nom, prenom, date_naissance, lieu_naissance, adresse, nationalite, situation_familiale, email, tel, stage, travail, licence, diplome, bac, arabe, francais, anglais, sport, lecture, caracteristiques, photo_path)

        return send_file(pdf_path, as_attachment=True)

    return render_template('index.html')

def generate_pdf(nom, prenom, date_naissance, lieu_naissance, adresse, nationalite, situation_familiale, email, tel, stage, travail, licence, diplome, bac, arabe, francais, anglais, sport, lecture, caracteristiques, photo_path):
    pdf_path = 'cv.pdf'
    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.drawString(100, 750, "Curriculum Vitae")

    y = 700
    if photo_path:
        c.drawImage(photo_path, 500, y, width=100, height=100)
    c.drawString(100, y, f"Nom: {nom}")
    y -= 20
    c.drawString(100, y, f"Prénom: {prenom}")
    y -= 20
    c.drawString(100, y, f"Date de naissance: {date_naissance}")
    y -= 20
    c.drawString(100, y, f"Lieu de naissance: {lieu_naissance}")
    y -= 20
    c.drawString(100, y, f"Adresse: {adresse}")
    y -= 20
    c.drawString(100, y, f"Nationalité: {nationalite}")
    y -= 20
    c.drawString(100, y, f"Situation familiale: {situation_familiale}")
    y -= 20
    c.drawString(100, y, f"E-mail: {email}")
    y -= 20
    c.drawString(100, y, f"Tel: {tel}")
    y -= 40

    c.drawString(100, y, "Experiences Professionnelles:")
    y -= 20
    c.drawString(120, y, f"Stage au sein de: {stage}")
    y -= 20
    c.drawString(120, y, f"Travail au sein de: {travail}")
    y -= 40

    c.drawString(100, y, "Formations et Diplômes Obtenus:")
    y -= 20
    c.drawString(120, y, f"Licence en (20../20..): {licence}")
    y -= 20
    c.drawString(120, y, f"Diplôme de (20../20..): {diplome}")
    y -= 20
    c.drawString(120, y, f"Baccalauréat en... (2024/2025): {bac}")
    y -= 40

    c.drawString(100, y, "Langues:")
    y -= 20
    c.drawString(120, y, f"Arabe: {arabe}")
    y -= 20
    c.drawString(120, y, f"Français: {francais}")
    y -= 20
    c.drawString(120, y, f"Anglais: {anglais}")
    y -= 40

    c.drawString(100, y, "Activités Extra Professionnelles:")
    y -= 20
    c.drawString(120, y, f"Sport: {sport}")
    y -= 20
    c.drawString(120, y, f"Lecture: {lecture}")
    y -= 40

    c.drawString(100, y, "Caractéristiques Personnelles:")
    y -= 20
    c.drawString(120, y, caracteristiques)

    c.save()
    return pdf_path

if __name__ == '__main__':
    app.run(debug=True)