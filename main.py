from customtkinter import *
import random

set_appearance_mode("dark")
set_default_color_theme("dark-blue")

root = CTk(fg_color="#222")
root.title("Search & Filter")
root.geometry("750x500")
# 464d75

def on_button_release(event):
    search_term = event.widget.get()
    search_filter(search_term)

def generate_random_fruit_name(number):
    return random.sample(fruits, number)

def search_filter(search_term):
    for widget in searching_frame.winfo_children():
            widget.destroy()

    if search_term == "":
        initial_fruits = generate_random_fruit_name(10)
        for item in initial_fruits:
            CTkButton(searching_frame, text=f"  {item}", width=20, font=("Poppins", 21, "normal"), command=lambda item=item: on_button_click(item), 
                    anchor="w", corner_radius=0, fg_color="#333", text_color="#c7c3c3", hover_color="#444").pack(fill=X, pady=0, ipady=10, padx=1)
    else:
        filtered_data = [item for item in fruits if item.lower().startswith(search_term.lower())]
        filtered_data.sort()
        for item in filtered_data:
            CTkButton(searching_frame, text=f"  {item}", width=20, font=("Poppins", 21, "normal"), command=lambda item=item: on_button_click(item), 
                    anchor="w", corner_radius=0, fg_color="#333", text_color="#c7c3c3", hover_color="#444").pack(fill=X, pady=0, ipady=10, padx=1)

def on_button_click(item):
    print(item)

fruits = ["Apple", "Apricot", "Avocado", "Banana", "Blackberry", "Boysenberry", "Mango", "Mandarin", "Mulberry",
          "Cherry", "Coconut", "Cantaloupe", "Papaya", "Passionfruit", "Pomegranate", "Orange", "Olive",
          "Strawberry", "Star Fruit", "Pineapple", "Pear", "Plum", "Kiwi", "Kumquat", "Grape", "Guava", "Grapefruit",
          "Watermelon", "Peach", "Persimmon", "Blueberry", "Blackcurrant"]

search_box = CTkEntry(root, font=("Canbera", 22, "bold"), placeholder_text="Search for a fruit name ...", placeholder_text_color="#a5a5a5", corner_radius=5, border_width=0, fg_color="#333", text_color="white")
search_box.pack(side=TOP, fill=X, ipady=10, padx=20, pady=10)
search_box.bind("<KeyRelease>", on_button_release)

searching_frame = CTkScrollableFrame(root, fg_color="#444")
searching_frame.pack(side=BOTTOM, fill=BOTH, expand=True, padx=20, pady=20)

for item in fruits:
    CTkButton(searching_frame, text=f"  {item}", width=20, font=("Poppins", 21, "normal"), command=lambda item=item: on_button_click(item), 
                    anchor="w", corner_radius=0, fg_color="#333", text_color="#c7c3c3", hover_color="#444").pack(fill=X, pady=0, ipady=10, padx=1)

root.mainloop()