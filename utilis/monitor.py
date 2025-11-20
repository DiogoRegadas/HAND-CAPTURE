# src/utilis/monitor.py

import psutil
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
import time

def start_monitoring():


    times = [0]
    cpu_vals = [0]
    mem_vals = [0]

    start_time = time.time()

    fig, ax = plt.subplots()
    ax.set_title("Real-Time CPU & Memory Usage")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Usage (%)")
    ax.set_ylim(0, 100)
    ax.set_xlim(0, 60)

    cpu_line, = ax.plot(times, cpu_vals, label="CPU (%)", color="cyan")
    mem_line, = ax.plot(times, mem_vals, label="Memory (%)", color="magenta")
    ax.legend()
    plt.tight_layout()

    def update(frame):
        current_time = time.time() - start_time
        process = psutil.Process(os.getpid())

        cpu = process.cpu_percent(interval=0.1)
        mem = process.memory_percent()

        times.append(current_time)
        cpu_vals.append(cpu)
        mem_vals.append(mem)

        if len(times) > 60:
            times.pop(0)
            cpu_vals.pop(0)
            mem_vals.pop(0)

        cpu_line.set_data(times, cpu_vals)
        mem_line.set_data(times, mem_vals)
        ax.set_xlim(times[0], times[-1] + 1)

        return cpu_line, mem_line

    ani = animation.FuncAnimation(fig, update, interval=1000)
    plt.show()
