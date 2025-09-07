import os
from tkinter import Tk, Label, filedialog, Button, messagebox, StringVar, Scale, HORIZONTAL, Frame
from PIL import Image
from PyPDF2 import PdfReader, PdfWriter

class FileCompressor:
    def __init__(self):
        self.root = Tk()
        self.root.title("File Compressor - Press File")
        self.root.geometry("450x450")
        
        self.selected_file = StringVar()
        self.quality_recommendation = StringVar()
        self.setup_ui()
        
    def setup_ui(self):
        # Header
        Label(self.root, text="FILE COMPRESSOR", font=("Arial", 16, "bold")).pack(pady=10)
        
        # File selection
        Label(self.root, text="Pilih file untuk dikompres (Gambar: JPG/PNG, PDF)").pack(pady=5)
        Button(self.root, text="📁 Pilih File", command=self.select_file, 
               bg="#4CAF50", fg="white", width=20).pack(pady=5)
        
        # Selected file display
        self.file_label = Label(self.root, textvariable=self.selected_file, 
                               wraplength=400, fg="blue")
        self.file_label.pack(pady=5)
        
        # Quality control frame
        quality_frame = Frame(self.root)
        quality_frame.pack(pady=10)
        
        Label(quality_frame, text="Kualitas Kompres (10-100):").pack()
        self.quality_scale = Scale(quality_frame, from_=10, to=100, orient=HORIZONTAL, 
                                  length=250, resolution=1, command=self.update_quality_info)
        self.quality_scale.set(75)
        self.quality_scale.pack(pady=5)
        
        # Quality recommendation
        self.quality_label = Label(quality_frame, textvariable=self.quality_recommendation, 
                                  fg="darkgreen", font=("Arial", 9))
        self.quality_label.pack()
        
        # Resize option
        resize_frame = Frame(self.root)
        resize_frame.pack(pady=5)
        
        Label(resize_frame, text="Resize Gambar:").pack()
        resize_options_frame = Frame(resize_frame)
        resize_options_frame.pack()
        
        Button(resize_options_frame, text="Tanpa Resize", command=lambda: self.set_resize(None),
               bg="#607D8B", fg="white", width=12).pack(side="left", padx=2)
        Button(resize_options_frame, text="50% Ukuran", command=lambda: self.set_resize(0.5),
               bg="#795548", fg="white", width=12).pack(side="left", padx=2)
        Button(resize_options_frame, text="75% Ukuran", command=lambda: self.set_resize(0.75),
               bg="#FF5722", fg="white", width=12).pack(side="left", padx=2)
        
        # Quality presets
        preset_frame = Frame(self.root)
        preset_frame.pack(pady=5)
        
        Button(preset_frame, text="Kualitas Tinggi (85)", command=lambda: self.set_quality(85),
               bg="#2196F3", fg="white", width=15).pack(side="left", padx=2)
        Button(preset_frame, text="Seimbang (60)", command=lambda: self.set_quality(60),
               bg="#FF9800", fg="white", width=15).pack(side="left", padx=2)
        Button(preset_frame, text="Kompres Kuat (30)", command=lambda: self.set_quality(30),
               bg="#9C27B0", fg="white", width=15).pack(side="left", padx=2)
        
        # Compress button
        self.compress_btn = Button(self.root, text="🗜️ KOMPRES FILE", 
                                  command=self.compress_file, 
                                  bg="#4CAF50", fg="white", 
                                  font=("Arial", 12, "bold"),
                                  state="disabled", width=20)
        self.compress_btn.pack(pady=15)
        
        # Status label
        self.status_label = Label(self.root, text="Pilih file terlebih dahulu", 
                                 fg="gray")
        self.status_label.pack(pady=5)
        
        # Initialize
        self.resize_factor = None
        self.update_quality_info(75)

    def set_quality(self, value):
        """Set quality preset"""
        self.quality_scale.set(value)
        self.update_quality_info(value)

    def set_resize(self, factor):
        """Set resize factor"""
        self.resize_factor = factor
        if factor is None:
            resize_text = "Tanpa resize"
        else:
            resize_text = f"Resize ke {int(factor*100)}%"
        
        messagebox.showinfo("Resize", f"Mode resize: {resize_text}")

    def update_quality_info(self, value):
        """Update quality recommendation text"""
        quality = int(float(value))
        
        if quality >= 80:
            info = "Kualitas Tinggi - Kompresi ringan"
            color = "darkgreen"
        elif quality >= 60:
            info = "Kualitas Sedang - Seimbang"
            color = "green"
        elif quality >= 40:
            info = "Kualitas Rendah - Kompresi kuat"
            color = "orange"
        elif quality >= 20:
            info = "Kualitas Sangat Rendah - Ukuran minimal"
            color = "red"
        else:
            info = "EKSTREM: Kompresi maksimal, kualitas buruk"
            color = "darkred"
        
        self.quality_recommendation.set(info)
        self.quality_label.config(fg=color)

    def select_file(self):
        file_path = filedialog.askopenfilename(
            title="Pilih file untuk dikompres",
            filetypes=[
                ("Gambar", "*.jpg *.jpeg *.png"),
                ("PDF", "*.pdf"),
                ("Semua file", "*.*")
            ]
        )
        
        if file_path:
            self.selected_file.set(f"File: {os.path.basename(file_path)}")
            self.current_file = file_path
            self.compress_btn.config(state="normal")
            self.status_label.config(text="File siap untuk dikompres", fg="green")
            
            # Show file info
            file_size = os.path.getsize(file_path)
            file_size_mb = file_size / (1024 * 1024)
            messagebox.showinfo("Info File", f"Ukuran file: {file_size_mb:.2f} MB")

    def compress_image(self, input_path, output_path, quality):
        try:
            print(f"Memulai kompresi dengan kualitas: {quality}")
            
            # Buka gambar
            with Image.open(input_path) as img:
                # Info gambar asli
                print(f"Mode asli: {img.mode}, Ukuran: {img.size}")
                
                # Copy gambar untuk manipulasi
                result_img = img.copy()
                
                # Resize jika diminta
                if self.resize_factor and self.resize_factor < 1.0:
                    new_size = tuple(int(dim * self.resize_factor) for dim in result_img.size)
                    result_img = result_img.resize(new_size, Image.Resampling.LANCZOS)
                    print(f"Diresize ke: {new_size}")
                
                # Deteksi format output
                output_ext = os.path.splitext(output_path)[1].lower()
                
                # Konversi mode untuk JPEG
                if output_ext in ['.jpg', '.jpeg']:
                    if result_img.mode in ('RGBA', 'LA'):
                        # Buat background putih untuk transparansi
                        background = Image.new('RGB', result_img.size, (255, 255, 255))
                        if result_img.mode == 'LA':
                            result_img = result_img.convert('RGBA')
                        background.paste(result_img, mask=result_img.split()[-1])
                        result_img = background
                    elif result_img.mode in ('P', 'L', '1', 'CMYK'):
                        result_img = result_img.convert('RGB')
                
                # Parameter save yang memungkinkan kompresi kuat
                if output_ext in ['.jpg', '.jpeg']:
                    save_params = {
                        'format': 'JPEG',
                        'quality': max(10, quality),  # Minimum 10, bukan 50
                        'optimize': True,
                        'progressive': True if quality < 60 else False
                    }
                elif output_ext == '.png':
                    # Untuk PNG, convert ke palette jika kualitas rendah
                    if quality < 50:
                        # Convert ke palette 256 warna untuk ukuran lebih kecil
                        result_img = result_img.convert('P', palette=Image.Palette.ADAPTIVE, colors=256)
                    
                    save_params = {
                        'format': 'PNG',
                        'optimize': True,
                        'compress_level': 9  # Kompresi maksimal untuk PNG
                    }
                
                # Simpan gambar
                result_img.save(output_path, **save_params)
                
                print(f"Berhasil menyimpan: {output_path}")
                return True
                
        except Exception as e:
            print(f"Error: {str(e)}")
            messagebox.showerror("Error", f"Gagal mengompres gambar: {str(e)}")
            return False

    def compress_pdf_simple(self, input_path, output_path):
        """PDF compression dengan PyPDF2"""
        try:
            reader = PdfReader(input_path)
            writer = PdfWriter()
            
            for page in reader.pages:
                # Kompres konten halaman
                page.compress_content_streams()
                writer.add_page(page)
            
            # Hapus metadata
            writer.add_metadata({})
            
            with open(output_path, "wb") as f:
                writer.write(f)
            
            return True
        except Exception as e:
            messagebox.showerror("Error", f"Gagal mengompres PDF: {str(e)}")
            return False

    def compress_file(self):
        if not hasattr(self, 'current_file'):
            messagebox.showwarning("Peringatan", "Pilih file terlebih dahulu!")
            return

        file_dir = os.path.dirname(self.current_file)
        file_name, file_ext = os.path.splitext(os.path.basename(self.current_file))
        suggested_name = f"{file_name}_compressed{file_ext}"

        output_path = filedialog.asksaveasfilename(
            title="Simpan file hasil kompres",
            initialdir=file_dir,
            initialfile=suggested_name,
            defaultextension=file_ext,
            filetypes=[(f"File {file_ext.upper()}", f"*{file_ext}"), ("Semua file", "*.*")]
        )
        
        if not output_path:
            self.status_label.config(text="Dibatalkan", fg="gray")
            return

        self.status_label.config(text="Sedang mengompres...", fg="orange")
        self.root.update()

        ext = file_ext.lower()
        success = False
        
        if ext in [".jpg", ".jpeg", ".png"]:
            quality = self.quality_scale.get()
            success = self.compress_image(self.current_file, output_path, quality)
        elif ext == ".pdf":
            success = self.compress_pdf_simple(self.current_file, output_path)
        else:
            messagebox.showerror("Error", "Tipe file tidak didukung!")
            self.status_label.config(text="Tipe file tidak didukung", fg="red")
            return

        if success:
            original_size = os.path.getsize(self.current_file)
            compressed_size = os.path.getsize(output_path)
            reduction = max(0.0, (original_size - compressed_size) / original_size * 100)

            messagebox.showinfo(
                "Berhasil!",
                f"File berhasil dikompres!\n\n"
                f"Ukuran asli: {self.format_size(original_size)}\n"
                f"Ukuran setelah kompres: {self.format_size(compressed_size)}\n"
                f"Pengurangan: {reduction:.1f}%\n\n"
                f"File disimpan sebagai:\n{os.path.basename(output_path)}"
            )
            self.status_label.config(text="Kompres berhasil!", fg="green")
        else:
            self.status_label.config(text="Kompres gagal!", fg="red")

    def format_size(self, size_bytes):
        """Format ukuran file ke format yang mudah dibaca"""
        if size_bytes < 1024:
            return f"{size_bytes} B"
        elif size_bytes < 1024*1024:
            return f"{size_bytes/1024:.1f} KB"
        else:
            return f"{size_bytes/(1024*1024):.1f} MB"

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = FileCompressor()
    app.run()