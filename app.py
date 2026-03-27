from flask import Flask, render_template_string, redirect, url_for

app = Flask(__name__)
app.secret_key = 'kris_artura_2026' # Chìa khóa để mã hóa mã xác thực


# --- GIAO DIỆN TỔNG THỂ (CSS) ---
COMMON_STYLE = '''
<style>
    body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f6; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; }
    .card { background: white; padding: 2rem; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); text-align: center; width: 350px; }
    .btn { background-color: #28a745; color: white; padding: 12px 24px; text-decoration: none; border-radius: 8px; display: inline-block; margin-top: 20px; transition: 0.3s; border: none; cursor: pointer; font-size: 16px; }
    .btn:hover { background-color: #218838; transform: scale(1.05); }
    .btn-blue { background-color: #007bff; }
    .btn-blue:hover { background-color: #0069d9; }
</style>
'''

# --- LINK CHÍNH (TRANG CAPTCHA) ---
@app.route('/')
def captcha():
    # Trang này chỉ hiện ô nhập mã, không hiện ảnh/nhạc
    return '''
    <div style="text-align: center; padding: 50px; font-family: sans-serif;">
        <h2>HỆ THỐNG KAVNHUB</h2>
        <p>Vui lòng nhập mã truy cập:</p>
        <form action="/verify" method="post">
            <input type="text" name="user_key" placeholder="Nhập Key..." style="padding: 10px; border-radius: 5px;">
            <button type="submit" style="padding: 10px 20px; background: #007bff; color: white; border: none; border-radius: 5px;">Vào hệ thống</button>
        </form>
    </div>
    '''

@app.route('/verify', methods=['POST'])
def verify():
    import flask
    user_input = flask.request.form.get('user_key')
    if user_input == "ArturaVhub": # Đây là Key của anh
        flask.session['is_logged_in'] = True
        return flask.redirect('/home')
    else:
        return '<h3>Sai mã rồi! <a href="/">Quay lại</a></h3>'
        

# --- LINK 2 (TRANG HOME PRO) ---
@app.route('/home')
def home():
    return COMMON_STYLE + '''
    <style>
        /* Cho phép trang web có thể vuốt xuống */
        body { height: auto; padding: 20px 0; display: block; } 
        
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            overflow: hidden; /* Để ảnh không bị tràn góc bo */
            padding-bottom: 30px;
        }

        .header-img {
            width: 100%;
            height: 250px;
            object-fit: cover; /* Giúp ảnh không bị méo */
        }

        .content { padding: 30px; text-align: left; }

        .music-player {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 10px;
            margin: 20px 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .info-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-top: 20px;
        }

        .info-box {
            background: #eef2f7;
            padding: 15px;
            border-radius: 10px;
            border-left: 5px solid #007bff;
        }
    </style>

    <div class="container">
         <img src="/https://github.com/Kris-ArturaVhub/KAvnhub/raw/main/Screenshot_2026-anhnen.jpg" alt="..." style="width: 200px; border-radius: 10px;">

        <div class="content">
            <h1>🚀 KAvnhub_space </h1>
            <p style="color: #666;">Chào mừng bạn đến với không gian ảo. Đây là nơi tôi lưu trữ các links.</p>

            <div class="music-player">
                <p style="margin-right: 15px; font-weight: bold;">🎵 Đang phát:</p>
                <audio controls autoplay loop>
                    <source src="https://github.com/Kris-ArturaVhub/KAvnhub/raw/main/livingroomsong.mp3" type="audio/mpeg">
                    Trình duyệt của bạn không hỗ trợ phát nhạc.
                </audio>
            </div>

            <div class="info-grid">
                <div class="info-box">
                    <h3>👤 Profile</h3>
                    <p>Bí danh: Kris_Artura <br>Genz <br>Vị trí: Khánh Hòa, VN</p>
                </div>
                <div class="info-box" style="border-left-color: #28a745;">
                    <h3>💻 profile</h3>
                    <p>• Python / Flask<br>• SQL Injection (Basic)<br>• sdt:84+799.269_197</p>
                </div>
            </div>

            <div style="margin-top: 30px;">
                <h3>📜 Thông tư</h3>
                <p>Lưu ý: web được tạo bởi thực tập sinh IT cùng AI,đảm bảo an toàn tuyệt đối.</p>
            </div>

            <div style="text-align: center; margin-top: 40px;">
                
                <a href="/links" class="btn btn-blue" style="width: 200px;">Khám phá thêm ➔</a><br>
                <a href="https://www.facebook.com/share/1JKumr9zp1/" class="btn" style="background: #1DA1F2; width: 40%;">Facebook</a><br>
                <a href="https://www.tiktok.com/@ka.19920425?_r=1&_t=ZS-950s2mflaGA" class="btn" style="background: #ce1126; width: 40%;">Tiktok</a><br>
            </div>
        </div>
    </div>
    
    <p style="text-align: center; color: #aaa; margin-top: 20px;">© 2024 10110 Web Project</p>
    '''
    

# --- LINK 3 (DANH SÁCH LINK TỰ GẮN) ---
@app.route('/links')
def other_links():
    return COMMON_STYLE + '''
    <div class="card">
        <h2>🔗 Danh mục liên kết</h2>
        <p>Chọn nơi bạn muốn đến:</p>
        <a href="https://www.roblox.com" class="btn" style="background: #ce1126; width: 80%;">Vào Roblox</a><br>
        <a href="https://google.com" class="btn" style="background: #4285F4; width: 80%;">Tìm kiếm Google</a><br>
        <a href="/" class="btn" style="background: #6c757d; width: 80%;">Quay lại từ đầu</a>
        <a href="https://www.facebook.com/share/1JKumr9zp1/" class="btn" style="background: #1DA1F2; width: 80%;">Facebook</a><br>
    </div>
    '''
@app.route('/home')
def home():
    import flask
    # Kiểm tra nếu chưa nhập mã thì đuổi về trang chủ
    if not flask.session.get('is_logged_in'):
        return flask.redirect('/')

    # Nếu đã nhập mã đúng, hiện ảnh và nhạc
    return '''
    <div style="text-align: center; padding: 20px; font-family: sans-serif;">
        <h1 style="color: #28a745;">TRUY CẬP THÀNH CÔNG!</h1>
        
        <img src="https://github.com/Kris-ArturaVhub/KAvnhub/raw/main/Screenshot_2026-anhnen.jpg" 
             style="width: 100%; max-width: 400px; border-radius: 15px;">
        
        <br><br>
        <audio controls autoplay>
            <source src="https://github.com/Kris-ArturaVhub/KAvnhub/raw/main/livingroomsong.mp3" type="audio/mpeg">
        </audio>
        
        <br><br>
        <a href="/logout" style="color: red;">Đăng xuất</a>
    </div>
    '''

@app.route('/logout')
def logout():
    import flask
    flask.session.pop('is_logged_in', None)
    return flask.redirect('/')
    


    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    
