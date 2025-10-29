# 🚀 API Reliability Monitor with Prometheus

A custom Prometheus exporter that monitors API uptime and response times for multiple public APIs.

## 🏗️ Architecture

```
[Python Exporter] → [Prometheus Server] → [Dashboard/Grafana]
        |                    |                    |
  Pings APIs every 30s   Scrapes metrics    Visualizes data
  Exposes on :8000       every 15s          Real-time charts
```

## 📊 Monitored APIs

- **GitHub API**: `https://api.github.com`
- **Weather API**: `https://api.open-meteo.com`
- **HTTPBin**: `https://httpbin.org/get`
- **JSONPlaceholder**: `https://jsonplaceholder.typicode.com`

## 🚀 Quick Start

### Method 1: Using Batch Scripts (Recommended)

1. **Start API Monitor**:
   ```cmd
   start_api_monitor.bat
   ```

2. **Start Prometheus** (in new terminal):
   ```cmd
   start_prometheus.bat
   ```

### Method 2: Manual Commands

1. **Install dependencies**:
   ```cmd
   pip install -r requirements.txt
   ```

2. **Start API Monitor**:
   ```cmd
   python api_monitor.py
   ```

3. **Start Prometheus**:
   ```cmd
   prometheus.exe --config.file=prometheus.yml
   ```

## 🔗 Access Points

- **API Metrics**: http://localhost:8000/metrics
- **Simple Dashboard**: Open `api_dashboard.html` in browser
- **Prometheus UI**: http://localhost:9090
- **Targets Status**: http://localhost:9090/targets

## 📈 Key Metrics

- `api_up`: API availability (1=up, 0=down)
- `api_latency_seconds`: Response time in seconds
- `api_status_code`: HTTP status code returned

## 🔍 Prometheus Queries

Try these queries in Prometheus UI:

```promql
# Average latency by API
avg(api_latency_seconds) by (api_name)

# API uptime percentage
avg_over_time(api_up[5m]) * 100

# APIs currently down
api_up == 0

# High latency APIs (>1 second)
api_latency_seconds > 1
```

## 📊 Sample Dashboard Panels

1. **API Status Overview** (Stat panel)
2. **Response Time Trends** (Time series)
3. **Uptime Percentage** (Gauge)
4. **Status Code Distribution** (Pie chart)

## 🛠️ Customization

Edit `api_monitor.py` to:
- Add more APIs to monitor
- Change check intervals
- Add custom metrics
- Modify timeout values

## 📝 Project Report Structure

1. **Abstract**: API monitoring system overview
2. **Introduction**: Need for API reliability tracking
3. **Architecture**: System components and data flow
4. **Implementation**: Code explanation and metrics
5. **Results**: Screenshots and performance data
6. **Conclusion**: Benefits and future improvements

## 🔧 Troubleshooting

- **Port conflicts**: Check if ports 8000/9090 are free
- **Python errors**: Ensure Python 3.7+ is installed
- **Network issues**: Check internet connectivity for API calls
- **Metrics not showing**: Verify Prometheus is scraping correctly

## 📈 Expected Results

| API | Avg Latency | Uptime % |
|-----|-------------|----------|
| GitHub | ~200ms | 99.9% |
| Weather | ~500ms | 99.5% |
| HTTPBin | ~300ms | 99.8% |
| JSONPlaceholder | ~250ms | 99.7% |