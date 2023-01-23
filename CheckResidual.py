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
        time = []
        final_prgh = []
        final_omega = []
        final_k = []
        Lenght = len(Time)
        for i in range(Lenght):
            temp_1 = float(Time[i])
            time.append(temp_1)
            temp_2 = float(P_rgh[i])
            final_prgh.append(temp_2)
            temp_3 = float(Omega[i])
            final_omega.append(temp_3)
            temp_4 = float(K[i])
            final_k.append(temp_4)
        return time, final_prgh, final_omega, final_k

    Temp_2 = Float(Temp_1)

    def JSON(Temp_2):
        time, final_prgh, final_omega, final_k = Temp_2
        Time_json = json.dumps(time, indent=4)
        Prgh_json = json.dumps(final_prgh, indent=4)
        Omega_json = json.dumps(final_omega, indent=4)
        K_json = json.dumps(final_k, indent=4)
        with open("Results.json", "w") as outfile:
            outfile.write(Time_json)
            outfile.write(Prgh_json)
            outfile.write(Omega_json)
            outfile.write(K_json)
        outfile.close()
        return Time_json, Prgh_json, Omega_json, K_json
    JSON(Temp_2)
class Graph:

    def Plot_Graph():
        time, final_prgh, final_omega, final_k = CheckResidual.Temp_2
        x1 = time
        y1 = final_prgh
        plt.plot(x1, y1, label="P_rgh")
        x2 = time
        y2 = final_omega
        plt.plot(x2, y2, label="Omega")
        x3 = time
        y3 = final_k
        plt.plot(x3, y3, label="K")
        plt.yscale("log")
        plt.xlabel("Time")
        plt.ylabel("Final residual")
        plt.legend()
        plt.show()
    Plot_Graph()