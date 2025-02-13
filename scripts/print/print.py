from statistics import mean
import matplotlib.pyplot as plt
import numpy as np

PATH = "out/official/"
CONF = "20250127_182418/"           # configuration name here
with open(PATH + CONF + "log.txt", "r") as f:
    string = f.read()

test = False
train_loss = []
val_loss = []
for line in string.split("\n"):
    line = line.strip()
    
    if line.startswith("INFO:root:"):
        line = line[10:]
    else:
        continue
    
    print(line)
    try:
        if line.startswith("Training epoch") and "Iteration 1," not in line:
            train_loss.append(float(line.split(":")[1].strip()))
            
        if line.startswith("Validation iteration") and not test and "iteration 1," not in line :
            val_loss.append(float(line.split(":")[1].strip()))
    except IndexError:
        pass
        
    if line.startswith("Inference..."):
        test = True
        
print(len(train_loss))
print(len(val_loss))


# val_loss_avg = [mean(val_loss[i:i+19]) for i in range(0, len(val_loss), 19)]
# plt.figure(figsize=(10, 5))
# plt.plot(range(len(val_loss_avg) * 19), np.repeat(val_loss_avg, 19), label="Validation (avg)", color='orange')

plt.plot(train_loss[::], label="Train")
#plt.plot(val_loss[::], label="Validation")
plt.grid(which='both')
plt.legend()
plt.show()