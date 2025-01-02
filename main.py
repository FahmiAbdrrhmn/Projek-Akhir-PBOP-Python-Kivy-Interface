from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label  # Impor Label
from kamar import KamarApp
from tamu import TamuApp
from reservasi import ReservasiApp

class MainApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # Label header
        self.header = Label(text="Menu Utama", size_hint=(1, 0.1))
        self.layout.add_widget(self.header)

        # Tombol-tombol menu utama
        self.kelola_kamar_button = Button(text="Kelola Kamar", size_hint=(1, 0.3), on_press=self.open_kamar)
        self.kelola_tamu_button = Button(text="Kelola Tamu", size_hint=(1, 0.3), on_press=self.open_tamu)
        self.kelola_reservasi_button = Button(text="Kelola Reservasi", size_hint=(1, 0.3), on_press=self.open_reservasi)

        self.layout.add_widget(self.kelola_kamar_button)
        self.layout.add_widget(self.kelola_tamu_button)
        self.layout.add_widget(self.kelola_reservasi_button)

        return self.layout

    def open_kamar(self, instance):
        self.stop()  # Menutup aplikasi utama
        KamarApp().run()  # Membuka aplikasi Kelola Kamar

    def open_tamu(self, instance):
        self.stop()  # Menutup aplikasi utama
        TamuApp().run()  # Membuka aplikasi Kelola Tamu

    def open_reservasi(self, instance):
        self.stop()  # Menutup aplikasi utama
        ReservasiApp().run()  # Membuka aplikasi Kelola Reservasi

if __name__ == "__main__":
    MainApp().run()
