from flask import Flask, request, Response
from qrcode import QRCode, constants
from io import BytesIO
app = Flask(__name__)

@app.route('/qr', methods=['GET'])
def qr_code():
    url = request.args.get('url')
    if not url:
        return 'Please provide a valid URL'
    qr = QRCode(
        version=1,
        error_correction=constants.ERROR_CORRECT_L,
        box_size=10,
        border=5,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    bio = BytesIO()
    img.save(bio, format="PNG")
    bio.seek(0)
    response = Response(bio.read(), content_type="image/png")
    response.headers["Content-Disposition"] = "attachment; filename=qr.png"
    return response

    #return send_file(bio, attachment_filename='qr.png', as_attachment=True)
    #return Response(bio.read(), content_type="image/png")

if __name__ =='__main__' :
    app.run()