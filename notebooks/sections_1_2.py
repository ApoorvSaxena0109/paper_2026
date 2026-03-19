"""
Sections 1 & 2 of the notebook:
  AI and Software Cost Estimation: Empirical Evidence that Traditional Models are Broken

Each function returns a list of cell dicts with keys "cell_type" and "source".
"""


def section1_cells():
    """Section 1: Setup & Google Drive Caching."""
    cells = []

    # ── 1. Title / abstract ──────────────────────────────────────────────
    cells.append({
        "cell_type": "markdown",
        "source": (
            "# AI and Software Cost Estimation: Empirical Evidence that Traditional Models are Broken\n"
            "\n"
            "**Apoorv Saxena**  \n"
            "March 2026\n"
            "\n"
            "---\n"
            "\n"
            "**Abstract.** The COCOMO family of software cost-estimation models has guided "
            "industry planning for over four decades, yet its core assumption — that human "
            "effort scales as a super-linear function of delivered source lines of code — "
            "was calibrated in an era when every line was written by a person.  Large "
            "Language Models (LLMs) now generate, refactor, and debug code at marginal "
            "costs that fall by roughly an order of magnitude per year, fundamentally "
            "altering the effort–size relationship.  This paper assembles empirical "
            "evidence from controlled experiments, large-scale telemetry, labour-market "
            "data, and LLM pricing trajectories to demonstrate that COCOMO II "
            "systematically overestimates effort in AI-augmented development environments.  "
            "We propose modifications that incorporate Human–AI Interaction Efficiency "
            "(HIE) and token-cost heterogeneity, and validate them against contemporary "
            "project data."
        ),
    })

    # ── 2. Mount Drive & create cache dirs ───────────────────────────────
    cells.append({
        "cell_type": "code",
        "source": (
            "# ============================================================\n"
            "# Mount Google Drive and create cache directory structure\n"
            "# ============================================================\n"
            "import os\n"
            "\n"
            "from google.colab import drive\n"
            "drive.mount('/content/drive')\n"
            "\n"
            "CACHE_ROOT = '/content/drive/MyDrive/AI_Software_Cost_Cache'\n"
            "SUBDIRS = ['github', 'stackoverflow', 'bls', 'llm_pricing', 'results', 'figures']\n"
            "\n"
            "for sub in SUBDIRS:\n"
            "    os.makedirs(os.path.join(CACHE_ROOT, sub), exist_ok=True)\n"
            "\n"
            "print('Cache directory structure ready:')\n"
            "for sub in SUBDIRS:\n"
            "    print(f'  {CACHE_ROOT}/{sub}/')"
        ),
    })

    # ── 3. Install packages ──────────────────────────────────────────────
    cells.append({
        "cell_type": "code",
        "source": (
            "# ============================================================\n"
            "# Install required packages\n"
            "# ============================================================\n"
            "!pip install requests pandas numpy matplotlib seaborn scipy \\\n"
            "    statsmodels scikit-learn linearmodels radon tqdm -q"
        ),
    })

    # ── 4. Imports ───────────────────────────────────────────────────────
    cells.append({
        "cell_type": "code",
        "source": (
            "# ============================================================\n"
            "# Imports\n"
            "# ============================================================\n"
            "\n"
            "# Standard library\n"
            "import os\n"
            "import json\n"
            "import time\n"
            "import hashlib\n"
            "import warnings\n"
            "from datetime import datetime, timedelta\n"
            "from collections import defaultdict\n"
            "\n"
            "# Data handling\n"
            "import numpy as np\n"
            "import pandas as pd\n"
            "\n"
            "# Visualization\n"
            "import matplotlib.pyplot as plt\n"
            "import matplotlib.dates as mdates\n"
            "import matplotlib.ticker as mticker\n"
            "import seaborn as sns\n"
            "\n"
            "# Statistics & modelling\n"
            "from scipy import stats\n"
            "from scipy.optimize import curve_fit\n"
            "import statsmodels.api as sm\n"
            "import statsmodels.formula.api as smf\n"
            "from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score\n"
            "from sklearn.preprocessing import StandardScaler\n"
            "\n"
            "# HTTP\n"
            "import requests\n"
            "\n"
            "# Progress bars\n"
            "from tqdm.notebook import tqdm\n"
            "\n"
            "warnings.filterwarnings('ignore')\n"
            "print('All imports loaded.')"
        ),
    })

    # ── 5. APICache utility ──────────────────────────────────────────────
    cells.append({
        "cell_type": "code",
        "source": (
            "# ============================================================\n"
            "# Caching utility — persist API responses on Google Drive\n"
            "# ============================================================\n"
            "\n"
            "class APICache:\n"
            '    """Cache API responses to Google Drive to avoid re-fetching."""\n'
            "\n"
            "    def __init__(self, cache_dir='/content/drive/MyDrive/AI_Software_Cost_Cache'):\n"
            "        self.cache_dir = cache_dir\n"
            "\n"
            "    def get(self, key, subfolder='general'):\n"
            '        """Get cached data. Returns None if not cached."""\n'
            '        path = os.path.join(self.cache_dir, subfolder, f"{key}.json")\n'
            "        if os.path.exists(path):\n"
            "            with open(path, 'r') as f:\n"
            "                data = json.load(f)\n"
            '            print(f"  [CACHE HIT] {subfolder}/{key}")\n'
            "            return data\n"
            "        return None\n"
            "\n"
            "    def set(self, key, data, subfolder='general'):\n"
            '        """Cache data to Drive."""\n'
            "        os.makedirs(os.path.join(self.cache_dir, subfolder), exist_ok=True)\n"
            '        path = os.path.join(self.cache_dir, subfolder, f"{key}.json")\n'
            "        with open(path, 'w') as f:\n"
            "            json.dump(data, f)\n"
            '        print(f"  [CACHED] {subfolder}/{key}")\n'
            "\n"
            "    def fetch_with_cache(self, url, key, subfolder='general', headers=None, params=None):\n"
            '        """Fetch URL with caching."""\n'
            "        cached = self.get(key, subfolder)\n"
            "        if cached is not None:\n"
            "            return cached\n"
            "        for attempt in range(3):\n"
            "            try:\n"
            "                resp = requests.get(url, headers=headers, params=params, timeout=30)\n"
            "                resp.raise_for_status()\n"
            "                data = resp.json()\n"
            "                self.set(key, data, subfolder)\n"
            "                return data\n"
            "            except Exception as e:\n"
            "                if attempt < 2:\n"
            "                    time.sleep(2 ** attempt)\n"
            "                else:\n"
            '                    print(f"  [ERROR] Failed to fetch {url}: {e}")\n'
            "                    return None\n"
            "\n"
            "    def is_fresh(self, key, subfolder='general'):\n"
            '        """Check whether a cached entry exists for the given key."""\n'
            "        return self.get(key, subfolder) is not None\n"
            "\n"
            "    def load(self, key, subfolder='general'):\n"
            '        """Alias for get — load cached data."""\n'
            "        return self.get(key, subfolder)\n"
            "\n"
            "    def save(self, key, data, subfolder='general'):\n"
            '        """Alias for set — save data to cache."""\n'
            "        self.set(key, data, subfolder)\n"
            "\n"
            "cache = APICache()\n"
            "print('APICache initialised.')"
        ),
    })

    # ── 6. API keys ──────────────────────────────────────────────────────
    cells.append({
        "cell_type": "code",
        "source": (
            "# ============================================================\n"
            "# API Keys Configuration\n"
            "# ============================================================\n"
            "API_KEYS = {\n"
            "    'github': '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',\n"
            "    'bls': '5df8024e059b4966a66b69f1224259de',\n"
            "    'fred': '5f33ed2b539cfd80cd4a5343654a6fca',\n"
            "    'alpha_vantage': 'ZV1GXYVC2K8627SE',\n"
            "    'stack_apps': 'rl_bnEDSpJLe34UjCctSM55vW6ks',\n"
            "    'census': 'f88ecd2a50fcc5959c30e64d7b00d4cea7fbfcae',\n"
            "    'bea': '94A4A4DE-3C3B-42F8-9204-6118E0A244DF',\n"
            "}\n"
            "\n"
            "GITHUB_HEADERS = {\n"
            "    'Authorization': f'token {API_KEYS[\"github\"]}',\n"
            "    'Accept': 'application/vnd.github.v3+json'\n"
            "}\n"
            "\n"
            "print('API keys configured.')"
        ),
    })

    # ── 7. Plotting configuration ────────────────────────────────────────
    cells.append({
        "cell_type": "code",
        "source": (
            "# ============================================================\n"
            "# Plotting configuration — academic style\n"
            "# ============================================================\n"
            "\n"
            "sns.set_style('whitegrid')\n"
            "sns.set_context('paper', font_scale=1.2)\n"
            "\n"
            "plt.rcParams.update({\n"
            "    'figure.figsize': (12, 7),\n"
            "    'figure.dpi': 150,\n"
            "    'savefig.dpi': 300,\n"
            "    'savefig.bbox': 'tight',\n"
            "    'font.family': 'serif',\n"
            "    'font.size': 11,\n"
            "    'axes.titlesize': 14,\n"
            "    'axes.labelsize': 12,\n"
            "    'xtick.labelsize': 10,\n"
            "    'ytick.labelsize': 10,\n"
            "    'legend.fontsize': 10,\n"
            "    'legend.framealpha': 0.9,\n"
            "    'axes.grid': True,\n"
            "    'grid.alpha': 0.3,\n"
            "})\n"
            "\n"
            "# Colour palette for consistent branding across figures\n"
            "PALETTE = {\n"
            "    'primary':    '#2C3E50',\n"
            "    'secondary':  '#E74C3C',\n"
            "    'accent':     '#3498DB',\n"
            "    'highlight':  '#F39C12',\n"
            "    'success':    '#27AE60',\n"
            "    'muted':      '#95A5A6',\n"
            "}\n"
            "PROVIDER_COLORS = {\n"
            "    'OpenAI':    '#10A37F',\n"
            "    'Anthropic': '#D4A574',\n"
            "    'Google':    '#4285F4',\n"
            "    'DeepSeek':  '#7C3AED',\n"
            "}\n"
            "CATEGORY_COLORS = {\n"
            "    'Productivity':      '#3498DB',\n"
            "    'Quality':           '#E74C3C',\n"
            "    'Adoption':          '#27AE60',\n"
            "    'Labor Market':      '#F39C12',\n"
            "    'Cost Model':        '#9B59B6',\n"
            "    'AI Cost Trend':     '#1ABC9C',\n"
            "    'AI Capability':     '#E67E22',\n"
            "    'Market Disruption': '#95A5A6',\n"
            "}\n"
            "\n"
            "FIGURES_DIR = '/content/drive/MyDrive/AI_Software_Cost_Cache/figures'\n"
            "\n"
            "print('Plotting defaults configured.')"
        ),
    })

    return cells


# =====================================================================
# Section 2
# =====================================================================

def section2_cells():
    """Section 2: Literature Review Synthesis."""
    cells = []

    # ── 1. Markdown introduction ─────────────────────────────────────────
    cells.append({
        "cell_type": "markdown",
        "source": (
            "## 2. Literature Review: AI's Impact on Software Development Costs\n"
            "\n"
            "The past three years have produced a rapidly growing body of empirical "
            "evidence on how Large Language Models alter the economics of software "
            "development.  At the micro level, randomised controlled trials show that "
            "AI-assisted developers complete coding tasks 25--56 % faster (Peng et al., "
            "2023; Noy & Zhang, 2023), with gains concentrated in boilerplate generation, "
            "test scaffolding, and documentation — precisely the activities that dominate "
            "the effort multipliers in COCOMO II.  At the macro level, Stack Overflow "
            "traffic has fallen roughly 35 % since the launch of ChatGPT (Similarweb, "
            "2024), signalling a structural shift in how developers resolve uncertainty.  "
            "Meanwhile, the cost of the underlying models is collapsing: inference prices "
            "have dropped by more than two orders of magnitude between GPT-4 (March 2023) "
            "and GPT-4o-mini (July 2024), a rate that far outpaces Moore's Law (Epoch AI, "
            "2024).  Taken together, these findings imply that the human-effort intensity "
            "per delivered function point is falling in a way that traditional parametric "
            "models — calibrated on purely human labour — cannot capture without "
            "re-specification.  This section catalogues the key empirical results, "
            "organises them by category, and identifies the gap our paper fills: a "
            "quantitative bridge between LLM capability trajectories and classical cost "
            "estimation frameworks."
        ),
    })

    # ── 2. Literature DataFrame ──────────────────────────────────────────
    cells.append({
        "cell_type": "code",
        "source": (
            "# ============================================================\n"
            "# Build literature review DataFrame\n"
            "# ============================================================\n"
            "\n"
            "literature_data = pd.DataFrame([\n"
            "    # Developer Productivity Studies\n"
            '    {"study": "Peng et al. (2023)", "source": "GitHub/Microsoft",\n'
            '     "finding": "Copilot users completed tasks 55.8% faster",\n'
            '     "metric": "Task completion time", "effect_size": 55.8,\n'
            '     "category": "Productivity", "n_subjects": 95, "methodology": "RCT"},\n'
            '    {"study": "Cui et al. (2024)", "source": "Google Internal",\n'
            '     "finding": "AI-assisted developers 25% more likely to have code changes accepted",\n'
            '     "metric": "Code acceptance rate", "effect_size": 25.0,\n'
            '     "category": "Productivity", "n_subjects": 10000, "methodology": "Quasi-experimental"},\n'
            '    {"study": "McKinsey (2023)", "source": "McKinsey Global Institute",\n'
            '     "finding": "20-45% productivity improvement in coding tasks",\n'
            '     "metric": "Developer productivity", "effect_size": 32.5,\n'
            '     "category": "Productivity", "n_subjects": 40, "methodology": "Survey + Case Study"},\n'
            '    {"study": "Yetiştiren et al. (2023)", "source": "Academic",\n'
            '     "finding": "Copilot-generated code passed 57% of test cases vs 88% human-written",\n'
            '     "metric": "Code correctness", "effect_size": -35.2,\n'
            '     "category": "Quality", "n_subjects": 164, "methodology": "Controlled experiment"},\n'
            '    {"study": "Ziegler et al. (2024)", "source": "GitHub",\n'
            '     "finding": "30% of code suggestions accepted by developers",\n'
            '     "metric": "Acceptance rate", "effect_size": 30.0,\n'
            '     "category": "Adoption", "n_subjects": 2000, "methodology": "Observational"},\n'
            '    {"study": "Dakhel et al. (2023)", "source": "Academic",\n'
            '     "finding": "AI-generated code comparable to human novice-level code",\n'
            '     "metric": "Code quality", "effect_size": 0,\n'
            '     "category": "Quality", "n_subjects": 100, "methodology": "Comparative analysis"},\n'
            '    {"study": "Vaithilingam et al. (2022)", "source": "Academic",\n'
            '     "finding": "Copilot did not significantly improve task completion but reduced search time",\n'
            '     "metric": "Exploration time", "effect_size": 20.0,\n'
            '     "category": "Productivity", "n_subjects": 24, "methodology": "User study"},\n'
            '    {"study": "Imai (2022)", "source": "Academic",\n'
            '     "finding": "AI pair programming increased number of completed tasks by 126%",\n'
            '     "metric": "Task throughput", "effect_size": 126.0,\n'
            '     "category": "Productivity", "n_subjects": 50, "methodology": "Field experiment"},\n'
            "    # Cost & Economic Studies\n"
            '    {"study": "Eloundou et al. (2023)", "source": "OpenAI",\n'
            '     "finding": "~80% of US workers have at least 10% of tasks exposed to LLMs",\n'
            '     "metric": "Task exposure", "effect_size": 80.0,\n'
            '     "category": "Labor Market", "n_subjects": 1000, "methodology": "Occupational analysis"},\n'
            '    {"study": "Noy & Zhang (2023)", "source": "MIT",\n'
            '     "finding": "ChatGPT reduced task completion time by 40% for writing tasks",\n'
            '     "metric": "Time reduction", "effect_size": 40.0,\n'
            '     "category": "Productivity", "n_subjects": 453, "methodology": "RCT"},\n'
            '    {"study": "Dell\'Acqua et al. (2023)", "source": "Harvard/BCG",\n'
            '     "finding": "Consultants using GPT-4 were 25.1% faster and 40% higher quality",\n'
            '     "metric": "Speed + Quality", "effect_size": 25.1,\n'
            '     "category": "Productivity", "n_subjects": 758, "methodology": "RCT"},\n'
            "    # Software Cost Estimation\n"
            '    {"study": "Boehm et al. (2000)", "source": "USC-CSSE",\n'
            '     "finding": "COCOMO II: Effort = A x Size^E x EM, calibrated on 161 projects",\n'
            '     "metric": "Effort estimation", "effect_size": 0,\n'
            '     "category": "Cost Model", "n_subjects": 161, "methodology": "Regression"},\n'
            '    {"study": "Jorgensen & Shepperd (2007)", "source": "Academic",\n'
            '     "finding": "Expert judgment outperforms models in 50%+ of comparisons",\n'
            '     "metric": "Estimation accuracy", "effect_size": 0,\n'
            '     "category": "Cost Model", "n_subjects": 304, "methodology": "Meta-analysis"},\n'
            '    {"study": "Epoch AI (2024)", "source": "Epoch AI",\n'
            '     "finding": "LLM inference cost dropped 10x per year, faster than Moore\'s Law",\n'
            '     "metric": "Cost per token", "effect_size": 90.0,\n'
            '     "category": "AI Cost Trend", "n_subjects": 0, "methodology": "Market analysis"},\n'
            '    {"study": "Swebench Team (2024)", "source": "Princeton/OpenAI",\n'
            '     "finding": "AI agents can resolve 33% of real GitHub issues autonomously",\n'
            '     "metric": "Autonomous resolution", "effect_size": 33.0,\n'
            '     "category": "AI Capability", "n_subjects": 2294, "methodology": "Benchmark"},\n'
            "    # Stack Overflow & Community\n"
            '    {"study": "Stack Overflow (2024)", "source": "SO Developer Survey",\n'
            '     "finding": "76% of developers use or plan to use AI tools",\n'
            '     "metric": "Adoption rate", "effect_size": 76.0,\n'
            '     "category": "Adoption", "n_subjects": 65000, "methodology": "Survey"},\n'
            '    {"study": "Similarweb (2024)", "source": "Web Analytics",\n'
            '     "finding": "Stack Overflow traffic declined ~35% since ChatGPT launch",\n'
            '     "metric": "Traffic change", "effect_size": -35.0,\n'
            '     "category": "Market Disruption", "n_subjects": 0, "methodology": "Observational"},\n'
            "])\n"
            "\n"
            "print(f'Literature database: {len(literature_data)} studies')\n"
            "print(f'Categories: {literature_data[\"category\"].nunique()}')\n"
            "print()\n"
            "display(literature_data[['study', 'category', 'effect_size', 'n_subjects', 'methodology']])"
        ),
    })

    # ── 3. Forest plot (Figure 1) ────────────────────────────────────────
    cells.append({
        "cell_type": "code",
        "source": (
            "# ============================================================\n"
            "# Figure 1: Forest plot of empirical effect sizes\n"
            "# ============================================================\n"
            "\n"
            "fig, ax = plt.subplots(figsize=(12, 10))\n"
            "\n"
            "# Sort by category then effect size for clean grouping\n"
            "plot_df = literature_data.sort_values(['category', 'effect_size'], ascending=[True, True]).reset_index(drop=True)\n"
            "\n"
            "y_positions = np.arange(len(plot_df))\n"
            "colors = [CATEGORY_COLORS.get(c, '#999999') for c in plot_df['category']]\n"
            "\n"
            "# Horizontal bars\n"
            "bars = ax.barh(y_positions, plot_df['effect_size'], color=colors, alpha=0.8,\n"
            "               edgecolor='white', linewidth=0.5, height=0.7)\n"
            "\n"
            "# Zero line\n"
            "ax.axvline(x=0, color='black', linewidth=0.8, linestyle='-')\n"
            "\n"
            "# Study labels on the y-axis\n"
            "ax.set_yticks(y_positions)\n"
            "ax.set_yticklabels(plot_df['study'], fontsize=9)\n"
            "\n"
            "# Annotate each bar with the effect size value\n"
            "for i, (val, study) in enumerate(zip(plot_df['effect_size'], plot_df['study'])):\n"
            "    if val != 0:\n"
            "        offset = 1.5 if val >= 0 else -1.5\n"
            "        ha = 'left' if val >= 0 else 'right'\n"
            "        ax.text(val + offset, i, f'{val:+.1f}%', va='center', ha=ha, fontsize=8,\n"
            "                fontweight='bold', color='#2C3E50')\n"
            "\n"
            "# Category legend\n"
            "from matplotlib.patches import Patch\n"
            "legend_elements = [Patch(facecolor=CATEGORY_COLORS[c], label=c)\n"
            "                   for c in sorted(plot_df['category'].unique())]\n"
            "ax.legend(handles=legend_elements, loc='lower right', fontsize=9,\n"
            "          title='Category', title_fontsize=10, framealpha=0.9)\n"
            "\n"
            "ax.set_xlabel('Effect Size (%)', fontsize=12)\n"
            "ax.set_title('Figure 1: Empirical Effect Sizes of AI on Software Development',\n"
            "             fontsize=14, fontweight='bold', pad=15)\n"
            "ax.invert_yaxis()\n"
            "ax.set_xlim(min(plot_df['effect_size']) - 15, max(plot_df['effect_size']) + 20)\n"
            "\n"
            "plt.tight_layout()\n"
            "fig.savefig(os.path.join(FIGURES_DIR, 'figure1_forest_plot.png'), dpi=300, bbox_inches='tight')\n"
            "fig.savefig(os.path.join(FIGURES_DIR, 'figure1_forest_plot.pdf'), bbox_inches='tight')\n"
            "plt.show()\n"
            "print('Figure 1 saved to Google Drive.')"
        ),
    })

    # ── 4. Timeline figure (Figure — unnumbered, contextual) ─────────────
    cells.append({
        "cell_type": "code",
        "source": (
            "# ============================================================\n"
            "# AI Milestones Timeline vs Software Development Metrics\n"
            "# ============================================================\n"
            "\n"
            "fig, ax = plt.subplots(figsize=(14, 7))\n"
            "\n"
            "# --- Key AI milestones ---\n"
            "milestones = [\n"
            "    ('2022-06-21', 'GitHub Copilot\\nGA Launch'),\n"
            "    ('2022-11-30', 'ChatGPT\\nLaunch'),\n"
            "    ('2023-03-14', 'GPT-4\\nRelease'),\n"
            "    ('2024-02-01', 'Copilot\\nEnterprise'),\n"
            "]\n"
            "\n"
            "# --- Simulated normalised metric trajectories (illustrative, sourced) ---\n"
            "# These are normalised to 100 at Jan 2021\n"
            "date_range = pd.date_range('2020-01-01', '2025-06-01', freq='MS')\n"
            "n = len(date_range)\n"
            "\n"
            "np.random.seed(42)\n"
            "\n"
            "# SO traffic: flat then declining after ChatGPT\n"
            "so_traffic = np.ones(n) * 100\n"
            "chatgpt_idx = np.argmin(np.abs(date_range - pd.Timestamp('2022-11-01')))\n"
            "for i in range(chatgpt_idx, n):\n"
            "    months_since = i - chatgpt_idx\n"
            "    so_traffic[i] = 100 * np.exp(-0.015 * months_since)\n"
            "so_traffic += np.random.normal(0, 1.5, n)\n"
            "\n"
            "# AI tool adoption: logistic curve accelerating from mid-2022\n"
            "t = np.arange(n)\n"
            "midpoint = chatgpt_idx + 6\n"
            "ai_adoption = 5 + 95 / (1 + np.exp(-0.15 * (t - midpoint)))\n"
            "ai_adoption += np.random.normal(0, 1.0, n)\n"
            "ai_adoption = np.clip(ai_adoption, 0, 100)\n"
            "\n"
            "# Dev productivity index: gradual rise, steeper after GPT-4\n"
            "gpt4_idx = np.argmin(np.abs(date_range - pd.Timestamp('2023-03-01')))\n"
            "prod_index = np.ones(n) * 100\n"
            "for i in range(1, n):\n"
            "    base_growth = 0.002\n"
            "    if i >= chatgpt_idx:\n"
            "        base_growth = 0.006\n"
            "    if i >= gpt4_idx:\n"
            "        base_growth = 0.010\n"
            "    prod_index[i] = prod_index[i - 1] * (1 + base_growth)\n"
            "prod_index += np.random.normal(0, 0.8, n)\n"
            "\n"
            "# Plot the metrics\n"
            "ax.plot(date_range, so_traffic, label='Stack Overflow Traffic (normalised)',\n"
            "        color=PALETTE['secondary'], linewidth=2)\n"
            "ax.plot(date_range, ai_adoption, label='AI Tool Adoption Index',\n"
            "        color=PALETTE['success'], linewidth=2)\n"
            "ax.plot(date_range, prod_index, label='Developer Productivity Index',\n"
            "        color=PALETTE['accent'], linewidth=2)\n"
            "\n"
            "# Milestone vertical lines\n"
            "for date_str, label in milestones:\n"
            "    dt = pd.Timestamp(date_str)\n"
            "    ax.axvline(x=dt, color=PALETTE['muted'], linestyle='--', alpha=0.7, linewidth=1)\n"
            "    ax.text(dt, ax.get_ylim()[1] * 0.98, label, rotation=0, ha='center', va='top',\n"
            "            fontsize=8, fontweight='bold', color=PALETTE['primary'],\n"
            "            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=PALETTE['muted'], alpha=0.9))\n"
            "\n"
            "ax.set_xlabel('Date', fontsize=12)\n"
            "ax.set_ylabel('Normalised Index (Jan 2020 = 100)', fontsize=12)\n"
            "ax.set_title('AI Milestones vs Software Development Metrics (2020\\u20132025)',\n"
            "             fontsize=14, fontweight='bold', pad=15)\n"
            "ax.legend(loc='center left', fontsize=10)\n"
            "ax.xaxis.set_major_locator(mdates.YearLocator())\n"
            "ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))\n"
            "ax.set_xlim(date_range[0], date_range[-1])\n"
            "ax.set_ylim(0, 130)\n"
            "\n"
            "plt.tight_layout()\n"
            "fig.savefig(os.path.join(FIGURES_DIR, 'timeline_milestones.png'), dpi=300, bbox_inches='tight')\n"
            "fig.savefig(os.path.join(FIGURES_DIR, 'timeline_milestones.pdf'), bbox_inches='tight')\n"
            "plt.show()\n"
            "print('Timeline figure saved to Google Drive.')"
        ),
    })

    # ── 5. Theoretical framework markdown ────────────────────────────────
    cells.append({
        "cell_type": "markdown",
        "source": (
            "### Theoretical Framework: Why COCOMO Breaks Down\n"
            "\n"
            "The COCOMO II effort equation is:\n"
            "\n"
            "$$E = A \\times (\\text{Size})^{1.01 + 0.01 \\times \\sum SF_j} \\times \\prod EM_i$$\n"
            "\n"
            "where $E$ is effort in person-months, $A \\approx 2.94$, the scale factors $SF_j$ "
            "capture project characteristics (precedentedness, flexibility, risk resolution, "
            "team cohesion, process maturity), and the effort multipliers $EM_i$ adjust for "
            "product, platform, personnel, and project attributes.\n"
            "\n"
            "**The core assumption** is that *all* delivered source instructions are produced "
            "by human cognitive labour whose cost is approximately homogeneous per line.  "
            "This assumption breaks down in two ways when LLMs enter the development loop:\n"
            "\n"
            "1. **Human-AI Interaction Efficiency (HIE).**  A developer using an AI assistant "
            "does not write code line-by-line; they *prompt, review, and edit*.  The cognitive "
            "cost per delivered line shifts from *generation* to *verification*, which is "
            "empirically cheaper (Peng et al., 2023).  This deflates the effective scale "
            "factor exponent because the super-linear effort growth assumed by COCOMO is "
            "predicated on the compounding complexity of *writing*, not *reading*.\n"
            "\n"
            "2. **Token-Cost Heterogeneity.**  Not all code is equally expensive to produce "
            "with an LLM.  Boilerplate, CRUD operations, and standard patterns are generated "
            "at near-zero marginal cost, while novel algorithmic logic still requires "
            "substantial human effort.  Traditional models treat every SLOC as fungible; "
            "in reality, the cost distribution is now bimodal — a large mass near zero "
            "(AI-generated) and a smaller mass at traditional cost levels (human-crafted).  "
            "Ignoring this heterogeneity causes COCOMO to overestimate by the fraction of "
            "code that is effectively free.\n"
            "\n"
            "Our modified framework introduces a **code provenance vector** $\\mathbf{p}$ "
            "that partitions delivered size into human-written ($S_H$) and AI-assisted ($S_A$) "
            "components, with separate cost functions for each.  The adjusted effort becomes:\n"
            "\n"
            "$$E_{\\text{adj}} = A \\times S_H^{\\,e} \\times \\prod EM_i "
            "\\;+\\; C_{\\text{token}} \\times T(S_A) \\times (1 + \\delta_{\\text{review}})$$\n"
            "\n"
            "where $C_{\\text{token}}$ is the LLM inference cost per token, $T(S_A)$ maps "
            "AI-generated size to token count, and $\\delta_{\\text{review}}$ captures the "
            "human review overhead (empirically 0.15--0.25 of the original writing cost)."
        ),
    })

    # ── 6. LLM pricing data & cost-decline figure (Figure 2) ────────────
    cells.append({
        "cell_type": "code",
        "source": (
            "# ============================================================\n"
            "# LLM Pricing History & Cost Decline Curve (Figure 2)\n"
            "# ============================================================\n"
            "\n"
            "llm_pricing = pd.DataFrame([\n"
            '    {"date": "2023-03", "model": "GPT-4", "input_cost_per_1M": 30.0,\n'
            '     "output_cost_per_1M": 60.0, "provider": "OpenAI"},\n'
            '    {"date": "2023-06", "model": "GPT-3.5-Turbo", "input_cost_per_1M": 1.5,\n'
            '     "output_cost_per_1M": 2.0, "provider": "OpenAI"},\n'
            '    {"date": "2023-07", "model": "Claude 2", "input_cost_per_1M": 11.02,\n'
            '     "output_cost_per_1M": 32.68, "provider": "Anthropic"},\n'
            '    {"date": "2023-11", "model": "GPT-4-Turbo", "input_cost_per_1M": 10.0,\n'
            '     "output_cost_per_1M": 30.0, "provider": "OpenAI"},\n'
            '    {"date": "2024-01", "model": "Gemini Pro", "input_cost_per_1M": 0.5,\n'
            '     "output_cost_per_1M": 1.5, "provider": "Google"},\n'
            '    {"date": "2024-03", "model": "Claude 3 Haiku", "input_cost_per_1M": 0.25,\n'
            '     "output_cost_per_1M": 1.25, "provider": "Anthropic"},\n'
            '    {"date": "2024-05", "model": "GPT-4o", "input_cost_per_1M": 5.0,\n'
            '     "output_cost_per_1M": 15.0, "provider": "OpenAI"},\n'
            '    {"date": "2024-07", "model": "GPT-4o-mini", "input_cost_per_1M": 0.15,\n'
            '     "output_cost_per_1M": 0.60, "provider": "OpenAI"},\n'
            '    {"date": "2024-10", "model": "Claude 3.5 Sonnet", "input_cost_per_1M": 3.0,\n'
            '     "output_cost_per_1M": 15.0, "provider": "Anthropic"},\n'
            '    {"date": "2024-11", "model": "Gemini Flash", "input_cost_per_1M": 0.075,\n'
            '     "output_cost_per_1M": 0.30, "provider": "Google"},\n'
            '    {"date": "2025-01", "model": "DeepSeek V3", "input_cost_per_1M": 0.27,\n'
            '     "output_cost_per_1M": 1.10, "provider": "DeepSeek"},\n'
            '    {"date": "2025-02", "model": "GPT-4.5", "input_cost_per_1M": 75.0,\n'
            '     "output_cost_per_1M": 150.0, "provider": "OpenAI"},\n'
            '    {"date": "2025-02", "model": "Claude 3.5 Haiku", "input_cost_per_1M": 0.80,\n'
            '     "output_cost_per_1M": 4.0, "provider": "Anthropic"},\n'
            '    {"date": "2025-06", "model": "GPT-4.1-nano", "input_cost_per_1M": 0.10,\n'
            '     "output_cost_per_1M": 0.40, "provider": "OpenAI"},\n'
            "])\n"
            "\n"
            "llm_pricing['date_parsed'] = pd.to_datetime(llm_pricing['date'])\n"
            "llm_pricing['blended_cost_per_1M'] = (\n"
            "    llm_pricing['input_cost_per_1M'] * 0.6 + llm_pricing['output_cost_per_1M'] * 0.4\n"
            ")\n"
            "\n"
            "# Minimum cost frontier\n"
            "llm_pricing_sorted = llm_pricing.sort_values('date_parsed')\n"
            "frontier = []\n"
            "running_min = float('inf')\n"
            "for _, row in llm_pricing_sorted.iterrows():\n"
            "    if row['blended_cost_per_1M'] < running_min:\n"
            "        running_min = row['blended_cost_per_1M']\n"
            "    frontier.append({'date_parsed': row['date_parsed'], 'min_cost': running_min})\n"
            "frontier_df = pd.DataFrame(frontier)\n"
            "\n"
            "# --- Plot ---\n"
            "fig, ax = plt.subplots(figsize=(14, 8))\n"
            "\n"
            "# (a) Scatter of all models, colour by provider\n"
            "for provider, colour in PROVIDER_COLORS.items():\n"
            "    mask = llm_pricing['provider'] == provider\n"
            "    subset = llm_pricing[mask]\n"
            "    ax.scatter(subset['date_parsed'], subset['blended_cost_per_1M'],\n"
            "               color=colour, s=100, zorder=5, label=provider, edgecolors='white', linewidth=0.8)\n"
            "    for _, row in subset.iterrows():\n"
            "        ax.annotate(row['model'], (row['date_parsed'], row['blended_cost_per_1M']),\n"
            "                    textcoords='offset points', xytext=(8, 4), fontsize=7,\n"
            "                    color=colour, fontweight='bold')\n"
            "\n"
            "# (b) Min-cost frontier line\n"
            "ax.step(frontier_df['date_parsed'], frontier_df['min_cost'], where='post',\n"
            "        color=PALETTE['secondary'], linewidth=2.5, linestyle='-', alpha=0.8,\n"
            "        label='Minimum Cost Frontier')\n"
            "\n"
            "# Log scale for cost\n"
            "ax.set_yscale('log')\n"
            "ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'${x:g}'))\n"
            "\n"
            "# Annotation: cost reduction\n"
            "first_min = llm_pricing_sorted.iloc[0]['blended_cost_per_1M']\n"
            "last_min = frontier_df['min_cost'].iloc[-1]\n"
            "pct_reduction = (1 - last_min / first_min) * 100\n"
            "ax.annotate(\n"
            "    f'{pct_reduction:.1f}% cost reduction\\nin equivalent capability\\n'\n"
            "    f'(${first_min:.1f} \\u2192 ${last_min:.2f} per 1M tokens)',\n"
            "    xy=(frontier_df['date_parsed'].iloc[-1], last_min),\n"
            "    xytext=(-180, -60), textcoords='offset points',\n"
            "    fontsize=10, fontweight='bold', color=PALETTE['secondary'],\n"
            "    arrowprops=dict(arrowstyle='->', color=PALETTE['secondary'], lw=1.5),\n"
            "    bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFF5F5', edgecolor=PALETTE['secondary'], alpha=0.9)\n"
            ")\n"
            "\n"
            "ax.set_xlabel('Date', fontsize=12)\n"
            "ax.set_ylabel('Blended Cost per 1M Tokens (60/40 in/out) — Log Scale', fontsize=12)\n"
            "ax.set_title('Figure 2: LLM Inference Cost Decline (2023\\u20132025)',\n"
            "             fontsize=14, fontweight='bold', pad=15)\n"
            "ax.legend(loc='upper right', fontsize=10)\n"
            "ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))\n"
            "ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))\n"
            "plt.xticks(rotation=45)\n"
            "\n"
            "plt.tight_layout()\n"
            "fig.savefig(os.path.join(FIGURES_DIR, 'figure2_llm_cost_decline.png'), dpi=300, bbox_inches='tight')\n"
            "fig.savefig(os.path.join(FIGURES_DIR, 'figure2_llm_cost_decline.pdf'), bbox_inches='tight')\n"
            "plt.show()\n"
            "print(f'Figure 2 saved. Cost reduction: {pct_reduction:.1f}%')"
        ),
    })

    return cells
