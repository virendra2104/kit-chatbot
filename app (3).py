import gradio as gr
import os
from mistralai import Mistral

client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

SYSTEM_MESSAGE = """
College Name:Kashi Institute of Technology
Affiliated to :Dr.APJ Abdul kalam Technical University(Lucknow)
Course offered:B.Tech,B.Pharma,MCA,BCA,Polytecnic,BBA,MBA
B.tech branch:CSE,ME,ECE,Civil,EE,CSE(AI&ML)
Fee Structure of B.tech(CSE):120000
Fee Structure of B.tech(other than cse):100000
Fee Structure of B.Pharma):135000
Fee Structure of BBA:80000
Fee Structure of MBA:125000
Fee Structure of Polytecnic:55000
Fee Structure of BCA:70000
Fee Structure of MCA:110000
All the fee structure:Year wise
Facility:AC calssroom,Full campus Wi-Fi,Digial Library,Auditoriam,Two Seminar Hall,Full placement guidance and assisment and more
Faculty:Top Class
Specification:Top College in Purvanchal
transport ,mess and hostel :Avalilable
Phone:+918345039403
E-mail:kashiit@gmail.com
Website:www.kashiit.ac.in
Answer only based on the above information.
If a question is outside this scope, politely say you don’t have that information.
"""

def chat(user_input, history):
    if history is None:
        history = []

    messages = [{"role": "system", "content": SYSTEM_MESSAGE}]
    messages.extend(history)
    messages.append({"role": "user", "content": user_input})

    response = client.chat.complete(
        model="mistral-small",
        messages=messages
    )

    reply = response.choices[0].message.content

    history.append({"role": "user", "content": user_input})
    history.append({"role": "assistant", "content": reply})

    return reply, history


with gr.Blocks() as demo:
    gr.Markdown("### Blismos Academy Chatbot API")

    user_input = gr.Textbox(label="Message")
    state = gr.State([])
    output = gr.Textbox(label="Response")

    user_input.submit(
        chat,
        inputs=[user_input, state],
        outputs=[output, state],
        api_name="predict"   # 🔥 Your HTML will call this
    )

demo.launch()
