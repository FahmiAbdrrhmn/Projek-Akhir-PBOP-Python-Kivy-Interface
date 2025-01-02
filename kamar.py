import psycopg2
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from eksporexcel import export_kamar_to_excel  # Import fungsi ekspor dari eksporexcel.py



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


class KamarApp(App):
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
        self.input_label_id = Label(text="ID Kamar", size_hint=(0.3, 1))
        self.input_text_id = TextInput(size_hint=(0.7, 1), hint_text="auto jika tambah")

        self.input_label_type = Label(text="Tipe Kamar", size_hint=(0.3, 1))
        self.input_text_type = TextInput(size_hint=(0.7, 1))

        self.input_label_price = Label(text="Harga Per Malam", size_hint=(0.4, 1))
        self.input_text_price = TextInput(size_hint=(0.7, 1))

        self.input_label_status = Label(text="Status", size_hint=(0.3, 1))
        self.input_text_status = TextInput(size_hint=(0.7, 1))

        self.input_layout.add_widget(self.input_label_id)
        self.input_layout.add_widget(self.input_text_id)
        self.input_layout.add_widget(self.input_label_type)
        self.input_layout.add_widget(self.input_text_type)
        self.input_layout.add_widget(self.input_label_price)
        self.input_layout.add_widget(self.input_text_price)
        self.input_layout.add_widget(self.input_label_status)
        self.input_layout.add_widget(self.input_text_status)

        # Tombol CRUD
        self.add_button = Button(text="Tambah Kamar", on_press=self.add_kamar)
        self.update_button = Button(text="Perbarui Kamar", on_press=self.update_kamar)
        self.delete_button = Button(text="Hapus Kamar", on_press=self.delete_kamar)

        self.layout.add_widget(self.input_layout)
        self.layout.add_widget(self.add_button)
        self.layout.add_widget(self.update_button)
        self.layout.add_widget(self.delete_button)

        # Menampilkan daftar data kamar
        self.data_layout = GridLayout(cols=1, size_hint_y=None)
        self.data_layout.bind(minimum_height=self.data_layout.setter('height'))

        self.scroll_view = ScrollView()
        self.scroll_view.add_widget(self.data_layout)
        self.layout.add_widget(self.scroll_view)

        self.load_data()

        return self.layout

    def load_data(self):
        try:
            self.cursor.execute("SELECT * FROM kamar")
            rows = self.cursor.fetchall()
            self.data_layout.clear_widgets()

            for row in rows:
                item = Button(text=f"ID: {row[0]} - Tipe: {row[1]} - Harga: {row[2]} - Status: {row[3]}")
                self.data_layout.add_widget(item)
        except Exception as e:
            print(f"Error loading data: {e}")

    def add_kamar(self, instance):
        tipe = self.input_text_type.text
        harga = self.input_text_price.text
        status = self.input_text_status.text
        if tipe and harga and status:
            try:
                # Menambahkan kamar dengan tipe, harga, dan status
                self.cursor.execute("INSERT INTO kamar (tipe_kamar, harga_per_malam, status) VALUES (%s, %s, %s)",
                                    (tipe, harga, status))
                self.conn.commit()
                self.load_data()
                self.input_text_type.text = ''
                self.input_text_price.text = ''
                self.input_text_status.text = ''
            except Exception as e:
                print(f"Error adding kamar: {e}")
        else:
            print("Tipe Kamar, Harga Per Malam, dan Status tidak boleh kosong")

    def update_kamar(self, instance):
        id_kamar = self.input_text_id.text
        tipe = self.input_text_type.text
        harga = self.input_text_price.text
        status = self.input_text_status.text

        if id_kamar and tipe and harga and status:
            try:
                # Memperbarui tipe_kamar, harga_per_malam, dan status berdasarkan id_kamar
                self.cursor.execute("UPDATE kamar SET tipe_kamar = %s, harga_per_malam = %s, status = %s WHERE id_kamar = %s",
                                    (tipe, harga, status, id_kamar))
                self.conn.commit()
                self.load_data()
                self.input_text_id.text = ''
                self.input_text_type.text = ''
                self.input_text_price.text = ''
                self.input_text_status.text = ''
            except Exception as e:
                print(f"Error updating kamar: {e}")
        else:
            print("ID Kamar, Tipe Kamar, Harga Per Malam, dan Status tidak boleh kosong")

    def delete_kamar(self, instance):
        id_kamar = self.input_text_id.text
        if id_kamar:
            try:
                self.cursor.execute("DELETE FROM kamar WHERE id_kamar = %s", (id_kamar,))
                self.conn.commit()
                self.load_data()
                self.input_text_id.text = ''
                self.input_text_type.text = ''
                self.input_text_price.text = ''
                self.input_text_status.text = ''
            except Exception as e:
                print(f"Error deleting kamar: {e}")
        else:
            print("ID Kamar tidak boleh kosong")
            
    def back_to_main(self, instance):
        from main import MainApp  # Import MainApp di dalam fungsi untuk menghindari circular import
        self.stop()  # Menutup aplikasi Kelola Kamar
        MainApp().run()  # Kembali ke aplikasi utama
        
    def export_to_excel(self, instance):
        export_kamar_to_excel()  # Panggil fungsi ekspor dari eksporexcel.py
        

if __name__ == "__main__":
    KamarApp().run()
