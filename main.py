# Impor
from flask import Flask, render_template,request, redirect
# Mengimpor pustaka database
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Menghubungkan SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Membuat sebuah DB
db = SQLAlchemy(app )

#Tugas #1. Membuat tabel DB

class Card(db.Model):
    # Membuat kolom
    # id
    id = db.Column(db.Integer, primary_key=True)
    # Judul
    title = db.Column(db.String(100), nullable=False)
    # Deskripsi
    subtitle = db.Column(db.String(300), nullable=False)
    # Teks
    text = db.Column(db.Text, nullable=False)

    # Menghasilkan objek dan id-nya
    def _repr_(self):
        return f'<Card {self.id}>'

# Menjalankan halaman dengan konten
@app.route('/')
def index():
    # Menampilkan objek DB
    # Tugas #2. Menampilkan objek-objek dari DB di index.html
    

    return render_template('index.html',
                           #cards = kartu

                           )

# Menjalankan halaman dengan kartu
@app.route('/card/<int:id>')
def card(id):
    # Tugas #2. Menampilkan kartu yang tepat berdasarkan id-nya
    

    return render_template('card.html', card=card)

# Menjalankan halaman dan membuat kartu
@app.route('/create')
def create():
    return render_template('create_card.html')

# Formulir kartu
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']

        # Tugas #2. Buatlah cara untuk menyimpan data dalam DB
        card = Card(title=title, subtitle=subtitle, text=text)
        db.session.add(card)
        db.session.commit()

        return redirect('/')
    else:
        return render_template('create_card.html')


if __name__ == "__main__":
    app.run(debug=True)
