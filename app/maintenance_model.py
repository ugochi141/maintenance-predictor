from sklearn.ensemble import RandomForestClassifier
import numpy as np
from datetime import datetime, timedelta

class MaintenancePredictor:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100)
        self.equipment_database = {}
        
    def predict_failure(self, equipment_id, usage_hours, error_count, last_maintenance):
        """Predict probability of equipment failure"""
        features = [
            usage_hours,
            error_count,
            (datetime.now() - last_maintenance).days,
            self.get_equipment_age(equipment_id)
        ]
        
        failure_probability = self.model.predict_proba([features])[0][1]
        
        return {
            "equipment_id": equipment_id,
            "failure_probability": failure_probability,
            "risk_level": "HIGH" if failure_probability > 0.7 else "MEDIUM" if failure_probability > 0.4 else "LOW",
            "recommended_action": self.get_recommendation(failure_probability)
        }
    
    def get_equipment_age(self, equipment_id):
        """Calculate equipment age in days"""
        # Would fetch from database
        return 365  # Placeholder
    
    def get_recommendation(self, probability):
        """Get maintenance recommendation based on failure probability"""
        if probability > 0.7:
            return "Schedule immediate preventive maintenance"
        elif probability > 0.4:
            return "Schedule maintenance within 1 week"
        else:
            return "Continue monitoring"
    
    def schedule_maintenance(self, equipment_id, priority):
        """Schedule maintenance based on priority"""
        schedule = {
            "HIGH": datetime.now() + timedelta(days=1),
            "MEDIUM": datetime.now() + timedelta(days=7),
            "LOW": datetime.now() + timedelta(days=30)
        }
        
        return {
            "equipment_id": equipment_id,
            "scheduled_date": schedule.get(priority, schedule["MEDIUM"]),
            "estimated_downtime": "2 hours"
        }
