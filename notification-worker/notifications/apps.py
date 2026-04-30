from django.apps import AppConfig

class NotificationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notifications'

    def ready(self):
        import requests
        try:
            requests.put('http://consul:8500/v1/agent/service/register', json={
                "Name": "notification-worker",
                "ID":   "notification-worker-1",
                "Port": 8084,
                "Check": {
                    "HTTP":     "http://notification_worker:8084/health/",
                    "Interval": "10s",
                    "Timeout":  "3s"
                }
            }, timeout=3)
            print("[✓] Service enregistré dans Consul")
        except Exception as e:
            print(f"[!] Consul non disponible : {e}")