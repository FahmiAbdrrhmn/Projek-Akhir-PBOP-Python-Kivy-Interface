import psycopg2
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from eksporexcel import export_reservasi_to_excel  # Import fungsi ekspor dari eksporexcel.py


# Koneksi ke database PostgreSQL
def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="reservasihotelfahmi", user="postgres", password="1qaz2wsx", host="localhost", port="5432"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None


class ReservasiApp(App):
    def build(self):
        self.conn = connect_db()
        if not self.conn:
            print("Database connection failed.")
            return

        self.cursor = self.conn.cursor()

        self.layout = BoxLayout(orientation='vertical')
        
        # Tombol kembali ke menu utama
        self.back_button = Button(text="Kembali ke Menu Utama", size_hint=(1, 0.1), on_press=self.back_to_main)
        self.layout.add_widget(self.back_button)
        
        # Tombol untuk ekspor ke Excel
        self.export_button = Button(text="Ekspor ke Excel", size_hint=(1, 0.1), on_press=self.export_to_excel)
        self.layout.add_widget(self.export_button)


        # Input form untuk operasi CRUD
        self.input_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=50)
        self.input_label_id = Label(text="ID Reservasi", size_hint=(0.3, 1))
        self.input_text_id = TextInput(size_hint=(0.7, 1), hint_text="auto jika tambah")

        self.input_label_tamu = Label(text="ID Tamu", size_hint=(0.3, 1))
        self.input_text_tamu = TextInput(size_hint=(0.7, 1))

        self.input_label_kamar = Label(text="ID Kamar", size_hint=(0.3, 1))
        self.input_text_kamar = TextInput(size_hint=(0.7, 1))

        self.input_label_check_in = Label(text="Check-in", size_hint=(0.3, 1))
        self.input_text_check_in = TextInput(size_hint=(0.7, 1))

        self.input_label_check_out = Label(text="Check-out", size_hint=(0.3, 1))
        self.input_text_check_out = TextInput(size_hint=(0.7, 1))

        self.input_label_total = Label(text="Total Harga", size_hint=(0.3, 1))
        self.input_text_total = TextInput(size_hint=(0.7, 1))

        self.input_layout.add_widget(self.input_label_id)
        self.input_layout.add_widget(self.input_text_id)
        self.input_layout.add_widget(self.input_label_tamu)
        self.input_layout.add_widget(self.input_text_tamu)
        self.input_layout.add_widget(self.input_label_kamar)
        self.input_layout.add_widget(self.input_text_kamar)
        self.input_layout.add_widget(self.input_label_check_in)
        self.input_layout.add_widget(self.input_text_check_in)
        self.input_layout.add_widget(self.input_label_check_out)
        self.input_layout.add_widget(self.input_text_check_out)
        self.input_layout.add_widget(self.input_label_total)
        self.input_layout.add_widget(self.input_text_total)

        # Tombol CRUD
        self.add_button = Button(text="Tambah Reservasi", on_press=self.add_reservasi)
        self.update_button = Button(text="Perbarui Reservasi", on_press=self.update_reservasi)
        self.delete_button = Button(text="Hapus Reservasi", on_press=self.delete_reservasi)

        self.layout.add_widget(self.input_layout)
        self.layout.add_widget(self.add_button)
        self.layout.add_widget(self.update_button)
        self.layout.add_widget(self.delete_button)

        # Menampilkan daftar data reservasi
        self.data_layout = GridLayout(cols=1, size_hint_y=None)
        self.data_layout.bind(minimum_height=self.data_layout.setter('height'))

        self.scroll_view = ScrollView()
        self.scroll_view.add_widget(self.data_layout)
        self.layout.add_widget(self.scroll_view)

        self.load_data()

        return self.layout

    def load_data(self):
        try:
            self.cursor.execute("SELECT * FROM reservasi")
            rows = self.cursor.fetchall()
            self.data_layout.clear_widgets()

            for row in rows:
                item = Button(text=f"ID: {row[0]} - Tamu: {row[1]} - Kamar: {row[2]} - Check-in: {row[3]} - Check-out: {row[4]} - Total: {row[5]}")
                self.data_layout.add_widget(item)
        except Exception as e:
            print(f"Error loading data: {e}")

    def add_reservasi(self, instance):
        id_tamu = self.input_text_tamu.text
        id_kamar = self.input_text_kamar.text
        check_in = self.input_text_check_in.text
        check_out = self.input_text_check_out.text
        total = self.input_text_total.text

        if id_tamu and id_kamar and check_in and check_out and total:
            try:
                # Menambahkan reservasi
                self.cursor.execute("INSERT INTO reservasi (id_tamu, id_kamar, check_in, check_out, total_harga) VALUES (%s, %s, %s, %s, %s)",
                                    (id_tamu, id_kamar, check_in, check_out, total))
                self.conn.commit()
                self.load_data()
                self.input_text_tamu.text = ''
                self.input_text_kamar.text = ''
                self.input_text_check_in.text = ''
                self.input_text_check_out.text = ''
                self.input_text_total.text = ''
            except Exception as e:
                print(f"Error adding reservasi: {e}")
        else:
            print("Semua field harus diisi")

    def update_reservasi(self, instance):
        id_reservasi = self.input_text_id.text
        id_tamu = self.input_text_tamu.text
        id_kamar = self.input_text_kamar.text
        check_in = self.input_text_check_in.text
        check_out = self.input_text_check_out.text
        total = self.input_text_total.text

        if id_reservasi and id_tamu and id_kamar and check_in and check_out and total:
            try:
                # Memperbarui reservasi
                self.cursor.execute("UPDATE reservasi SET id_tamu = %s, id_kamar = %s, check_in = %s, check_out = %s, total_harga = %s WHERE id_reservasi = %s",
                                    (id_tamu, id_kamar, check_in, check_out, total, id_reservasi))
                self.conn.commit()
                self.load_data()
                self.input_text_id.text = ''
                self.input_text_tamu.text = ''
                self.input_text_kamar.text = ''
                self.input_text_check_in.text = ''
                self.input_text_check_out.text = ''
                self.input_text_total.text = ''
            except Exception as e:
                print(f"Error updating reservasi: {e}")
        else:
            print("ID Reservasi, Tamu, Kamar, Check-in, Check-out, dan Total Harga tidak boleh kosong")

    def delete_reservasi(self, instance):
        id_reservasi = self.input_text_id.text
        if id_reservasi:
            try:
                self.cursor.execute("DELETE FROM reservasi WHERE id_reservasi = %s", (id_reservasi,))
                self.conn.commit()
                self.load_data()
                self.input_text_id.text = ''
                self.input_text_tamu.text = ''
                self.input_text_kamar.text = ''
                self.input_text_check_in.text = ''
                self.input_text_check_out.text = ''
                self.input_text_total.text = ''
            except Exception as e:
                print(f"Error deleting reservasi: {e}")
        else:
            print("ID Reservasi tidak boleh kosong")
            
    def back_to_main(self, instance):
        from main import MainApp  # Import MainApp di dalam fungsi untuk menghindari circular import
        self.stop()  # Menutup aplikasi Kelola Reservasi
        MainApp().run()  # Kembali ke aplikasi utama
        
    def export_to_excel(self, instance):
        export_reservasi_to_excel()  # Panggil fungsi ekspor dari eksporexcel.py


if __name__ == "__main__":
    ReservasiApp().run()
