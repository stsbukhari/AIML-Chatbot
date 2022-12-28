import aiml

kernel = aiml.Kernel()
kernel.learn("BasicChat.aiml")
#print(kernel.respond("How are you"))

while True:
    print(kernel.respond("How ARE YOU"))
