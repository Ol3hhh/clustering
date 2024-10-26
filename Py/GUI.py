import tkinter as tk
from tkinter import ttk
from clustering import clustering, points, categories, glasses, alcoholic, tags, ingredients


# GUI analysis of cocktails using tkinter
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("K-means Analysis")
        self.geometry("800x600")

        # Create main frame with a canvas and vertical scrollbar
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=1)

        self.canvas = tk.Canvas(self.main_frame)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        self.scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Create a frame inside the canvas for content
        self.second_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.second_frame, anchor="nw")

        # Label and ComboBox for selecting a cocktail
        self.label = tk.Label(self.second_frame, text="Choose a cocktail from the list")
        self.label.pack(pady=10)

        # Populate ComboBox with cocktail names
        self.combo = ttk.Combobox(self.second_frame, values=[point[0] for point in points])
        self.combo.pack(pady=10)
        self.combo.bind("<<ComboboxSelected>>", self.show_similar)

        # Label to display similar cocktails
        self.result_label = tk.Label(self.second_frame, text="", justify=tk.LEFT)
        self.result_label.pack(pady=10)

    def show_similar(self, event):
        selected_cocktail = self.combo.get()

        # Find the selected cocktail and retrieve similar cocktails
        for point in points:
            if point[0] == selected_cocktail:
                similar = clustering.compare(point)
                break

        # Format and display information for similar cocktails
        similar_info = []
        for cocktail in similar:
            category = list(categories.keys())[list(categories.values()).index(cocktail[1])]
            glass = list(glasses.keys())[list(glasses.values()).index(cocktail[2])]
            alc = list(alcoholic.keys())[list(alcoholic.values()).index(cocktail[3])]
            tags_list = [list(tags.keys())[list(tags.values()).index(t)] for t in cocktail[4]]
            ingredients_list = [list(ingredients.keys())[list(ingredients.values()).index(i)] for i in cocktail[5]]
            info = f"{cocktail[0]}:\n  Category: {category}\n  Glass: {glass}\n  Alcoholic: {alc}\n  Tags: {', '.join(tags_list)}\n  Ingredients: {', '.join(ingredients_list)}"
            similar_info.append(info)

        self.result_label.config(text="Similar drinks:\n" + "\n\n".join(similar_info))
