from flask import Flask, render_template, request, redirect, url_for
from database import initialize_db, get_visits, save_visit, check_out
from pathlib import Path
import socket
import qrcode


app = Flask(__name__)
initialize_db()


@app.get('/')
def index():
    return render_template('index.html', message=None)


@app.post('/registrer')
def register():
    name = request.form.get('name', '').strip()
    purpose = request.form.get('purpose', '').strip()
    
    if not name or not purpose:
        return render_template('index.html', message='Fyll ut begge feltene.'), 400
    
    if save_visit(name, purpose):
        return render_template('index.html', message='Besøket er registrert.')
    else:
        return render_template('index.html', message='Feil under registrering.')


@app.get('/admin')
def admin():
    visits = get_visits()
    return render_template('admin.html', visits=visits)


@app.post('/utsjekk/<int:visit_id>')
def check_out_visit(visit_id):
    check_out(visit_id)
    return redirect(url_for('admin'))


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't need to be reachable; no packets are sent
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip


def generate_qr_code(port: int):
    local_ip = get_local_ip()
    
    image = qrcode.make(f"http://{local_ip}:{port}")
    
    image_path = Path(__file__).with_name('website-qrcode.png')
    with image_path.open('wb') as image_file:
        image.save(image_file)


if __name__ == '__main__':
    port = 5000
    
    generate_qr_code(port)
    
    app.run(debug=True, host='0.0.0.0', port=port)
    
