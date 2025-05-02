from datetime import datetime
from quantum_operations import QuantumOperations

class QuantumAI:
    def __init__(self):
        self.initialized = False
        self.start_time = datetime.now()
        self.quantum_ops = QuantumOperations()
    
    def initialize(self):
        self.initialized = True
        quantum_state = self.quantum_ops.simulate_quantum_state()
        self.quantum_ops.register_operation("initialization")
        
        return {
            "status": "success",
            "message": "Sistema IA Quantica inicializado",
            "timestamp": self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "quantum_state": quantum_state
        }
        
    def status(self):
        return {
            "initialized": self.initialized,
            "uptime": str(datetime.now() - self.start_time),
            "operations_history": self.quantum_ops.get_operations_history()
        }
