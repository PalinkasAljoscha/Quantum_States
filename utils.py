import cirq
import numpy as np


def show_dirac_evol(circuit,round_digits=3):
    n_qubits = len(circuit.all_qubits())
    subcircuit = cirq.Circuit()
    print('start in', format(0, '0'+str(n_qubits)+'b'))
    for mo in circuit.moments:
        ops = mo.operations
        subcircuit.append(ops)
        wf = np.round(subcircuit.final_state_vector(),round_digits)
        print('...wavefunction after applying',end=' ')
        [print(x,end=', ') for x in ops]
        print(':\n'+' + '.join([str(np.round(wf[i],2))+'|'+format(i, '0'+str(n_qubits)+'b')+'>' 
                          for i in range(len(wf)) if wf[i]!=0]))

def show_vec_evol(circuit,round_digits=3):
    n_qubits = len(circuit.all_qubits())
    subcircuit = cirq.Circuit()
    print('start in', format(0, '0'+str(n_qubits)+'b'))
    for mo in circuit.moments:
        ops = mo.operations
        subcircuit.append(ops)
        wf = np.round(subcircuit.final_state_vector(),round_digits)
        print('...wavefunction after applying',end=' ')
        [print(x,end=', ') for x in ops]
        print(':\n',wf,'\n')
    