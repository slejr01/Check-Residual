import matplotlib.pyplot as plt
import json
class CheckResidual:
    def ReadData():
        Time = []
        P_rgh = []
        Omega = []
        K = []
        X=0
        with open("log.run") as f:
            for line in f:
                if "Time =" in line:
                    Temp_time = line.split("=")[-1].strip()
                    if "Execution" in line:
                        continue
                    Time.append(Temp_time)
                elif "GAMG:" in line:
                    Temp_prgh = line.split("=")[2].strip()
                    Temp_prgh = Temp_prgh.split(",")[0].strip()
                    X = X+1
                    if (X==8):
                        P_rgh.append(Temp_prgh)
                        X = 0
                elif "omega," in line:
                    Temp_omega = line.split("=")[2].strip()
                    Temp_omega = Temp_omega.split(",")[0].strip()
                    Omega.append(Temp_omega)
                elif "k," in line:
                    Temp_k = line.split("=")[2].strip()
                    Temp_k = Temp_k.split(",")[0].strip()
                    K.append(Temp_k)
            f.close()
            return Time, P_rgh, Omega, K

    Temp_1 = ReadData()

    def Float(Temp_1):
        Time, P_rgh, Omega, K = Temp_1
        time = [float(t) for t in Time]
        final_prgh = [float(p) for p in P_rgh]
        final_omega = [float(o) for o in Omega]
        final_k = [float(k) for k in K]
        return time, final_prgh, final_omega, final_k
    Temp_2 = Float(Temp_1)

    def JSON(Temp_2):
        time, final_prgh, final_omega, final_k = Temp_2
        data = {
            "Time": time,
            "P_rgh": final_prgh,
            "Omega": final_omega,
            "K": final_k
        }
        with open("Results.json", "w") as outfile:
            json.dump(data, outfile, indent=4)
        return json.dumps(data, indent=4)

    JSON(Temp_2)
class Graph:

    def Plot_Graph():
        time, final_prgh, final_omega, final_k = CheckResidual.Temp_2
        plt.plot(time, final_prgh, label="P_rgh")
        plt.plot(time, final_omega, label="Omega")
        plt.plot(time, final_k, label="K")
        plt.yscale("log")
        plt.xlabel("Time")
        plt.ylabel("Final residual")
        plt.legend()
        plt.show()
    Plot_Graph()
