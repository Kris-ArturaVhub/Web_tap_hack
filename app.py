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
    
    return '''
    <script src="https://www.google.com/recaptcha/api.js" async defer></script>
    <div style="text-align: center; padding: 50px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f4f9; height: 100vh;">
        <div style="background: white; padding: 30px; border-radius: 15px; display: inline-block; box-shadow: 0 10px 25px rgba(0,0,0,0.1);">
            <h2 style="color: #333; margin-bottom: 20px;">KAVNHUB SECURITY</h2>
            
            <div class="g-recaptcha" data-sitekey="6LeA3JksAAAAAKEYSY3MDVtN6YJkdN_-JJiSwNtU"></div>
            
            <form action="/verify" method="post">
                <input type="password" name="user_key" placeholder="Nhập mật mã truy cập..." 
                       style="padding: 12px; width: 250px; border-radius: 8px; border: 2px solid #ddd; margin-bottom: 20px; outline: none;">
                
                <br>

                <div style="background: #fafafa; border: 1px solid #d3d3d3; padding: 15px; border-radius: 5px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                    <input type="checkbox" id="captcha_check" style="width: 20px; height: 20px; cursor: pointer;" 
                           onchange="document.getElementById('submit_btn').disabled = !this.checked;">
                    <label for="captcha_check" style="margin-left: 10px; font-size: 14px; color: #555; cursor: pointer;">
                        Tôi xác nhận không phải là người máy
                    </label>
                </div>

                <button type="submit" id="submit_btn" disabled 
                        style="padding: 12px 30px; background: #007bff; color: white; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; opacity: 0.5;">
                    XÁC NHẬN VÀO HỆ THỐNG
                </button>
            </form>
            
            <p style="font-size: 12px; color: #aaa; margin-top: 20px;">© 2026 Kris Artura VNHub Portal</p>
        </div>
    </div>

    <script>
        // Hiệu ứng làm sáng nút khi tick vào ô
        const checkbox = document.getElementById('captcha_check');
        const btn = document.getElementById('submit_btn');
        checkbox.addEventListener('change', function() {
            if (this.checked) {
                btn.style.opacity = "1";
                btn.style.backgroundColor = "#28a745"; // Đổi sang màu xanh lá cho ngầu
            } else {
                btn.style.opacity = "0.5";
                btn.style.backgroundColor = "#007bff";
            }
        });
    </script>
    '''
    

@app.route('/verify', methods=['POST'])
def verify():
    import requests
    import flask
    
    # 1. Lấy Pass và kết quả ô tích từ người dùng
    user_pass = flask.request.form.get('user_key')
    captcha_res = flask.request.form.get('g-recaptcha-response')

    # 2. Check mật mã trước
    if user_pass != "ArturaVhub":
        return 'Sai mã rồi! <a href="/">Quay lại</a>'

    # 3. Check ô tích với Google (Thay Secret Key của anh vào đây)
    v = requests.post('https://www.google.com/recaptcha/api/siteverify', data={
        'secret': 'DÁN_SECRET_KEY_CỦA_ANH_VÀO_ĐÂY',
        'response': captcha_res
    }).json()

    if v.get('success'):
        flask.session['logged_in'] = True
        return flask.redirect('/home')
    else:
        return 'Lỗi Captcha hoặc bạn chưa tích ô! <a href="/">Thử lại</a>'
    

# --- LINK 2 (TRANG HOME PRO) ---
@app.route('/home')
def home():
    import flask
    if not flask.session.get('is_logged_in'):
        return flask.redirect('/')
        
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

    


    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    
