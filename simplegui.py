"""
Extremely simple tool to get davinci responses in a GUI.
"""

from toolkit.queryGPT import query_davinci

import tkinter as tk

if __name__ == "__main__":

    root = tk.Tk()
    root.title("Davinci Model GUI interface")
    root.resizable(False, False)

    outgoing_label = tk.Label(root, text="input your prompt here:")
    outgoing_prompt = tk.Text(root, width=50, height=10, wrap="word")

    send_it_button = tk.Button(root,
                               text="query Davinci-003",
                               command=lambda:incoming_label_var.set(
                                   query_davinci(outgoing_prompt.get("1.0", "end-1c")
                                                 )
                                    )
                               )

    incoming_label_var = tk.StringVar(root, "no response yet")
    incoming_label = tk.Label(root,
                              textvariable=incoming_label_var, wraplength=400)

    outgoing_label.pack()
    outgoing_prompt.pack()
    send_it_button.pack()
    incoming_label.pack()

    root.mainloop()
