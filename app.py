from flask import Flask, render_template_string, redirect, url_for

app = Flask(__name__)

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
def index():
    return COMMON_STYLE + '''
    <div class="card">
        <h2>Xác minh bảo mật</h2>
        <p>Vui lòng xác nhận bạn không phải là Gay để tiếp tục.</p>
        <div style="border: 1px solid #ccc; padding: 15px; background: #fafafa; border-radius: 5px; display: flex; align-items: center; gap: 10px; margin: 20px 0;">
            <input type="checkbox" id="captcha" style="width: 25px; height: 25px; cursor: pointer;" onclick="setTimeout(() => { window.location.href='/home' }, 500)">
            <label for="captcha" style="cursor: pointer;">Tôi không phải là gay</label>
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/ad/RecaptchaLogo.svg" width="30" style="margin-left: auto;">
        </div>
    </div>
    '''

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
         <img src="/static/Screenshot_2026-01-16-20-24-51-00_a23b203fd3aafc6dcb84e438dda678b6.jpg" alt="..." style="width: 200px; border-radius: 10px;">

        <div class="content">
            <h1>🚀 KAvnhub_space </h1>
            <p style="color: #666;">Chào mừng bạn đến với không gian ảo. Đây là nơi tôi lưu trữ các links.</p>

            <div class="music-player">
                <p style="margin-right: 15px; font-weight: bold;">🎵 Đang phát:</p>
                <audio controls autoplay loop>
                    <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
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
                
                <a href="/links" class="btn btn-blue" style="width: 200px;">Khám phá thêm ➔</a>
                <a href="https://www.facebook.com/share/1JKumr9zp1/" class="btn" style="background: #1DA1F2; width: 80%;">Facebook</a><br>
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
    
