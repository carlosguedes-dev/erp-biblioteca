import customtkinter as ctk
import database
from tkinter import messagebox

# Configurações globais
ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ERP Biblioteca - Gestão Inteligente")
        self.geometry("1100x700")
        self.minsize(900, 600)
        
        # Inicializa DB
        database.init_db()

        # Configuração do grid (1 linha, 2 colunas)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # --- BARRA LATERAL ---
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="📚 ERP Biblioteca", font=ctk.CTkFont(size=24, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(30, 30))

        self.btn_dashboard = ctk.CTkButton(self.sidebar_frame, text="📊 Dashboard", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", font=ctk.CTkFont(size=16), command=self.show_dashboard)
        self.btn_dashboard.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.btn_books = ctk.CTkButton(self.sidebar_frame, text="📖 Acervo", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", font=ctk.CTkFont(size=16), command=self.show_books)
        self.btn_books.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        self.btn_clients = ctk.CTkButton(self.sidebar_frame, text="👥 Leitores", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", font=ctk.CTkFont(size=16), command=self.show_clients)
        self.btn_clients.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

        self.btn_loans = ctk.CTkButton(self.sidebar_frame, text="🔄 Empréstimos", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", font=ctk.CTkFont(size=16), command=self.show_loans)
        self.btn_loans.grid(row=4, column=0, padx=10, pady=5, sticky="ew")
        
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Tema:", anchor="w")
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Dark", "Light", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=7, column=0, padx=20, pady=(10, 20))

        # --- ÁREA PRINCIPAL ---
        self.main_frame = ctk.CTkFrame(self, corner_radius=15, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        
        # Views dictionary
        self.views = {}
        
        self.setup_dashboard()
        self.setup_books()
        self.setup_clients()
        self.setup_loans()

        # Iniciar no Dashboard
        self.show_dashboard()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)
        
    def hide_all_views(self):
        for view in self.views.values():
            view.grid_forget()
        
        # Reset buttons styles
        buttons = [self.btn_dashboard, self.btn_books, self.btn_clients, self.btn_loans]
        for btn in buttons:
            btn.configure(fg_color="transparent")

    # ==============================
    # DASHBOARD
    # ==============================
    def setup_dashboard(self):
        frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.views["dashboard"] = frame
        
        title = ctk.CTkLabel(frame, text="Visão Geral do Sistema", font=ctk.CTkFont(size=28, weight="bold"))
        title.pack(anchor="w", pady=(0, 20))
        
        cards_frame = ctk.CTkFrame(frame, fg_color="transparent")
        cards_frame.pack(fill="x", pady=10)
        cards_frame.grid_columnconfigure((0, 1, 2), weight=1)
        
        # Card 1
        self.card_books = ctk.CTkFrame(cards_frame, corner_radius=15, fg_color="#1f538d")
        self.card_books.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(self.card_books, text="Acervo (Livros)", font=ctk.CTkFont(size=16)).pack(pady=(20,5))
        self.lbl_total_books = ctk.CTkLabel(self.card_books, text="0", font=ctk.CTkFont(size=40, weight="bold"))
        self.lbl_total_books.pack(pady=(0,20))

        # Card 2
        self.card_clients = ctk.CTkFrame(cards_frame, corner_radius=15, fg_color="#2c7a7b")
        self.card_clients.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(self.card_clients, text="Leitores Ativos", font=ctk.CTkFont(size=16)).pack(pady=(20,5))
        self.lbl_total_clients = ctk.CTkLabel(self.card_clients, text="0", font=ctk.CTkFont(size=40, weight="bold"))
        self.lbl_total_clients.pack(pady=(0,20))

        # Card 3
        self.card_loans = ctk.CTkFrame(cards_frame, corner_radius=15, fg_color="#b83232")
        self.card_loans.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(self.card_loans, text="Empréstimos Pendentes", font=ctk.CTkFont(size=16)).pack(pady=(20,5))
        self.lbl_total_loans = ctk.CTkLabel(self.card_loans, text="0", font=ctk.CTkFont(size=40, weight="bold"))
        self.lbl_total_loans.pack(pady=(0,20))
        
        subtitle = ctk.CTkLabel(frame, text="Últimos Movimentos", font=ctk.CTkFont(size=20, weight="bold"))
        subtitle.pack(anchor="w", pady=(30, 10))
        
        self.recent_frame = ctk.CTkScrollableFrame(frame, fg_color="transparent")
        self.recent_frame.pack(fill="both", expand=True)

    def show_dashboard(self):
        self.hide_all_views()
        self.btn_dashboard.configure(fg_color=("gray75", "gray25"))
        self.views["dashboard"].grid(row=0, column=0, sticky="nsew")
        
        # Atualizar dados
        t_books, t_clients, active_loans = database.get_dashboard_metrics()
        self.lbl_total_books.configure(text=str(t_books))
        self.lbl_total_clients.configure(text=str(t_clients))
        self.lbl_total_loans.configure(text=str(active_loans))
        
        # Atualizar recentes
        for widget in self.recent_frame.winfo_children():
            widget.destroy()
            
        loans = database.get_active_loans()
        for i, l in enumerate(loans[:5]): # pegar apenas os 5 ultimos
            item = ctk.CTkFrame(self.recent_frame, corner_radius=10)
            item.pack(fill="x", pady=5, padx=5)
            ctk.CTkLabel(item, text=f"📖 {l[1]}", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=15, pady=15)
            ctk.CTkLabel(item, text=f"👤 {l[2]}").pack(side="left", padx=15, pady=15)
            ctk.CTkLabel(item, text=f"📅 {l[3]} até {l[4]}").pack(side="right", padx=15, pady=15)

    # ==============================
    # LIVROS
    # ==============================
    def setup_books(self):
        frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.views["books"] = frame
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        
        header = ctk.CTkFrame(frame, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))
        
        ctk.CTkLabel(header, text="Gestão de Acervo", font=ctk.CTkFont(size=28, weight="bold")).pack(side="left")
        ctk.CTkButton(header, text="+ Novo Livro", font=ctk.CTkFont(weight="bold"), command=self.open_new_book_window).pack(side="right")
        
        self.books_list = ctk.CTkScrollableFrame(frame)
        self.books_list.grid(row=1, column=0, sticky="nsew")

    def open_new_book_window(self):
        dialog = ctk.CTkToplevel(self)
        dialog.title("Adicionar Livro")
        dialog.geometry("400x400")
        dialog.attributes('-topmost', True)
        
        ctk.CTkLabel(dialog, text="Título:").pack(pady=(20, 5))
        e_title = ctk.CTkEntry(dialog, width=300)
        e_title.pack(pady=5)
        
        ctk.CTkLabel(dialog, text="Autor:").pack(pady=(10, 5))
        e_author = ctk.CTkEntry(dialog, width=300)
        e_author.pack(pady=5)
        
        ctk.CTkLabel(dialog, text="Categoria/Gênero:").pack(pady=(10, 5))
        e_category = ctk.CTkEntry(dialog, width=300)
        e_category.pack(pady=5)
        
        def save():
            t = e_title.get()
            a = e_author.get()
            c = e_category.get()
            if t and a and c:
                database.add_book(t, a, c)
                dialog.destroy()
                self.show_books()
            else:
                messagebox.showerror("Erro", "Preencha todos os campos!")
                
        ctk.CTkButton(dialog, text="Salvar", command=save).pack(pady=30)

    def show_books(self):
        self.hide_all_views()
        self.btn_books.configure(fg_color=("gray75", "gray25"))
        self.views["books"].grid(row=0, column=0, sticky="nsew")
        
        for widget in self.books_list.winfo_children():
            widget.destroy()
            
        books = database.get_all_books()
        for b in books:
            item = ctk.CTkFrame(self.books_list, corner_radius=10)
            item.pack(fill="x", pady=5, padx=5)
            
            # id, title, author, category, status, added_date
            status_color = "green" if b[4] == "Disponível" else "orange"
            
            ctk.CTkLabel(item, text=f"ID: {b[0]}", width=50).pack(side="left", padx=10, pady=15)
            ctk.CTkLabel(item, text=b[1], font=ctk.CTkFont(weight="bold", size=15), width=250, anchor="w").pack(side="left", padx=10, pady=15)
            ctk.CTkLabel(item, text=b[2], width=200, anchor="w").pack(side="left", padx=10, pady=15)
            ctk.CTkLabel(item, text=b[3], width=150, anchor="w").pack(side="left", padx=10, pady=15)
            
            status_lbl = ctk.CTkLabel(item, text=b[4], text_color=status_color, font=ctk.CTkFont(weight="bold"))
            status_lbl.pack(side="right", padx=20, pady=15)

    # ==============================
    # CLIENTES
    # ==============================
    def setup_clients(self):
        frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.views["clients"] = frame
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        
        header = ctk.CTkFrame(frame, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))
        
        ctk.CTkLabel(header, text="Gestão de Leitores", font=ctk.CTkFont(size=28, weight="bold")).pack(side="left")
        ctk.CTkButton(header, text="+ Novo Leitor", font=ctk.CTkFont(weight="bold"), command=self.open_new_client_window).pack(side="right")
        
        self.clients_list = ctk.CTkScrollableFrame(frame)
        self.clients_list.grid(row=1, column=0, sticky="nsew")

    def open_new_client_window(self):
        dialog = ctk.CTkToplevel(self)
        dialog.title("Adicionar Leitor")
        dialog.geometry("400x500")
        dialog.attributes('-topmost', True)
        
        ctk.CTkLabel(dialog, text="Nome Completo:").pack(pady=(20, 5))
        e_name = ctk.CTkEntry(dialog, width=300)
        e_name.pack(pady=5)
        
        ctk.CTkLabel(dialog, text="CPF:").pack(pady=(10, 5))
        e_cpf = ctk.CTkEntry(dialog, width=300)
        e_cpf.pack(pady=5)
        
        ctk.CTkLabel(dialog, text="Email:").pack(pady=(10, 5))
        e_email = ctk.CTkEntry(dialog, width=300)
        e_email.pack(pady=5)
        
        ctk.CTkLabel(dialog, text="Telefone:").pack(pady=(10, 5))
        e_phone = ctk.CTkEntry(dialog, width=300)
        e_phone.pack(pady=5)
        
        def save():
            n = e_name.get()
            c = e_cpf.get()
            e = e_email.get()
            p = e_phone.get()
            if n and c:
                try:
                    database.add_client(n, c, e, p)
                    dialog.destroy()
                    self.show_clients()
                except Exception as ex:
                    messagebox.showerror("Erro", f"CPF já cadastrado ou erro: {ex}")
            else:
                messagebox.showerror("Erro", "Nome e CPF são obrigatórios!")
                
        ctk.CTkButton(dialog, text="Salvar", command=save).pack(pady=30)

    def show_clients(self):
        self.hide_all_views()
        self.btn_clients.configure(fg_color=("gray75", "gray25"))
        self.views["clients"].grid(row=0, column=0, sticky="nsew")
        
        for widget in self.clients_list.winfo_children():
            widget.destroy()
            
        clients = database.get_all_clients()
        for c in clients:
            item = ctk.CTkFrame(self.clients_list, corner_radius=10)
            item.pack(fill="x", pady=5, padx=5)
            
            # id, name, cpf, email, phone, date
            ctk.CTkLabel(item, text=f"👤 {c[1]}", font=ctk.CTkFont(weight="bold", size=16), width=250, anchor="w").pack(side="left", padx=15, pady=15)
            ctk.CTkLabel(item, text=f"CPF: {c[2]}", width=150, anchor="w").pack(side="left", padx=10, pady=15)
            ctk.CTkLabel(item, text=f"📧 {c[3]}", width=200, anchor="w").pack(side="left", padx=10, pady=15)
            ctk.CTkLabel(item, text=f"📞 {c[4]}", width=150, anchor="w").pack(side="left", padx=10, pady=15)

    # ==============================
    # EMPRÉSTIMOS
    # ==============================
    def setup_loans(self):
        frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.views["loans"] = frame
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        
        header = ctk.CTkFrame(frame, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(0, 20))
        
        ctk.CTkLabel(header, text="Controle de Circulação", font=ctk.CTkFont(size=28, weight="bold")).pack(side="left")
        ctk.CTkButton(header, text="🔄 Novo Empréstimo", font=ctk.CTkFont(weight="bold"), fg_color="#b83232", hover_color="#9c2727", command=self.open_new_loan_window).pack(side="right")
        
        self.loans_list = ctk.CTkScrollableFrame(frame)
        self.loans_list.grid(row=1, column=0, sticky="nsew")

    def open_new_loan_window(self):
        dialog = ctk.CTkToplevel(self)
        dialog.title("Registrar Empréstimo")
        dialog.geometry("400x400")
        dialog.attributes('-topmost', True)
        
        books = database.get_all_books()
        available_books = [b for b in books if b[4] == 'Disponível']
        
        clients = database.get_all_clients()
        
        if not available_books or not clients:
            messagebox.showwarning("Aviso", "É necessário ter livros disponíveis e leitores cadastrados!")
            dialog.destroy()
            return
            
        book_options = [f"{b[0]} - {b[1]}" for b in available_books]
        client_options = [f"{c[0]} - {c[1]}" for c in clients]
        
        ctk.CTkLabel(dialog, text="Selecione o Livro:").pack(pady=(20, 5))
        cb_books = ctk.CTkComboBox(dialog, values=book_options, width=300)
        cb_books.pack(pady=5)
        
        ctk.CTkLabel(dialog, text="Selecione o Leitor:").pack(pady=(10, 5))
        cb_clients = ctk.CTkComboBox(dialog, values=client_options, width=300)
        cb_clients.pack(pady=5)
        
        ctk.CTkLabel(dialog, text="Data de Devolução (YYYY-MM-DD):").pack(pady=(10, 5))
        e_date = ctk.CTkEntry(dialog, width=300)
        e_date.pack(pady=5)
        
        def save():
            b_val = cb_books.get()
            c_val = cb_clients.get()
            d_val = e_date.get()
            
            if b_val and c_val and d_val:
                b_id = int(b_val.split(" - ")[0])
                c_id = int(c_val.split(" - ")[0])
                database.add_loan(b_id, c_id, d_val)
                dialog.destroy()
                self.show_loans()
            else:
                messagebox.showerror("Erro", "Preencha todos os campos!")
                
        ctk.CTkButton(dialog, text="Registrar", fg_color="#b83232", hover_color="#9c2727", command=save).pack(pady=30)

    def show_loans(self):
        self.hide_all_views()
        self.btn_loans.configure(fg_color=("gray75", "gray25"))
        self.views["loans"].grid(row=0, column=0, sticky="nsew")
        
        for widget in self.loans_list.winfo_children():
            widget.destroy()
            
        loans = database.get_active_loans()
        for l in loans:
            item = ctk.CTkFrame(self.loans_list, corner_radius=10, fg_color="#361717")
            item.pack(fill="x", pady=5, padx=5)
            
            # l = (id, book_title, client_name, loan_date, return_date, status, book_id)
            loan_id = l[0]
            book_id = l[6]
            
            ctk.CTkLabel(item, text=f"📖 {l[1]}", font=ctk.CTkFont(weight="bold", size=15), width=250, anchor="w").pack(side="left", padx=15, pady=15)
            ctk.CTkLabel(item, text=f"👤 {l[2]}", width=200, anchor="w").pack(side="left", padx=10, pady=15)
            ctk.CTkLabel(item, text=f"Devolução: {l[4]}", width=150, anchor="w", text_color="#ff8c8c").pack(side="left", padx=10, pady=15)
            
            def make_return(lid=loan_id, bid=book_id):
                database.return_loan(lid, bid)
                self.show_loans()
                
            ctk.CTkButton(item, text="Baixar / Devolver", fg_color="green", hover_color="darkgreen", width=120, command=make_return).pack(side="right", padx=15, pady=15)

if __name__ == "__main__":
    app = App()
    app.mainloop()
