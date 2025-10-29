"""
REST API for RBR Telemetry Connector
Provides HTTP endpoints for accessing telemetry data
"""
from flask import Flask, jsonify, request
from flask_cors import CORS
from typing import Dict, Any, Optional
import threading
import json


class TelemetryAPI:
    """REST API for telemetry data"""
    
    def __init__(self, telemetry_reader, config: Dict[str, Any]):
        self.telemetry_reader = telemetry_reader
        self.config = config
        self.app = Flask(__name__)
        CORS(self.app)  # Enable CORS for MCP access
        
        self._setup_routes()
        self.server_thread: Optional[threading.Thread] = None
    
    def _setup_routes(self):
        """Setup API routes"""
        
        @self.app.route('/api/health', methods=['GET'])
        def health_check():
            """Health check endpoint"""
            return jsonify({
                "status": "ok",
                "service": "RBR Telemetry Connector",
                "version": "1.0.0"
            })
        
        @self.app.route('/api/telemetry', methods=['GET'])
        def get_telemetry():
            """Get current telemetry data"""
            try:
                data = self.telemetry_reader.get_current_data()
                return jsonify(data)
            except Exception as e:
                return jsonify({
                    "error": str(e),
                    "status": "error"
                }), 500
        
        @self.app.route('/api/telemetry/speed', methods=['GET'])
        def get_speed():
            """Get current speed"""
            try:
                data = self.telemetry_reader.get_current_data()
                return jsonify({
                    "speed_kmh": data.get("speed_kmh", 0),
                    "timestamp": data.get("timestamp")
                })
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        
        @self.app.route('/api/telemetry/rpm', methods=['GET'])
        def get_rpm():
            """Get current RPM"""
            try:
                data = self.telemetry_reader.get_current_data()
                return jsonify({
                    "rpm": data.get("rpm", 0),
                    "timestamp": data.get("timestamp")
                })
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        
        @self.app.route('/api/telemetry/position', methods=['GET'])
        def get_position():
            """Get current position"""
            try:
                data = self.telemetry_reader.get_current_data()
                return jsonify({
                    "position": data.get("position", {}),
                    "timestamp": data.get("timestamp")
                })
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        
        @self.app.route('/', methods=['GET'])
        def index():
            """API documentation"""
            return jsonify({
                "service": "RBR Telemetry Connector API",
                "version": "1.0.0",
                "endpoints": {
                    "/api/health": "Health check",
                    "/api/telemetry": "Get all telemetry data",
                    "/api/telemetry/speed": "Get speed data",
                    "/api/telemetry/rpm": "Get RPM data",
                    "/api/telemetry/position": "Get position data"
                }
            })
    
    def start(self):
        """Start API server in a background thread"""
        host = self.config.get("api", {}).get("host", "0.0.0.0")
        port = self.config.get("api", {}).get("port", 8080)
        
        def run_server():
            self.app.run(host=host, port=port, debug=False, use_reloader=False)
        
        self.server_thread = threading.Thread(target=run_server, daemon=True)
        self.server_thread.start()
        print(f"API server started on http://{host}:{port}")
    
    def stop(self):
        """Stop API server"""
        # Flask doesn't have a built-in way to stop gracefully in threading mode
        # The daemon thread will be terminated when main program exits
        pass
