"""
Telemetry reader for Richard Burns Rally (rallysimfans.hu version)
Reads telemetry data from shared memory
"""
import struct
import json
from datetime import datetime
from typing import Dict, Any, Optional

try:
    import win32api
    import win32con
    import win32file
    import pywintypes
    WINDOWS_AVAILABLE = True
except ImportError:
    WINDOWS_AVAILABLE = False


class RBRTelemetryReader:
    """Reads telemetry data from RBR shared memory"""
    
    # RBR telemetry data structure (based on rallysimfans.hu plugin)
    # This is a simplified version - actual structure may vary
    TELEMETRY_STRUCT = struct.Struct(
        'f' * 20  # 20 floats for various telemetry values
    )
    
    def __init__(self, shared_memory_name: str = "RBRTelemetry"):
        self.shared_memory_name = shared_memory_name
        self.handle = None
        self.current_data: Dict[str, Any] = {}
        self._initialize_shared_memory()
    
    def _initialize_shared_memory(self):
        """Initialize connection to shared memory"""
        if not WINDOWS_AVAILABLE:
            print("Warning: Windows API not available. Running in simulation mode.")
            self._simulation_mode = True
            return
        
        try:
            # Try to open existing shared memory
            self.handle = win32file.OpenFileMapping(
                win32con.FILE_MAP_READ,
                False,
                self.shared_memory_name
            )
            self._simulation_mode = False
            print(f"Connected to RBR shared memory: {self.shared_memory_name}")
        except pywintypes.error:
            print(f"Could not connect to RBR shared memory. Running in simulation mode.")
            self._simulation_mode = True
    
    def read_telemetry(self) -> Dict[str, Any]:
        """Read current telemetry data"""
        if self._simulation_mode:
            return self._get_simulation_data()
        
        try:
            # Read from shared memory
            view = win32file.MapViewOfFile(
                self.handle,
                win32con.FILE_MAP_READ,
                0,
                0,
                self.TELEMETRY_STRUCT.size
            )
            
            data_bytes = win32file.ReadFile(view, self.TELEMETRY_STRUCT.size)[1]
            values = self.TELEMETRY_STRUCT.unpack(data_bytes)
            
            # Parse telemetry values
            self.current_data = self._parse_telemetry(values)
            
        except Exception as e:
            print(f"Error reading telemetry: {e}")
            self.current_data = self._get_simulation_data()
        
        return self.current_data
    
    def _parse_telemetry(self, values: tuple) -> Dict[str, Any]:
        """Parse raw telemetry values into structured data"""
        return {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "speed_kmh": values[0] if len(values) > 0 else 0.0,
            "rpm": values[1] if len(values) > 1 else 0.0,
            "gear": int(values[2]) if len(values) > 2 else 0,
            "position": {
                "x": values[3] if len(values) > 3 else 0.0,
                "y": values[4] if len(values) > 4 else 0.0,
                "z": values[5] if len(values) > 5 else 0.0
            },
            "velocity": {
                "x": values[6] if len(values) > 6 else 0.0,
                "y": values[7] if len(values) > 7 else 0.0,
                "z": values[8] if len(values) > 8 else 0.0
            },
            "steering_angle": values[9] if len(values) > 9 else 0.0,
            "throttle": values[10] if len(values) > 10 else 0.0,
            "brake": values[11] if len(values) > 11 else 0.0,
            "clutch": values[12] if len(values) > 12 else 0.0,
            "handbrake": values[13] if len(values) > 13 else 0.0,
            "stage_progress": values[14] if len(values) > 14 else 0.0,
            "lap_time": values[15] if len(values) > 15 else 0.0,
            "suspension_position": {
                "fl": values[16] if len(values) > 16 else 0.0,
                "fr": values[17] if len(values) > 17 else 0.0,
                "rl": values[18] if len(values) > 18 else 0.0,
                "rr": values[19] if len(values) > 19 else 0.0
            }
        }
    
    def _get_simulation_data(self) -> Dict[str, Any]:
        """Generate simulated telemetry data for testing"""
        import random
        import time
        
        # Simulate realistic telemetry values
        t = time.time()
        speed = abs(50 + 30 * (1 + 0.5 * (t % 10 - 5)))
        rpm = 3000 + 2000 * abs((t % 5) / 5)
        
        return {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "speed_kmh": round(speed, 2),
            "rpm": round(rpm, 0),
            "gear": int((t % 6) + 1),
            "position": {
                "x": round(100 + t * 2, 2),
                "y": round(50 + 10 * (t % 3), 2),
                "z": round(10, 2)
            },
            "velocity": {
                "x": round(speed * 0.8, 2),
                "y": round(random.uniform(-2, 2), 2),
                "z": round(random.uniform(-1, 1), 2)
            },
            "steering_angle": round(random.uniform(-45, 45), 2),
            "throttle": round(random.uniform(0.3, 1.0), 2),
            "brake": round(random.uniform(0, 0.3), 2),
            "clutch": round(random.uniform(0, 0.2), 2),
            "handbrake": 0.0,
            "stage_progress": round((t % 120) / 120 * 100, 2),
            "lap_time": round(t % 120, 2),
            "suspension_position": {
                "fl": round(random.uniform(-0.05, 0.05), 3),
                "fr": round(random.uniform(-0.05, 0.05), 3),
                "rl": round(random.uniform(-0.05, 0.05), 3),
                "rr": round(random.uniform(-0.05, 0.05), 3)
            }
        }
    
    def get_current_data(self) -> Dict[str, Any]:
        """Get the most recently read telemetry data"""
        return self.current_data if self.current_data else self.read_telemetry()
    
    def close(self):
        """Close shared memory connection"""
        if self.handle and not self._simulation_mode:
            try:
                win32api.CloseHandle(self.handle)
            except:
                pass
