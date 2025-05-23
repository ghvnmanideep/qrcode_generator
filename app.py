from flask import Flask, render_template, request, send_file
import qrcode
import time
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('qr.html', msg="", img_path=None, time=time)

@app.route('/qrcode', methods=['POST'])
def generate_qrcode():
    msg = ""
    img_path = None
    if request.method == 'POST':
        data = request.form.get('data')
        if data:
            qr = qrcode.QRCode(version=5, box_size=5, border=3)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="red", back_color="white")
            img_path = "static/qr.png"
            img.save(img_path)
            msg = "QR Code successfully generated"
        else:
            msg = "Please provide data to generate QR Code."
    return render_template('qr.html', msg=msg, img_path="static/qr.png", time=time)

@app.route('/download')
def download_qrcode():
    return send_file("static/qr.png", as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)


# import random, string
# random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(12))
