from prometheus_client import start_http_server, Gauge, MetricsHandler
from http.server import HTTPServer
import requests
import time
import threading

# Define metrics
API_LATENCY = Gauge('api_latency_seconds', 'API response latency in seconds', ['api_name'])
API_UP = Gauge('api_up', 'API availability (1=up, 0=down)', ['api_name'])
API_STATUS_CODE = Gauge('api_status_code', 'HTTP status code returned by API', ['api_name'])

# List of APIs to monitor
API_ENDPOINTS = {
    'GitHub': 'https://api.github.com',

    'OpenWeatherMap': 'https://api.openweathermap.org/data/2.5/weather?q=London&appid=dea769fd19014ce280b666fe2a0ff4b5',
    'JSONPlaceholder': 'https://jsonplaceholder.typicode.com/posts',
    'HTTPBin': 'https://httpbin.org/get',
    'CoinGecko': 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd',
    'NewsAPI': 'https://newsapi.org/v2/top-headlines?country=us&apiKey=c739269cb5184c5d928d23fa3183dab8',
    'StackExchange': 'https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow',
    'DockerHub': 'https://hub.docker.com/v2/repositories/library/python/',
    'HackerNews': 'https://hacker-news.firebaseio.com/v0/topstories.json'
}

def check_apis():
    """Check all APIs and update metrics"""
    headers = {'User-Agent': 'API-Monitor/1.0'}
    
    for name, url in API_ENDPOINTS.items():
        try:
            start_time = time.time()
            response = requests.get(url, timeout=15, headers=headers)
            latency = time.time() - start_time

            # Update metrics
            API_STATUS_CODE.labels(api_name=name).set(response.status_code)
            API_LATENCY.labels(api_name=name).set(latency)
            
            if response.status_code == 200:
                API_UP.labels(api_name=name).set(1)
                status = "UP"
            else:
                API_UP.labels(api_name=name).set(0)
                status = "DOWN"

            print(f"[{time.strftime('%H:%M:%S')}] {name}: {status} | Status: {response.status_code} | Latency: {latency:.3f}s")

        except requests.exceptions.ConnectionError:
            API_UP.labels(api_name=name).set(0)
            API_LATENCY.labels(api_name=name).set(0)
            API_STATUS_CODE.labels(api_name=name).set(0)
            print(f"[{time.strftime('%H:%M:%S')}] {name}: DOWN | Connection Error")
        except requests.exceptions.Timeout:
            API_UP.labels(api_name=name).set(0)
            API_LATENCY.labels(api_name=name).set(0)
            API_STATUS_CODE.labels(api_name=name).set(0)
            print(f"[{time.strftime('%H:%M:%S')}] {name}: DOWN | Timeout")
        except Exception as e:
            API_UP.labels(api_name=name).set(0)
            API_LATENCY.labels(api_name=name).set(0)
            API_STATUS_CODE.labels(api_name=name).set(0)
            print(f"[{time.strftime('%H:%M:%S')}] {name}: DOWN | {type(e).__name__}")

def monitor_loop():
    """Main monitoring loop"""
    while True:
        check_apis()
        print("-" * 60)
        time.sleep(45)  # Check every 45 seconds

class CORSMetricsHandler(MetricsHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

if __name__ == "__main__":
    # Start Prometheus HTTP server with CORS support
    httpd = HTTPServer(('localhost', 8080), CORSMetricsHandler)
    server_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    server_thread.start()
    
    print("🚀 API Monitor Exporter started!")
    print("📊 Metrics available at: http://localhost:8080/metrics")
    print("🔄 Checking APIs every 30 seconds...")
    print("=" * 60)
    
    # Run initial check
    check_apis()
    print("-" * 60)
    
    # Start monitoring in background thread
    monitor_thread = threading.Thread(target=monitor_loop, daemon=True)
    monitor_thread.start()
    
    try:
        # Keep main thread alive
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Shutting down API Monitor...")