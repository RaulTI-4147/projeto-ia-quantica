from fastapi import FastAPI
from datetime import datetime
from quantum_core import QuantumAI
import uvicorn

app = FastAPI(title='Sistema IA Quantica')
quantum_system = QuantumAI()

@app.get('/')
def read_root():
    return {
        'status': 'online',
        'sistema': 'IA Quantica',
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

@app.post('/initialize')
def initialize_system():
    return quantum_system.initialize()

@app.get('/status')
def get_status():
    return quantum_system.status()

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)