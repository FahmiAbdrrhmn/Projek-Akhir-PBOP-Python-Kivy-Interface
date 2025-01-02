import psycopg2
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from eksporexcel import export_tamu_to_excel


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


class TamuApp(App):  
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
        self.input_label_id = Label(text="ID Tamu", size_hint=(0.3, 1))
        self.input_text_id = TextInput(size_hint=(0.7, 1), hint_text="auto jika tambah")
        self.input_label_name = Label(text="Nama Tamu", size_hint=(0.3, 1))
        self.input_text_name = TextInput(size_hint=(0.7, 1))

        self.input_label_contact = Label(text="Kontak Tamu", size_hint=(0.3, 1))
        self.input_text_contact = TextInput(size_hint=(0.7, 1))

        self.input_layout.add_widget(self.input_label_id)
        self.input_layout.add_widget(self.input_text_id)
        self.input_layout.add_widget(self.input_label_name)
        self.input_layout.add_widget(self.input_text_name)
        self.input_layout.add_widget(self.input_label_contact)
        self.input_layout.add_widget(self.input_text_contact)

        # Tombol CRUD
        self.add_button = Button(text="Tambah Tamu", on_press=self.add_tamu)
        self.update_button = Button(text="Perbarui Tamu", on_press=self.update_tamu)
        self.delete_button = Button(text="Hapus Tamu", on_press=self.delete_tamu)

        self.layout.add_widget(self.input_layout)
        self.layout.add_widget(self.add_button)
        self.layout.add_widget(self.update_button)
        self.layout.add_widget(self.delete_button)

        # Menampilkan daftar data
        self.data_layout = GridLayout(cols=1, size_hint_y=None)
        self.data_layout.bind(minimum_height=self.data_layout.setter('height'))

        self.scroll_view = ScrollView()
        self.scroll_view.add_widget(self.data_layout)
        self.layout.add_widget(self.scroll_view)

        self.load_data()

        return self.layout

    def load_data(self):
        try:
            self.cursor.execute("SELECT * FROM tamu")
            rows = self.cursor.fetchall()
            self.data_layout.clear_widgets()

            for row in rows:
                item = Button(text=f"ID: {row[0]} - Nama: {row[1]} - Kontak: {row[2]}")
                self.data_layout.add_widget(item)
        except Exception as e:
            print(f"Error loading data: {e}")

    def add_tamu(self, instance):
        name = self.input_text_name.text
        contact = self.input_text_contact.text
        if name and contact:
            try:
                # Menambahkan tamu dengan nama dan kontak
                self.cursor.execute("INSERT INTO tamu (nama_tamu, kontak) VALUES (%s, %s)", (name, contact))
                self.conn.commit()
                self.load_data()
                self.input_text_name.text = ''
                self.input_text_contact.text = ''
            except Exception as e:
                print(f"Error adding tamu: {e}")
        else:
            print("Nama Tamu dan Kontak tidak boleh kosong")

    def update_tamu(self, instance):
        id_tamu = self.input_text_id.text
        name = self.input_text_name.text
        contact = self.input_text_contact.text

        if id_tamu and name and contact:
            try:
                # Memperbarui nama_tamu dan kontak berdasarkan id_tamu
                self.cursor.execute("UPDATE tamu SET nama_tamu = %s, kontak = %s WHERE id_tamu = %s", 
                                    (name, contact, id_tamu))
                self.conn.commit()
                self.load_data()
                self.input_text_id.text = ''
                self.input_text_name.text = ''
                self.input_text_contact.text = ''
            except Exception as e:
                print(f"Error updating tamu: {e}")
        else:
            print("ID Tamu, Nama Tamu, dan Kontak tidak boleh kosong")

    def delete_tamu(self, instance):
        name = self.input_text_name.text
        if name:
            try:
                self.cursor.execute("DELETE FROM tamu WHERE nama_tamu = %s", (name,))
                self.conn.commit()
                self.load_data()
                self.input_text_name.text = ''
                self.input_text_contact.text = ''
            except Exception as e:
                print(f"Error deleting tamu: {e}")
        else:
            print("Nama Tamu tidak boleh kosong")
            
    def back_to_main(self, instance):
        from main import MainApp  # Import MainApp di dalam fungsi untuk menghindari circular import
        self.stop()  # Menutup aplikasi Kelola Tamu
        MainApp().run()  # Kembali ke aplikasi utama
        
    def export_to_excel(self, instance):
        export_tamu_to_excel()  # Panggil fungsi ekspor dari eksporexcel.py

if __name__ == "__main__":
    TamuApp().run()
