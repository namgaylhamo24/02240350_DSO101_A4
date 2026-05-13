# 02240350_DSO101_A4
# CI/CD Pipeline — Flask + GitHub Actions + Render

A complete DevOps pipeline with **Build → Test → Deploy** automation.

---

## 📂 Project Structure

```
project/
├── app.py                        # Flask backend application
├── test_app.py                   # pytest unit tests
├── requirements.txt              # Python dependencies
├── render.yaml                   # Render deployment config
└── .github/
    └── workflows/
        └── ci.yml                # GitHub Actions CI/CD pipeline
```

---

## 🚀 Quick Start (Local)

```bash
# 1. Clone the repo
git clone https://github.com/namgaylhamo24/02240350_DSO101_A4.git
cd 02240350_DSO101_A4

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py
# → Visit http://localhost:5000

# 4. Run tests
pytest test_app.py -v
```

---

## 🌐 API Endpoints

| Method | Endpoint        | Description               |
|--------|-----------------|---------------------------|
| GET    | `/`             | Welcome message + status  |
| GET    | `/health`       | Health check (200 OK)     |
| GET    | `/add/<a>/<b>`  | Add two integers          |

**Example:**
```
GET /add/3/7  →  {"result": 10}
```

---

## 🔄 CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/ci.yml`) triggers on every push to `main`:

| Step | Action |
|------|--------|
| **Checkout** | Pull latest code |
| **Setup Python** | Configure Python 3.9 |
| **Cache** | Cache pip packages for speed |
| **Install** | `pip install -r requirements.txt` |
| **Test** | `pytest test_app.py -v` |
| **Deploy** | POST to Render deploy API |

---

## ☁️ Deploy to Render

### One-time setup

1. Create a **Web Service** on [render.com](https://render.com) pointing to your GitHub repo.
2. Set the **Build Command**: `pip install -r requirements.txt`
3. Set the **Start Command**: `gunicorn app:app`
4. Copy your **Service ID** and generate an **API Key** from Render dashboard.

### Add GitHub Secrets

In your GitHub repo → **Settings → Secrets → Actions**, add:

| Secret Name         | Value                          |
|---------------------|--------------------------------|
| `RENDER_API_KEY`    | Your Render API key            |
| `RENDER_SERVICE_ID` | Your Render service ID (`srv-...`) |

After this, every push to `main` automatically deploys to Render. ✅

---

## 🧪 Tests

```
test_app.py::test_home               PASSED  (1+1==2 arithmetic check)
test_app.py::test_home_route         PASSED  (GET / returns 200)
test_app.py::test_health_route       PASSED  (GET /health returns healthy)
test_app.py::test_add_route          PASSED  (3+7=10)
test_app.py::test_add_negative_numbers  PASSED  (-5+3=-2)
test_app.py::test_add_zeros          PASSED  (0+0=0)
```

---

## 📊 Marking Criteria Coverage

| Criteria               | Implementation |
|------------------------|----------------|
| Project structure      | Flat layout with all required files |
| CI pipeline (build+test) | GitHub Actions with install + pytest steps |
| Test implementation    | 6 pytest tests covering all routes |
| Deployment automation  | Render API deploy triggered on push to main |
| Documentation          | This README |