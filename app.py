from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Resilient Deployment System</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial, sans-serif; background: #0f0f1a; color: white; }
        .header { background: linear-gradient(135deg, #1a1a2e, #16213e); padding: 30px; text-align: center; border-bottom: 2px solid #00d4ff; }
        .header h1 { font-size: 2.5em; color: #00d4ff; }
        .header p { color: #888; margin-top: 10px; }
        .container { max-width: 1100px; margin: 40px auto; padding: 0 20px; }
        .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-bottom: 30px; }
        .card { background: #1a1a2e; border-radius: 12px; padding: 25px; border: 1px solid #2a2a4a; text-align: center; }
        .card .icon { font-size: 2.5em; margin-bottom: 10px; }
        .card h3 { color: #00d4ff; margin-bottom: 8px; }
        .card p { color: #aaa; font-size: 0.9em; }
        .status { display: inline-block; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: bold; }
        .status.green { background: #0d3320; color: #00ff88; border: 1px solid #00ff88; }
        .status.blue { background: #0d1f33; color: #00d4ff; border: 1px solid #00d4ff; }
        .features { background: #1a1a2e; border-radius: 12px; padding: 30px; border: 1px solid #2a2a4a; margin-bottom: 30px; }
        .features h2 { color: #00d4ff; margin-bottom: 20px; }
        .feature-list { display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px; }
        .feature-item { display: flex; align-items: center; gap: 10px; padding: 12px; background: #0f0f1a; border-radius: 8px; }
        .feature-item span { color: #aaa; font-size: 0.9em; }
        .endpoints { background: #1a1a2e; border-radius: 12px; padding: 30px; border: 1px solid #2a2a4a; }
        .endpoints h2 { color: #00d4ff; margin-bottom: 20px; }
        .endpoint { display: flex; align-items: center; gap: 15px; padding: 12px; background: #0f0f1a; border-radius: 8px; margin-bottom: 10px; }
        .method { background: #003366; color: #00d4ff; padding: 4px 10px; border-radius: 5px; font-size: 0.85em; font-weight: bold; }
        .path { color: #00ff88; font-family: monospace; }
        .desc { color: #aaa; font-size: 0.85em; margin-left: auto; }
        .footer { text-align: center; padding: 30px; color: #555; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🚀 Resilient Deployment System</h1>
        <p>Production-grade DevOps + Cybersecurity Infrastructure</p>
        <br>
        <span class="status green">● SYSTEM ONLINE</span>
    </div>

    <div class="container">
        <div class="grid">
            <div class="card">
                <div class="icon">🔄</div>
                <h3>Self-Healing</h3>
                <p>Kubernetes automatically restarts crashed pods</p>
                <br>
                <span class="status green">● Active</span>
            </div>
            <div class="card">
                <div class="icon">📊</div>
                <h3>Monitoring</h3>
                <p>Prometheus + Grafana real-time dashboards</p>
                <br>
                <span class="status green">● Active</span>
            </div>
            <div class="card">
                <div class="icon">🔐</div>
                <h3>Security</h3>
                <p>RBAC + Trivy vulnerability scanning</p>
                <br>
                <span class="status green">● Active</span>
            </div>
            <div class="card">
                <div class="icon">🤖</div>
                <h3>CI/CD Pipeline</h3>
                <p>GitHub Actions auto-deploy on every push</p>
                <br>
                <span class="status green">● Active</span>
            </div>
            <div class="card">
                <div class="icon">🐳</div>
                <h3>Docker</h3>
                <p>Containerized Flask application</p>
                <br>
                <span class="status green">● Running</span>
            </div>
            <div class="card">
                <div class="icon">☁️</div>
                <h3>Cloud Ready</h3>
                <p>Designed for GKE + EKS deployment</p>
                <br>
                <span class="status blue">● GKE Ready</span>
            </div>
        </div>

        <div class="features">
            <h2>⚙️ Project Features</h2>
            <div class="feature-list">
                <div class="feature-item">✅ <span>2 Kubernetes replicas with load balancing</span></div>
                <div class="feature-item">✅ <span>Automatic pod restart on failure</span></div>
                <div class="feature-item">✅ <span>Prometheus alerting rules configured</span></div>
                <div class="feature-item">✅ <span>Trivy Docker image security scanning</span></div>
                <div class="feature-item">✅ <span>Kubernetes RBAC access control</span></div>
                <div class="feature-item">✅ <span>GitHub Actions CI/CD pipeline</span></div>
                <div class="feature-item">✅ <span>Real-time Grafana dashboards</span></div>
                <div class="feature-item">✅ <span>Professional README documentation</span></div>
            </div>
        </div>

        <div class="endpoints">
            <h2>🌐 API Endpoints</h2>
            <div class="endpoint">
                <span class="method">GET</span>
                <span class="path">/</span>
                <span class="desc">Main dashboard — this page</span>
            </div>
            <div class="endpoint">
                <span class="method">GET</span>
                <span class="path">/health</span>
                <span class="desc">Health check endpoint for Kubernetes</span>
            </div>
            <div class="endpoint">
                <span class="method">GET</span>
                <span class="path">/crash</span>
                <span class="desc">Simulate crash — triggers self-healing</span>
            </div>
        </div>
    </div>

    <div class="footer">
        <p>Built by ZorawarSinghKhan | Resilient Deployment System | Kubernetes + Docker + Prometheus + GitHub Actions</p>
    </div>
</body>
</html>
'''

@app.route('/health')
def health():
    return jsonify({"status": "OK", "message": "App is healthy"})

@app.route('/crash')
def crash():
    os._exit(1)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
