from vosk import Model, KaldiRecognizer
import os
import pyaudio

# Validacao da pasta de modelo
# Eh necessario criar a pasta model-br a partir de onde estiver este fonte
if not os.path.exists("pt"):
    print ("Modelo em portugues nao encontrado.")
    exit (1)

# Preparando o microfone para captura
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

# Apontando o algoritmo para ler o m odelo treinado na pasta "model-br"
model = Model(r"C:\Users\wgngu\Desktop\test\fala\pt")
rec = KaldiRecognizer(model, 16000)

# Criando um loop continuo para ficar ouvindo o microfone
while True:
    # Lendo audio do microfone
    data = stream.read(4000)
    
    # Convertendo audio em texto
    if rec.AcceptWaveform(data):
        print(rec.Result())
        