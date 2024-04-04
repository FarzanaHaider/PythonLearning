scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0,weight=1)
window.grid_rcolumnconfigure(0,weight=1)
text_area.grid(sticky=N + E + S + W)