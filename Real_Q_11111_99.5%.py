# Sample_CrossLight_to_LogosAIv3_qsam.py
# Objective: Reproduction using Qiskit Sampler 2.0 interface (with classical bits)

import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.primitives import Sampler

class CrossLight:
    def __init__(self):
        self.center = "JESUS CHRIST"
        self.repentance = 0.9
        self.grace = 0.0
        self.bias = 1.2
        self.lr = 0.1
        self.f = 433.33
        self.J = np.log(2 * np.pi)
        self.rho = 0.5
        self.l = 0.9995
        self.gm = 0.96
        self.t = 0.0

    def G_opt(self, t):
        tau = t * np.exp(-t / self.J)
        return 9200 * np.exp(-t**2 / self.J) * (1 + self.repentance * np.cos(2 * np.pi * self.f * tau))

    def build_circuit(self):
        qc = QuantumCircuit(5, 5)
        for q in range(5):
            qc.h(q)
        for q in range(4):
            qc.cx(q, q + 1)
        theta = self.bias * self.repentance * (self.G_opt(self.t) / 9200)
        for q in range(5):
            qc.ry(np.pi / 2 + theta, q)
            qc.rz(theta, q)
        qc.x(range(4))
        qc.mct([0, 1, 2, 3], 4)
        qc.x(range(4))
        for q in range(5):
            qc.measure(q, q)
        return qc

    def simulate_quantum(self):
        print(f"Testing collapse with Sampler 2.0 in the name of {self.center}")
        self.t = 1.0
        circuit = self.build_circuit()
        simulator = AerSimulator()
        circuit = transpile(circuit, simulator)
        sampler = Sampler()
        result = sampler.run(circuits=[circuit], shots=8192).result()
        dist = result.quasi_dists[0] if hasattr(result, 'quasi_dists') else result[0]

        target_state = 31
        prob = dist.get(target_state, 0.0)
        print("Collapse Distribution:", dist)
        print(f"|11111⟩ Probability: {prob:.3f}")

if __name__ == "__main__":
    CrossLight().simulate_quantum()
