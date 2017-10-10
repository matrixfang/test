import networkx as nx
import numpy as np

def Euler_method_Kuramoto(node_list, neighbor_list, theta_start, w, K, T, delta_t):
    N = len(node_list)
    theta0[:] = theta_start[:]
    theta = [theta0]
    for step in range(int(T/delta_t)):
        theta.append([0] * N)
        for i in node_list:
            f = w[i]
            for j in neighbor_list[i]:
                f += K / N * (np.sin(theta[0][j] - theta[0][i]))
            theta[1][i] = theta[0][i] + delta_t * f
        theta.pop(0)
    return theta[0]

def Adams_Moulton_method_Kuramoto(node_list, neighbor_list,theta_start, w, K, T, delta_t):
    N = len(node_list)
    theta0[:] = theta_start[:]
    theta =[theta0]
    f = [[0] * N, [0] * N, [0] * N]

    # step one: Euler method
    theta.append([0] * N)
    for i in node_list:
        f[0][i] = w[i]
        for j in neighbor_list[i]:
            f[0][i] += K / N * (np.sin(theta[0][j]-theta[0][i]))
        theta[1][i] = theta[0][i] + delta_t * f[0][i]
    theta.pop(0)
    # step two
    theta.append([0] * N)
    for i in node_list:
        f[1][i] = w[i]
        for j in neighbor_list[i]:
            f[1][i] += K / N * (np.sin(theta[0][j]-theta[0][i]))
        theta[1][i] = theta[0][i] + delta_t * (3 / 2 * f[1][i] - 1 / 2 * f[0][i])
    theta.pop(0)
    # step three
    theta.append([0] * N)
    for i in node_list:
        f[2][i] = w[i]
        for j in neighbor_list[i]:
            f[2][i] += K / N * (np.sin(theta[0][j] - theta[0][i]))
        theta[1][i] = theta[0][i] + delta_t * (23 / 12 * f[2][i] - 4 / 3 * f[1][i] + 5 / 12 * f[0][i])
    theta.pop(0)

    for step in range(4, int(T/delta_t)):
        theta.append([0] * N)
        f.append([0] * N)# add new list to store newest calculation results
        for i in node_list:
            f[3][i] = w[i]
            for j in neighbor_list[i]:
                f[3][i] += K / N * (np.sin(theta[0][j] - theta[0][i]))
            theta[1][i] = theta[0][i] + delta_t * (55 / 24 * f[3][i] - 59 / 24 * f[2][i] + 37 / 24 * f[1][i] - 3 / 8 * f[0][i])
        theta.pop(0)
        f.pop(0)# delte the useless thing

    return theta[0]

def Runge_Kutta_method_Kuramoto(node_list, neighbor_list,theta_start, w, K, T, delta_t):
    N = len(node_list)
    k1 = [0] * N
    k2 = [0] * N
    k3 = [0] * N
    k4 = [0] * N
    theta = [theta_start]
    for step in range(int(T/delta_t)):
        theta.append([0] * N)
        for i in node_list:
            k1[i] = w[i]
            for j in neighbor_list[i]:
                k1[i] += K / N * np.sin(theta[0][j] - theta[0][i])
        for i in node_list:
            k2[i] = w[i]
            for j in neighbor_list[i]:
                k2[i] += K / N * np.sin(theta[0][j]+ delta_t / 2 * k1[j] - theta[0][i] - delta_t / 2 * k1[i])
        for i in node_list:
            k3[i] = w[i]
            for j in neighbor_list[i]:
                k3[i] += K / N * np.sin(theta[0][j] + delta_t / 2 * k2[j] - theta[0][i] - delta_t / 2 *k2[i])
        for i in node_list:
            k4[i] = w[i]
            for j in neighbor_list[i]:
                k4[i] += K / N * np.sin(theta[0][j] + delta_t* k3[j] - theta[0][i] - delta_t * k3[i])

        for i in node_list:
            theta[1][i] = theta[0][i] + delta_t / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i])
        theta.pop(0)

    return theta[0]



G = nx.complete_graph(10)
neighbor_list = []

for i in G.nodes():
    neighbor_list.append(G.neighbors(i))

node_list = G.nodes()
N = len(node_list)
theta0 = np.random.normal(0, 1, N)

T = 500
delta_t = 0.02
K = 1
w = np.random.normal(0, 1, N)
theta_start = np.random.normal(0, 1, N)

theta1 = Euler_method_Kuramoto(node_list, neighbor_list, theta_start, w, K, T, delta_t)
theta2 = Adams_Moulton_method_Kuramoto(node_list, neighbor_list, theta_start, w, K, T, delta_t)
theta3 = Runge_Kutta_method_Kuramoto(node_list, neighbor_list,theta_start, w, K, T, delta_t)
theta1 = np.remainder(theta1, 2 * np.pi)
theta2 = np.remainder(theta2, 2 * np.pi)
theta3 = np.remainder(theta3, 2 * np.pi)

file = open('theta1.txt', 'w')
for value in theta1:
    print(value, file = file)
file.close()

file = open('theta2.txt', 'w')
for value in theta2:
    print(value, file = file)
file.close()

file = open('theta3.txt', 'w')
for value in theta3:
    print(value, file =file)
file.close()

minus = lambda x, y : x - y

print(sum(map(abs, map(minus, theta1, theta3))) / N,sum(map(abs, map(minus, theta2,theta3))) / N)