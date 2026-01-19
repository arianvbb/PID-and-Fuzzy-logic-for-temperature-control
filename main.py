import matplotlib.pyplot as plt
import Fuzzy
import PID

MPC_temp = []

Fuzzy.Fuzzy_run()
PID.PID_run()

figure, axes = plt.subplots(2, 1, figsize = (18, 10), dpi = 120)
figure.suptitle("Different temperature controls")

axes[0].plot(PID.Time, PID.PID_temp)
axes[0].set_title("PID")
axes[0].axhline(21, color = "red")
axes[0].set_xlabel("Time") 
axes[0].set_ylabel("Temperature")

axes[1].plot(Fuzzy.Time, Fuzzy.Fuzzy_temp)
axes[1].set_title("Fuzzy")
axes[1].axhline(21, color = "red")
axes[1].set_xlabel("Time") 
axes[1].set_ylabel("Temperature")

#axes[2].plot(MPC.Time, MPC_temp)
#axes[2].set_title("MPC")
#axes[2].axhline(21, color = "red")
#axes[2].set_xlabel("Time") 
#axes[2].set_ylabel("Temperature")

plt.tight_layout()
plt.show()
