"""
GUI Dashboard for RBR Telemetry Connector
Displays real-time telemetry data
"""
import tkinter as tk
from tkinter import ttk, font
from typing import Dict, Any
import threading


class TelemetryGUI:
    """GUI Dashboard for telemetry display"""
    
    def __init__(self, telemetry_reader, config: Dict[str, Any]):
        self.telemetry_reader = telemetry_reader
        self.config = config
        self.running = False
        self.update_interval = config.get("telemetry", {}).get("update_frequency_ms", 50)
        
        # Create main window
        self.root = tk.Tk()
        self.root.title(config.get("gui", {}).get("window_title", "RBR Telemetry Connector"))
        self.root.geometry(f"{config.get('gui', {}).get('window_width', 800)}x"
                          f"{config.get('gui', {}).get('window_height', 600)}")
        
        # Configure style
        self._setup_style()
        
        # Create UI elements
        self._create_widgets()
        
        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def _setup_style(self):
        """Setup visual style"""
        style = ttk.Style()
        
        # Try to use a modern theme
        try:
            style.theme_use('clam')
        except:
            pass
        
        # Configure colors for dark theme
        bg_color = "#2b2b2b"
        fg_color = "#ffffff"
        accent_color = "#4a9eff"
        
        self.root.configure(bg=bg_color)
        
        # Configure ttk styles
        style.configure("Title.TLabel", 
                       background=bg_color, 
                       foreground=accent_color,
                       font=('Arial', 16, 'bold'))
        
        style.configure("Data.TLabel", 
                       background=bg_color, 
                       foreground=fg_color,
                       font=('Arial', 12))
        
        style.configure("Value.TLabel", 
                       background=bg_color, 
                       foreground=accent_color,
                       font=('Arial', 14, 'bold'))
        
        style.configure("TFrame", background=bg_color)
    
    def _create_widgets(self):
        """Create GUI widgets"""
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, 
                               text="RBR Telemetry Dashboard", 
                               style="Title.TLabel")
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Create data display sections
        row = 1
        
        # Speed section
        ttk.Label(main_frame, text="Speed:", style="Data.TLabel").grid(
            row=row, column=0, sticky=tk.W, pady=5)
        self.speed_label = ttk.Label(main_frame, text="0.0 km/h", style="Value.TLabel")
        self.speed_label.grid(row=row, column=1, sticky=tk.E, pady=5)
        row += 1
        
        # RPM section
        ttk.Label(main_frame, text="RPM:", style="Data.TLabel").grid(
            row=row, column=0, sticky=tk.W, pady=5)
        self.rpm_label = ttk.Label(main_frame, text="0", style="Value.TLabel")
        self.rpm_label.grid(row=row, column=1, sticky=tk.E, pady=5)
        row += 1
        
        # Gear section
        ttk.Label(main_frame, text="Gear:", style="Data.TLabel").grid(
            row=row, column=0, sticky=tk.W, pady=5)
        self.gear_label = ttk.Label(main_frame, text="N", style="Value.TLabel")
        self.gear_label.grid(row=row, column=1, sticky=tk.E, pady=5)
        row += 1
        
        # Separator
        ttk.Separator(main_frame, orient='horizontal').grid(
            row=row, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        row += 1
        
        # Position section
        ttk.Label(main_frame, text="Position:", style="Data.TLabel").grid(
            row=row, column=0, sticky=tk.W, pady=5)
        self.position_label = ttk.Label(main_frame, text="X: 0.0, Y: 0.0, Z: 0.0", 
                                       style="Value.TLabel")
        self.position_label.grid(row=row, column=1, sticky=tk.E, pady=5)
        row += 1
        
        # Steering section
        ttk.Label(main_frame, text="Steering:", style="Data.TLabel").grid(
            row=row, column=0, sticky=tk.W, pady=5)
        self.steering_label = ttk.Label(main_frame, text="0.0°", style="Value.TLabel")
        self.steering_label.grid(row=row, column=1, sticky=tk.E, pady=5)
        row += 1
        
        # Separator
        ttk.Separator(main_frame, orient='horizontal').grid(
            row=row, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        row += 1
        
        # Throttle section
        ttk.Label(main_frame, text="Throttle:", style="Data.TLabel").grid(
            row=row, column=0, sticky=tk.W, pady=5)
        self.throttle_label = ttk.Label(main_frame, text="0%", style="Value.TLabel")
        self.throttle_label.grid(row=row, column=1, sticky=tk.E, pady=5)
        row += 1
        
        # Brake section
        ttk.Label(main_frame, text="Brake:", style="Data.TLabel").grid(
            row=row, column=0, sticky=tk.W, pady=5)
        self.brake_label = ttk.Label(main_frame, text="0%", style="Value.TLabel")
        self.brake_label.grid(row=row, column=1, sticky=tk.E, pady=5)
        row += 1
        
        # Separator
        ttk.Separator(main_frame, orient='horizontal').grid(
            row=row, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        row += 1
        
        # Stage progress section
        ttk.Label(main_frame, text="Stage Progress:", style="Data.TLabel").grid(
            row=row, column=0, sticky=tk.W, pady=5)
        self.progress_label = ttk.Label(main_frame, text="0%", style="Value.TLabel")
        self.progress_label.grid(row=row, column=1, sticky=tk.E, pady=5)
        row += 1
        
        # Lap time section
        ttk.Label(main_frame, text="Lap Time:", style="Data.TLabel").grid(
            row=row, column=0, sticky=tk.W, pady=5)
        self.laptime_label = ttk.Label(main_frame, text="0:00.00", style="Value.TLabel")
        self.laptime_label.grid(row=row, column=1, sticky=tk.E, pady=5)
        row += 1
        
        # Status label at bottom
        self.status_label = ttk.Label(main_frame, 
                                     text="Status: Waiting for telemetry...", 
                                     style="Data.TLabel")
        self.status_label.grid(row=row+1, column=0, columnspan=2, pady=(20, 0))
        
        # Configure column weights
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
    
    def _update_display(self):
        """Update display with latest telemetry data"""
        if not self.running:
            return
        
        try:
            # Read telemetry data
            data = self.telemetry_reader.read_telemetry()
            
            # Update labels
            self.speed_label.config(text=f"{data.get('speed_kmh', 0):.1f} km/h")
            self.rpm_label.config(text=f"{int(data.get('rpm', 0))}")
            
            gear = data.get('gear', 0)
            gear_text = "N" if gear == 0 else ("R" if gear < 0 else str(gear))
            self.gear_label.config(text=gear_text)
            
            pos = data.get('position', {})
            self.position_label.config(
                text=f"X: {pos.get('x', 0):.1f}, Y: {pos.get('y', 0):.1f}, Z: {pos.get('z', 0):.1f}")
            
            self.steering_label.config(text=f"{data.get('steering_angle', 0):.1f}°")
            
            throttle_pct = int(data.get('throttle', 0) * 100)
            self.throttle_label.config(text=f"{throttle_pct}%")
            
            brake_pct = int(data.get('brake', 0) * 100)
            self.brake_label.config(text=f"{brake_pct}%")
            
            self.progress_label.config(text=f"{data.get('stage_progress', 0):.1f}%")
            
            lap_time = data.get('lap_time', 0)
            minutes = int(lap_time // 60)
            seconds = lap_time % 60
            self.laptime_label.config(text=f"{minutes}:{seconds:05.2f}")
            
            self.status_label.config(text=f"Status: Connected - {data.get('timestamp', '')}")
            
        except Exception as e:
            self.status_label.config(text=f"Status: Error - {str(e)}")
        
        # Schedule next update
        if self.running:
            self.root.after(self.update_interval, self._update_display)
    
    def start(self):
        """Start the GUI"""
        self.running = True
        # Start update loop
        self.root.after(100, self._update_display)
        # Run main loop
        self.root.mainloop()
    
    def on_closing(self):
        """Handle window close event"""
        self.running = False
        self.root.destroy()
