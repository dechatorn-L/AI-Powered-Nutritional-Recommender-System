/**
 * NutriSavor AI - Intelligent Culinary Nutrition & Health Analytics
 * Handcrafted Frontend Controller & Data Visualization Layer
 */

// ==========================================
// 1. NATURAL BILINGUAL DICTIONARY (TH / EN)
// ==========================================
const I18N = {
  th: {
    appSubtitle: "ระบบค้นหาและวิเคราะห์คุณค่าโภชนาการอาหารด้วย AI อัจฉริยะ",
    tabSearch: "ค้นหาเมนูใกล้เคียง",
    tabTarget: "จัดเมนูตามเป้าหมาย",
    tabGrade: "ทดสอบเกรดอาหาร",
    tabPca: "แผนที่สารอาหาร 2D",
    tabEval: "สถิติโมเดล AI",
    tabExplorer: "คลังข้อมูลเมนูอาหาร",

    // Tab 1: Similarity
    searchContextTag: "ระบบจับคู่คุณค่าโภชนาการ (Nutritional Matcher)",
    searchHeading: "ค้นหาเมนูอาหารที่ใกล้เคียงและดีต่อสุขภาพ",
    searchDesc: "เลือกเมนูโปรดของคุณ เพื่อค้นหาเมนูที่มีสัดส่วนสารอาหารใกล้เคียง แคลอรี่เหมาะสม และมีเกรดสุขภาพ Nutri-Grade ที่ช่วยให้คุณคุมอาหารได้อร่อยไม่น่าเบื่อ",
    topKLabel: "จำนวนผลลัพธ์:",
    btnSearch: "ค้นหาเมนูใกล้เคียง",
    quickSuggestions: "เมนูยอดนิยมแนะนำ:",
    btnBrowseCatalog: "ดูเมนูทั้งหมด (1,014 รายการ)",
    targetDishBadge: "เมนูอ้างอิงต้นทาง",
    nrfScore: "ดัชนี NRF 5.3",
    calories: "พลังงาน",
    protein: "โปรตีน",
    carbs: "คาร์บ",
    fats: "ไขมัน",
    macroRatioTitle: "สัดส่วนพลังงาน (% Calorie Split)",
    radarComparisonTitle: "สัดส่วนสารอาหารสำคัญ (% Daily Value)",
    radarComparisonSub: "เปรียบเทียบวิตามิน แร่ธาตุ และสารอาหารหลักกับเมนูแนะนำอันดับ 1",
    recsHeading: "เมนูที่มีคุณค่าโภชนาการใกล้เคียงที่สุด",
    recsSub: "จัดอันดับตามความใกล้เคียงของสารอาหาร 11 มิติและแคลอรี่",

    // Tab 2: Target Optimizer
    targetContextTag: "จัดสูตรอาหารตามเป้าหมาย (Dietary Goal Solver)",
    targetHeading: "กำหนดเป้าหมายสารอาหารเพื่อหาเมนูที่ตรงใจ",
    targetDesc: "ปรับเลื่อนสารอาหารที่คุณต้องการในแต่ละมื้อ ระบบจะค้นหาเมนูอาหารจริงในฐานข้อมูลที่ให้สารอาหารตรงกับความต้องการของคุณมากที่สุด",
    presetGoalsLabel: "เป้าหมายยอดนิยม:",
    lblCalories: "พลังงานรวม (Calories)",
    lblProtein: "โปรตีน (Protein)",
    lblCarbs: "คาร์โบไฮเดรต (Carbohydrates)",
    lblFats: "ไขมันรวม (Total Fats)",
    lblSugar: "น้ำตาลอิสระ (Free Sugar)",
    lblSodium: "โซเดียม (Sodium)",
    lblFibre: "ใยอาหาร (Fibre)",
    btnFindMatches: "ค้นหาเมนูที่ตรงกับเป้าหมาย",
    targetMatchesHeading: "เมนูที่ตรงกับเป้าหมายสารอาหารของคุณ",
    targetMatchesSub: "เรียงตามความสอดคล้องกับสารอาหารที่คุณกำหนด",

    // Tab 3: Nutri-Grade AI
    gradeContextTag: "ห้องทดลองวินิจฉัยสุขภาพอาหาร (Nutri-Grade AI Lab)",
    gradeHeading: "ทดสอบคำนวณ Nutri-Grade ของเมนูอาหาร",
    gradeDesc: "จำลองสัดส่วนสารอาหารเพื่อประเมินเกรดสุขภาพ (Grade A/B/C) ด้วย Random Forest Classifier พร้อมตรวจสอบความสมดุลของพลังงานด้วย Atwater Energy Balance",
    gradeFormTitle: "สัดส่วนสารอาหารในสูตร",
    gradeFormDesc: "ระบุปริมาณสารอาหารจำกัดและสารอาหารหลักต่อ 1 ที่",
    gradePresetsLabel: "กรณีทดสอบมาตรฐาน:",
    btnPredictGrade: "ประมวลผลการจัดเกรด AI",
    readyToPredict: "ระบบพร้อมคำนวณเกรด",
    readyToPredictSub: "กดปุ่ม 'ประมวลผลการจัดเกรด AI' เพื่อดูผลลัพธ์และคำแนะนำ",
    predictedGradeLabel: "เกรดสุขภาพที่ประเมินได้",
    atwaterTitle: "การตรวจสอบสมดุลพลังงาน (Atwater Balance)",
    classProbabilities: "ความน่าจะเป็นของการจัดเกรดแต่ละระดับ",
    dietaryGuidanceTitle: "คำแนะนำทางโภชนาการ",

    // Tab 4: 2D PCA Map
    pcaContextTag: "การจัดกลุ่มอาหาร 5 คลัสเตอร์ (Food Clusters)",
    pcaHeading: "แผนภาพความสัมพันธ์ของสารอาหาร 2 มิติ (2D PCA)",
    pcaDesc: "ลดมิติข้อมูลสารอาหาร 11 มิติ สู่พิกัด 2 มิติ เพื่อแสดงให้เห็นการจัดกลุ่มตามธรรมชาติของอาหาร 1,014 ชนิด",

    // Tab 5: Model Analytics
    evalContextTag: "สถิติและการประเมินประสิทธิภาพ (Model Benchmarks)",
    evalHeading: "รายงานความแม่นยำของโมเดล Machine Learning",
    evalDesc: "ผลการทดสอบความแม่นยำของ Random Forest Classifier บนชุดข้อมูลทดสอบจริงแบบ Stratified 80/20",
    metricAccuracy: "ความแม่นยำรวม (Accuracy)",
    metricMacroF1: "Macro F1-Score",
    metricTestSamples: "จำนวนตัวอย่างทดสอบ",
    metricTrees: "จำนวน Decision Trees",
    metricAccSub: "ทดสอบกับ 20% ของข้อมูลที่ไม่เคยเห็น",
    metricF1Sub: "ค่าเฉลี่ยสมดุลทุกคลาส",
    metricSampleSub: "รายการอาหารที่นำมาประเมิน",
    metricTreesSub: "โครงสร้าง Random Forest",
    cmHeading: "ตาราง Confusion Matrix",
    cmCaption: "เปรียบเทียบเกรดจริงกับเกรดที่ AI ทำนาย",
    featImpHeading: "สารอาหารที่มีผลต่อการจัดเกรดมากที่สุด",
    featImpCaption: "น้ำหนักความสำคัญของสารอาหาร (Gini Importance)",

    // Tab 6: Dataset Explorer
    explorerContextTag: "คลังข้อมูลสูตรอาหาร (Recipe Database)",
    explorerHeading: "ค้นหาข้อมูลโภชนาการในคลังสูตรอาหาร",
    explorerDesc: "สำรวจรายการอาหาร 1,014 เมนู พร้อมคะแนน NRF 5.3 และเกรดสุขภาพ Nutri-Grade ครบถ้วน",
    thDishName: "ชื่อเมนูอาหาร",
    thCategory: "กลุ่มสารอาหาร (Cluster)",
    thGrade: "เกรด",
    thNRF: "NRF 5.3",
    thCalories: "พลังงาน (kcal)",
    thProtein: "โปรตีน (g)",
    thCarbs: "คาร์บ (g)",
    thFats: "ไขมัน (g)",
    thSugar: "น้ำตาล (g)",
    thSodium: "โซเดียม (mg)",
    btnPrev: "ย้อนกลับ",
    btnNext: "ถัดไป",

    // Modal
    modalCatalogTitle: "คลังเมนูอาหารทั้งหมด (1,014 รายการ)",
    modalCatalogSub: "คลิกเลือกเมนูที่ต้องการ เพื่อนำไปวิเคราะห์และหาเมนูที่ใกล้เคียงทันที",
    btnClose: "ปิดหน้าต่าง"
  },
  en: {
    appSubtitle: "Intelligent Culinary Nutrition & Health Analytics",
    tabSearch: "Dish Similarity",
    tabTarget: "Target Optimizer",
    tabGrade: "Nutri-Grade AI",
    tabPca: "2D Food Map",
    tabEval: "Model Analytics",
    tabExplorer: "Recipe Catalog",

    // Tab 1: Similarity
    searchContextTag: "Culinary Vector Matching Engine",
    searchHeading: "Find Healthier & Nutritionally Matched Meals",
    searchDesc: "Select your favorite dish to discover delicious alternatives with comparable macronutrients, balanced calories, and verified Nutri-Grades.",
    topKLabel: "Show:",
    btnSearch: "Find Matches",
    quickSuggestions: "Popular Inspirations:",
    btnBrowseCatalog: "Browse All Dishes (1,014)",
    targetDishBadge: "Reference Baseline Dish",
    nrfScore: "NRF 5.3 Score",
    calories: "Energy",
    protein: "Protein",
    carbs: "Carbs",
    fats: "Fats",
    macroRatioTitle: "Calorie Distribution (% kcal)",
    radarComparisonTitle: "Nutrient Profile (% Daily Value)",
    radarComparisonSub: "Comparing micronutrient and macronutrient densities with top recommendation",
    recsHeading: "Ranked Nutritional Matches",
    recsSub: "Dishes with closest nutrient vector profile and caloric alignment",

    // Tab 2: Target Optimizer
    targetContextTag: "Dietary Goal Solver",
    targetHeading: "Target-to-Meal Nutritional Optimizer",
    targetDesc: "Dial in your specific macronutrient boundaries. Our algorithm projects your nutritional targets to find matching real-world dishes.",
    presetGoalsLabel: "Dietary Presets:",
    lblCalories: "Caloric Energy",
    lblProtein: "Dietary Protein",
    lblCarbs: "Carbohydrates",
    lblFats: "Total Fats",
    lblSugar: "Free Sugar",
    lblSodium: "Sodium",
    lblFibre: "Dietary Fibre",
    btnFindMatches: "Solve Optimal Meal Candidates",
    targetMatchesHeading: "Optimized Meal Candidates",
    targetMatchesSub: "Dishes with closest vector proximity to your nutrient specifications",

    // Tab 3: Nutri-Grade AI
    gradeContextTag: "Health Diagnostic AI",
    gradeHeading: "Nutri-Grade Formulation Lab",
    gradeDesc: "Simulate custom nutritional formulations to assess clinical Nutri-Grades (A/B/C) with Random Forest intelligence and Atwater energy consistency validation.",
    gradeFormTitle: "Nutrient Composition Form",
    gradeFormDesc: "Enter limiting nutrients and macronutrients per 100g/serving.",
    gradePresetsLabel: "Test Benchmarks:",
    btnPredictGrade: "Run Nutri-Grade AI Prediction",
    readyToPredict: "Formulation Standby",
    readyToPredictSub: "Click 'Run Nutri-Grade AI Prediction' to calculate class probabilities and dietary guidance.",
    predictedGradeLabel: "Predicted Nutri-Grade",
    atwaterTitle: "Atwater Energy Balance",
    classProbabilities: "Classification Probability Breakdown",
    dietaryGuidanceTitle: "Nutritional Interpretation",

    // Tab 4: 2D PCA Map
    pcaContextTag: "Unsupervised Clustering & 2D Projection",
    pcaHeading: "2D Culinary Nutrition Landscape",
    pcaDesc: "11-dimensional nutritional vectors projected onto 2 principal components. Explore how recipes group into 5 distinct dietary clusters.",

    // Tab 5: Model Analytics
    evalContextTag: "Validation Benchmarks & Interpretability",
    evalHeading: "Machine Learning Model Performance",
    evalDesc: "Stratified held-out test evaluation benchmarks for the Random Forest Classifier, including confusion matrix and feature contribution analysis.",
    metricAccuracy: "Classification Accuracy",
    metricMacroF1: "Macro F1-Score",
    metricTestSamples: "Held-Out Test Sample",
    metricTrees: "Ensemble Estimators",
    metricAccSub: "Stratified 80/20 Test Split",
    metricF1Sub: "Unweighted Mean per Class",
    metricSampleSub: "Dishes Evaluated",
    metricTreesSub: "Gini Impurity Decision Trees",
    cmHeading: "Confusion Matrix",
    cmCaption: "Actual Ground-Truth versus Predicted Nutri-Grade",
    featImpHeading: "Nutrient Feature Importance",
    featImpCaption: "Gini impurity decrease across decision tree ensembles",

    // Tab 6: Dataset Explorer
    explorerContextTag: "Indexed Food Registry",
    explorerHeading: "Recipe Nutrition Catalog",
    explorerDesc: "Browse 1,014 authentic Indian culinary items with calculated NRF 5.3 Nutrient Density Scores and Nutri-Grades.",
    thDishName: "Recipe Name",
    thCategory: "Cluster Profile",
    thGrade: "Grade",
    thNRF: "NRF 5.3",
    thCalories: "Calories (kcal)",
    thProtein: "Protein (g)",
    thCarbs: "Carbs (g)",
    thFats: "Fats (g)",
    thSugar: "Sugar (g)",
    thSodium: "Sodium (mg)",
    btnPrev: "Previous",
    btnNext: "Next",

    // Modal
    modalCatalogTitle: "Recipe Catalog (1,014 Items)",
    modalCatalogSub: "Click any recipe to select it as reference and instantly calculate matches",
    btnClose: "Close Window"
  }
};

// ==========================================
// 2. APPLICATION STATE
// ==========================================
const state = {
  lang: 'th',
  theme: 'dark',
  currentTab: 'tab-search',
  status: null,
  radarChart: null,
  pcaChart: null,
  featImpChart: null,
  explorer: {
    query: '',
    category: '',
    grade: '',
    offset: 0,
    limit: 50,
    total: 0
  }
};

// ==========================================
// 3. INITIALIZATION & LIFECYCLE
// ==========================================
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initLanguage();
  initNavigation();
  initSearchTab();
  initTargetTab();
  initGradeTab();
  initPcaTab();
  initEvalTab();
  initExplorerTab();

  fetchSystemStatus();
});

// ==========================================
// 4. THEME & LANGUAGE CONTROLLERS
// ==========================================
function initTheme() {
  const savedTheme = localStorage.getItem('nutrisavor_theme') || 'dark';
  setTheme(savedTheme);

  document.getElementById('themeToggleBtn').addEventListener('click', () => {
    const nextTheme = state.theme === 'dark' ? 'light' : 'dark';
    setTheme(nextTheme);
  });
}

function setTheme(theme) {
  state.theme = theme;
  localStorage.setItem('nutrisavor_theme', theme);
  document.body.className = theme === 'dark' ? 'theme-dark' : 'theme-light';
  document.documentElement.setAttribute('data-theme', theme);

  if (state.radarChart) state.radarChart.update();
  if (state.pcaChart) state.pcaChart.update();
  if (state.featImpChart) state.featImpChart.update();
}

function initLanguage() {
  const savedLang = localStorage.getItem('nutrisavor_lang') || 'th';
  setLanguage(savedLang);

  document.querySelectorAll('.lang-option').forEach(btn => {
    btn.addEventListener('click', () => {
      setLanguage(btn.getAttribute('data-lang'));
    });
  });
}

function setLanguage(lang) {
  state.lang = lang;
  localStorage.setItem('nutrisavor_lang', lang);

  document.querySelectorAll('.lang-option').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
  });

  const dict = I18N[lang] || I18N.th;
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (dict[key]) {
      el.textContent = dict[key];
    }
  });

  updateTargetCalorieEstimate();
}

// ==========================================
// 5. NAVIGATION CONTROLLER
// ==========================================
function initNavigation() {
  document.querySelectorAll('.nav-item').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const targetBtn = e.target.closest('.nav-item') || btn;
      const tabId = targetBtn.getAttribute('data-tab');
      if (tabId) switchTab(tabId);
    });
  });
}

function switchTab(tabId) {
  state.currentTab = tabId;

  document.querySelectorAll('.nav-item').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('data-tab') === tabId);
  });

  document.querySelectorAll('.view-panel').forEach(pane => {
    pane.classList.toggle('active', pane.id === tabId);
  });

  window.scrollTo({ top: 0, behavior: 'instant' });

  if (tabId === 'tab-pca' && !state.pcaChart) {
    loadPcaClusterData();
  } else if (tabId === 'tab-eval' && !state.featImpChart) {
    loadEvaluationData();
  } else if (tabId === 'tab-explorer') {
    loadExplorerData();
  }
}

// ==========================================
// 6. REST API SERVICE LAYER
// ==========================================
async function apiGet(endpoint) {
  try {
    const res = await fetch(endpoint);
    return await res.json();
  } catch (err) {
    console.error(`API GET error on ${endpoint}:`, err);
    return { success: false, error: err.message };
  }
}

async function apiPost(endpoint, data) {
  try {
    const res = await fetch(endpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    return await res.json();
  } catch (err) {
    console.error(`API POST error on ${endpoint}:`, err);
    return { success: false, error: err.message };
  }
}

async function fetchSystemStatus() {
  const data = await apiGet('/api/status');
  if (data && data.status === 'ready') {
    state.status = data;
    const statusLabel = document.getElementById('statusLabel');
    statusLabel.textContent = `${data.dataset_count.toLocaleString()} Recipes · ${(data.model_accuracy * 100).toFixed(1)}% Acc`;
  }
}

// ==========================================
// 7. TAB 1: DISH-TO-DISH SEARCH
// ==========================================
function initSearchTab() {
  const input = document.getElementById('dishSearchInput');
  const clearBtn = document.getElementById('clearSearchBtn');
  const searchBtn = document.getElementById('executeSearchBtn');

  searchBtn.addEventListener('click', () => {
    const query = input.value.trim();
    if (query) executeDishSearch(query);
  });

  input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
      const query = input.value.trim();
      if (query) executeDishSearch(query);
    }
  });

  clearBtn.addEventListener('click', () => {
    input.value = '';
    input.focus();
  });

  document.querySelectorAll('.discovery-chip[data-dish]').forEach(chip => {
    chip.addEventListener('click', (e) => {
      const targetChip = e.target.closest('.discovery-chip') || chip;
      const dish = targetChip.getAttribute('data-dish');
      if (dish) {
        input.value = dish;
        executeDishSearch(dish);
      }
    });
  });

  initCatalogModal();
}

// Global state for catalog modal
let allCatalogDishes = [];
let selectedModalCategory = '';

async function initCatalogModal() {
  const modalOverlay = document.getElementById('catalogModalOverlay');
  const openBtn = document.getElementById('openCatalogModalBtn');
  const closeBtn = document.getElementById('closeCatalogModalBtn');
  const dismissBtn = document.getElementById('modalDismissBtn');
  const searchInput = document.getElementById('modalDishSearchInput');

  if (!modalOverlay || !openBtn) return;

  const openModal = async () => {
    modalOverlay.style.display = 'flex';
    document.body.style.overflow = 'hidden';
    if (allCatalogDishes.length === 0) {
      await loadAllCatalogDishes();
    } else {
      renderModalDishes();
    }
    if (searchInput) {
      searchInput.value = '';
      searchInput.focus();
    }
  };

  const closeModal = () => {
    modalOverlay.style.display = 'none';
    document.body.style.overflow = '';
  };

  openBtn.addEventListener('click', openModal);
  if (closeBtn) closeBtn.addEventListener('click', closeModal);
  if (dismissBtn) dismissBtn.addEventListener('click', closeModal);

  modalOverlay.addEventListener('click', (e) => {
    if (e.target === modalOverlay) closeModal();
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modalOverlay.style.display === 'flex') {
      closeModal();
    }
  });

  if (searchInput) {
    searchInput.addEventListener('input', () => {
      renderModalDishes();
    });
  }
}

async function loadAllCatalogDishes() {
  const grid = document.getElementById('modalDishesGrid');
  if (grid) grid.innerHTML = '<div style="grid-column: 1 / -1; padding: 2.5rem; text-align: center; color: var(--text-muted); font-size: 0.9rem;">Loading recipe database...</div>';

  const [dishRes, clusterRes] = await Promise.all([
    apiGet('/api/dishes?limit=1200'),
    apiGet('/api/clusters')
  ]);

  if (dishRes && dishRes.dishes) {
    allCatalogDishes = dishRes.dishes;
  }

  // Populate category filter pills
  const pillsContainer = document.getElementById('modalCategoryFilterPills');
  if (pillsContainer && clusterRes && clusterRes.clusters) {
    pillsContainer.innerHTML = '<button class="modal-cat-pill active" data-cat="">All Categories</button>';
    clusterRes.clusters.forEach(c => {
      const cleanName = c.name.replace(/^[^\w\s]+/, '').trim();
      const btn = document.createElement('button');
      btn.className = 'modal-cat-pill';
      btn.setAttribute('data-cat', c.name);
      btn.textContent = cleanName;
      btn.addEventListener('click', () => {
        pillsContainer.querySelectorAll('.modal-cat-pill').forEach(p => p.classList.remove('active'));
        btn.classList.add('active');
        selectedModalCategory = c.name;
        renderModalDishes();
      });
      pillsContainer.appendChild(btn);
    });

    pillsContainer.querySelector('.modal-cat-pill[data-cat=""]').addEventListener('click', (e) => {
      pillsContainer.querySelectorAll('.modal-cat-pill').forEach(p => p.classList.remove('active'));
      e.target.classList.add('active');
      selectedModalCategory = '';
      renderModalDishes();
    });
  }

  renderModalDishes();
}

function renderModalDishes() {
  const grid = document.getElementById('modalDishesGrid');
  const countText = document.getElementById('modalItemCountText');
  const searchInput = document.getElementById('modalDishSearchInput');
  const modalOverlay = document.getElementById('catalogModalOverlay');

  if (!grid) return;

  const query = (searchInput?.value || '').toLowerCase().trim();
  const filtered = allCatalogDishes.filter(d => {
    const matchesQuery = !query || d.name.toLowerCase().includes(query);
    const matchesCat = !selectedModalCategory || d.category === selectedModalCategory;
    return matchesQuery && matchesCat;
  });

  if (countText) {
    countText.textContent = state.lang === 'th'
      ? `แสดง ${filtered.length.toLocaleString()} จาก ${allCatalogDishes.length.toLocaleString()} รายการ`
      : `Showing ${filtered.length.toLocaleString()} of ${allCatalogDishes.length.toLocaleString()} dishes`;
  }

  if (filtered.length === 0) {
    grid.innerHTML = '<div style="grid-column: 1 / -1; padding: 3rem; text-align: center; color: var(--text-dim); font-size: 0.9rem;">No matching dishes found.</div>';
    return;
  }

  grid.innerHTML = '';
  filtered.forEach(dish => {
    const card = document.createElement('div');
    card.className = 'modal-dish-item';

    const gradeClass = getGradeClass(dish.grade);
    const cleanCat = dish.category ? dish.category.replace(/^[^\w\s]+/, '').trim() : 'Balanced Recipe';

    card.innerHTML = `
      <div class="modal-dish-top">
        <div>
          <h5 class="modal-dish-name">${escapeHtml(dish.name)}</h5>
          <span class="modal-dish-cat">${escapeHtml(cleanCat)}</span>
        </div>
        <span class="clinical-grade-badge ${gradeClass}">${escapeHtml(dish.grade)}</span>
      </div>
      <div class="modal-dish-meta">
        <span>NRF 5.3: <strong class="text-emerald font-numeric">${dish.health_score}</strong></span>
        <span><strong>${dish.calories}</strong> kcal · <strong>${dish.protein}g</strong> prot</span>
      </div>
    `;

    card.addEventListener('click', () => {
      if (modalOverlay) modalOverlay.style.display = 'none';
      document.body.style.overflow = '';

      const searchInput = document.getElementById('dishSearchInput');
      if (searchInput) searchInput.value = dish.name;
      executeDishSearch(dish.name);

      const resultsSection = document.getElementById('searchResultsSection');
      if (resultsSection) {
        resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });

    grid.appendChild(card);
  });
}

async function executeDishSearch(dishName) {
  const topK = document.getElementById('searchTopKSelect').value || 5;
  const resultsContainer = document.getElementById('searchResultsSection');

  const res = await apiGet(`/api/recommend/dish?name=${encodeURIComponent(dishName)}&k=${topK}`);
  if (!res.success) {
    alert(res.error || 'Dish not found in database');
    return;
  }

  resultsContainer.style.display = 'grid';
  renderTargetDish(res.target_dish);
  renderRecommendations(res.recommendations, 'recommendationsCardsGrid', 'recsCountBubble');
  renderRadarChart(res.target_dish, res.recommendations);

  resultsContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function renderTargetDish(dish) {
  document.getElementById('targetDishTitle').textContent = dish.name;
  document.getElementById('targetHealthScore').textContent = dish.health_score;
  document.getElementById('targetCalories').textContent = `${dish.calories} kcal`;
  document.getElementById('targetProtein').textContent = `${dish.protein} g`;
  document.getElementById('targetCarbs').textContent = `${dish.carbs} g`;
  document.getElementById('targetFats').textContent = `${dish.fats} g`;

  const gradeBadge = document.getElementById('targetDishGrade');
  gradeBadge.textContent = dish.grade;
  gradeBadge.className = 'clinical-grade-badge ' + getGradeClass(dish.grade);

  // Update Macro Calorie Ratio Stacked Bar
  const protCal = (dish.protein || 0) * 4;
  const carbCal = (dish.carbs || 0) * 4;
  const fatCal = (dish.fats || 0) * 9;
  const totalCal = Math.max(1, protCal + carbCal + fatCal);

  const pctProt = Math.round((protCal / totalCal) * 100);
  const pctCarb = Math.round((carbCal / totalCal) * 100);
  const pctFat = Math.max(0, 100 - pctProt - pctCarb);

  const bar = document.getElementById('targetMacroBar');
  if (bar) {
    bar.innerHTML = `
      <div class="macro-seg seg-protein" style="width: ${pctProt}%;" title="Protein: ${pctProt}% (${dish.protein}g)"></div>
      <div class="macro-seg seg-carbs" style="width: ${pctCarb}%;" title="Carbs: ${pctCarb}% (${dish.carbs}g)"></div>
      <div class="macro-seg seg-fats" style="width: ${pctFat}%;" title="Fats: ${pctFat}% (${dish.fats}g)"></div>
    `;
  }
}

function renderRecommendations(recs, gridId, countId) {
  const grid = document.getElementById(gridId);
  const countBubble = document.getElementById(countId);

  if (countBubble) countBubble.textContent = recs.length;
  grid.innerHTML = '';

  recs.forEach(dish => {
    const card = document.createElement('div');
    card.className = 'candidate-match-card';

    const gradeClass = getGradeClass(dish.grade);
    const matchPct = dish.match_pct || 0;

    let tagBadgesHtml = '';
    if (dish.tags?.high_protein) tagBadgesHtml += `<span class="badge-tag badge-high-protein">High Protein</span>`;
    if (dish.tags?.low_carb) tagBadgesHtml += `<span class="badge-tag badge-low-carb">Low Carb</span>`;
    if (dish.tags?.low_calorie) tagBadgesHtml += `<span class="badge-tag badge-low-calorie">Low Calorie</span>`;

    const cleanCategory = dish.category ? dish.category.replace(/^[^\w\s]+/, '').trim() : 'Balanced Recipe';

    // Calorie split
    const pCal = (dish.protein || 0) * 4;
    const cCal = (dish.carbs || 0) * 4;
    const fCal = (dish.fats || 0) * 9;
    const tCal = Math.max(1, pCal + cCal + fCal);
    const pPct = Math.round((pCal / tCal) * 100);
    const cPct = Math.round((cCal / tCal) * 100);
    const fPct = Math.max(0, 100 - pPct - cPct);

    card.innerHTML = `
      <div class="card-upper-row">
        <div>
          <h4 class="candidate-name">${escapeHtml(dish.name)}</h4>
          <span class="candidate-cluster">${escapeHtml(cleanCategory)}</span>
        </div>
        <span class="clinical-grade-badge ${gradeClass}">${escapeHtml(dish.grade)}</span>
      </div>

      <div class="similarity-bar-wrap">
        <div class="bar-meta-row">
          <span>Nutritional Match</span>
          <span class="font-numeric text-emerald">${matchPct.toFixed(1)}%</span>
        </div>
        <div class="bar-track">
          <div class="bar-progress" style="width: ${Math.min(100, Math.max(6, matchPct))}%;"></div>
        </div>
      </div>

      <div class="nutrients-inline-grid">
        <div>
          <div class="nutri-lbl">NRF 5.3</div>
          <div class="nutri-num text-emerald">${dish.health_score}</div>
        </div>
        <div>
          <div class="nutri-lbl">Calories</div>
          <div class="nutri-num">${dish.calories}</div>
        </div>
        <div>
          <div class="nutri-lbl">Protein</div>
          <div class="nutri-num">${dish.protein}g</div>
        </div>
        <div>
          <div class="nutri-lbl">Carb/Fat</div>
          <div class="nutri-num">${dish.carbs}g / ${dish.fats}g</div>
        </div>
      </div>

      <div class="stacked-macro-bar" style="height: 6px;">
        <div class="macro-seg seg-protein" style="width: ${pPct}%;" title="Protein: ${pPct}%"></div>
        <div class="macro-seg seg-carbs" style="width: ${cPct}%;" title="Carbs: ${cPct}%"></div>
        <div class="macro-seg seg-fats" style="width: ${fPct}%;" title="Fats: ${fPct}%"></div>
      </div>

      <div class="candidate-actions-row">
        <div class="clinical-tags-row">
          ${tagBadgesHtml}
        </div>
        <button class="btn-chain-search" title="Inspect this recipe as baseline">
          <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
          <span>Explore</span>
        </button>
      </div>
    `;

    // Chain search button click
    const exploreBtn = card.querySelector('.btn-chain-search');
    if (exploreBtn) {
      exploreBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        const input = document.getElementById('dishSearchInput');
        if (input) input.value = dish.name;
        executeDishSearch(dish.name);
      });
    }

    grid.appendChild(card);
  });
}

function renderRadarChart(targetDish, recs) {
  const canvas = document.getElementById('dishRadarChart');
  if (!canvas) return;

  if (state.radarChart) {
    state.radarChart.destroy();
  }

  const labels = ['Protein %DV', 'Fibre %DV', 'Vit C %DV', 'Calcium %DV', 'Iron %DV', 'Sugar %DV', 'Fat %DV', 'Sodium %DV'];

  const computeDvProfile = (d) => [
    Math.min(150, (d.protein / 50) * 100),
    Math.min(150, (d.fibre / 28) * 100),
    Math.min(150, ((d.vitamin_c || 0) / 90) * 100),
    Math.min(150, ((d.calcium || 0) / 1300) * 100),
    Math.min(150, ((d.iron || 0) / 18) * 100),
    Math.min(150, (d.sugar / 50) * 100),
    Math.min(150, (d.fats / 78) * 100),
    Math.min(150, (d.sodium / 2300) * 100)
  ];

  const datasets = [
    {
      label: `Reference: ${targetDish.name}`,
      data: computeDvProfile(targetDish),
      backgroundColor: 'rgba(59, 130, 246, 0.18)',
      borderColor: '#3b82f6',
      borderWidth: 2,
      pointBackgroundColor: '#3b82f6',
      pointRadius: 3
    }
  ];

  if (recs && recs.length > 0) {
    const topRec = recs[0];
    datasets.push({
      label: `Top Match: ${topRec.name}`,
      data: computeDvProfile(topRec),
      backgroundColor: 'rgba(22, 163, 74, 0.22)',
      borderColor: '#16a34a',
      borderWidth: 2,
      pointBackgroundColor: '#16a34a',
      pointRadius: 3
    });
  }

  const isDark = state.theme === 'dark';
  const gridColor = isDark ? 'rgba(255, 255, 255, 0.08)' : 'rgba(0, 0, 0, 0.08)';
  const textColor = isDark ? '#94a3b8' : '#475569';

  state.radarChart = new Chart(canvas, {
    type: 'radar',
    data: { labels, datasets },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        r: {
          grid: { color: gridColor },
          angleLines: { color: gridColor },
          pointLabels: { color: textColor, font: { family: 'Plus Jakarta Sans', size: 10, weight: '600' } },
          ticks: { display: false, max: 150 }
        }
      },
      plugins: {
        legend: {
          labels: { color: textColor, font: { family: 'Plus Jakarta Sans', size: 11, weight: '700' } }
        }
      }
    }
  });
}

// ==========================================
// 8. TAB 2: TARGET GOALS OPTIMIZER
// ==========================================
function initTargetTab() {
  const sliders = [
    { id: 'targetCaloriesInput', valId: 'valCalories' },
    { id: 'targetProteinInput', valId: 'valProtein' },
    { id: 'targetCarbsInput', valId: 'valCarbs' },
    { id: 'targetFatsInput', valId: 'valFats' },
    { id: 'targetSugarInput', valId: 'valSugar' },
    { id: 'targetSodiumInput', valId: 'valSodium' }
  ];

  sliders.forEach(s => {
    const input = document.getElementById(s.id);
    const valSpan = document.getElementById(s.valId);
    input.addEventListener('input', () => {
      valSpan.textContent = input.value;
      updateTargetCalorieEstimate();
    });
  });

  const presets = {
    'clean-bulk': { cal: 350, prot: 35, carb: 25, fat: 8, sugar: 3, sod: 350 },
    'keto': { cal: 300, prot: 25, carb: 5, fat: 22, sugar: 1, sod: 400 },
    'weight-loss': { cal: 130, prot: 16, carb: 8, fat: 2, sugar: 1, sod: 200 },
    'low-sodium': { cal: 180, prot: 12, carb: 25, fat: 5, sugar: 2, sod: 80 }
  };

  document.querySelectorAll('.clinical-preset-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const targetBtn = e.target.closest('.clinical-preset-btn') || btn;
      document.querySelectorAll('.clinical-preset-btn').forEach(b => b.classList.remove('active'));
      targetBtn.classList.add('active');

      const g = presets[targetBtn.getAttribute('data-goal')];
      if (!g) return;

      document.getElementById('targetCaloriesInput').value = g.cal;
      document.getElementById('valCalories').textContent = g.cal;
      document.getElementById('targetProteinInput').value = g.prot;
      document.getElementById('valProtein').textContent = g.prot;
      document.getElementById('targetCarbsInput').value = g.carb;
      document.getElementById('valCarbs').textContent = g.carb;
      document.getElementById('targetFatsInput').value = g.fat;
      document.getElementById('valFats').textContent = g.fat;
      document.getElementById('targetSugarInput').value = g.sugar;
      document.getElementById('valSugar').textContent = g.sugar;
      document.getElementById('targetSodiumInput').value = g.sod;
      document.getElementById('valSodium').textContent = g.sod;

      updateTargetCalorieEstimate();
      executeTargetSearch();
    });
  });

  document.getElementById('executeTargetSearchBtn').addEventListener('click', executeTargetSearch);
  updateTargetCalorieEstimate();
}

function updateTargetCalorieEstimate() {
  const prot = parseFloat(document.getElementById('targetProteinInput')?.value || 0);
  const carb = parseFloat(document.getElementById('targetCarbsInput')?.value || 0);
  const fat = parseFloat(document.getElementById('targetFatsInput')?.value || 0);
  const estimated = Math.round(prot * 4 + carb * 4 + fat * 9);

  const hintEl = document.getElementById('targetMacroHintText');
  if (hintEl) {
    hintEl.textContent = state.lang === 'th'
      ? `การประมาณการพลังงาน: ~${estimated} kcal (คำนวณจาก Atwater Factor: โปรตีน×4 + คาร์บ×4 + ไขมัน×9)`
      : `Macro Energy Estimate: ~${estimated} kcal based on Atwater split (Protein×4 + Carbs×4 + Fats×9).`;
  }
}

async function executeTargetSearch() {
  const targetData = {
    Calories: parseFloat(document.getElementById('targetCaloriesInput').value),
    Protein: parseFloat(document.getElementById('targetProteinInput').value),
    Carbohydrates: parseFloat(document.getElementById('targetCarbsInput').value),
    Fats: parseFloat(document.getElementById('targetFatsInput').value),
    'Free Sugar': parseFloat(document.getElementById('targetSugarInput').value),
    Sodium: parseFloat(document.getElementById('targetSodiumInput').value),
    k: 6
  };

  const resultsSection = document.getElementById('targetResultsSection');
  const res = await apiPost('/api/recommend/target', targetData);

  if (!res.success) {
    alert(res.error || 'Optimization solver failed');
    return;
  }

  resultsSection.style.display = 'block';
  renderRecommendations(res.recommendations, 'targetCardsGrid', 'targetCountBubble');
  resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// ==========================================
// 9. TAB 3: NUTRI-GRADE AI CLASSIFIER
// ==========================================
function initGradeTab() {
  const sugarInput = document.getElementById('gradeSugarInput');
  const fatInput = document.getElementById('gradeFatInput');
  const sodiumInput = document.getElementById('gradeSodiumInput');
  const proteinInput = document.getElementById('gradeProteinInput');
  const carbInput = document.getElementById('gradeCarbInput');
  const fiberInput = document.getElementById('gradeFiberInput');

  document.getElementById('presetHealthy').addEventListener('click', () => {
    sugarInput.value = '1.5'; fatInput.value = '3.0'; sodiumInput.value = '120';
    proteinInput.value = '22.0'; carbInput.value = '8.0'; fiberInput.value = '4.0';
    executeGradePrediction();
  });

  document.getElementById('presetModerate').addEventListener('click', () => {
    sugarInput.value = '8.0'; fatInput.value = '12.0'; sodiumInput.value = '450';
    proteinInput.value = '12.0'; carbInput.value = '25.0'; fiberInput.value = '2.5';
    executeGradePrediction();
  });

  document.getElementById('presetSweet').addEventListener('click', () => {
    sugarInput.value = '28.0'; fatInput.value = '14.0'; sodiumInput.value = '90';
    proteinInput.value = '4.0'; carbInput.value = '55.0'; fiberInput.value = '0.5';
    executeGradePrediction();
  });

  document.getElementById('presetFatty').addEventListener('click', () => {
    sugarInput.value = '2.0'; fatInput.value = '32.0'; sodiumInput.value = '750';
    proteinInput.value = '18.0'; carbInput.value = '10.0'; fiberInput.value = '1.0';
    executeGradePrediction();
  });

  document.getElementById('executeGradePredictBtn').addEventListener('click', executeGradePrediction);
}

async function executeGradePrediction() {
  const payload = {
    sugar: parseFloat(document.getElementById('gradeSugarInput').value || 0),
    fat: parseFloat(document.getElementById('gradeFatInput').value || 0),
    sodium: parseFloat(document.getElementById('gradeSodiumInput').value || 0),
    protein: parseFloat(document.getElementById('gradeProteinInput').value || 0),
    carb: parseFloat(document.getElementById('gradeCarbInput').value || 0),
    fiber: parseFloat(document.getElementById('gradeFiberInput').value || 0)
  };

  const res = await apiPost('/api/grade/predict', payload);
  if (!res.success) {
    alert(res.error || 'Prediction calculation failed');
    return;
  }

  document.getElementById('gradePlaceholder').style.display = 'none';
  document.getElementById('gradeActiveDisplay').style.display = 'block';

  const gradeCircle = document.getElementById('gradeCircle');
  const gradeTitle = document.getElementById('gradeTitle');
  const gradeConfidencePill = document.getElementById('gradeConfidencePill');
  const atwaterDesc = document.getElementById('atwaterDesc');
  const adviceText = document.getElementById('adviceText');

  const gradeLetter = res.grade.charAt(0);
  gradeCircle.textContent = gradeLetter;
  gradeCircle.className = 'grade-badge-circle circle-' + gradeLetter.toLowerCase();
  gradeTitle.textContent = res.grade;
  gradeConfidencePill.textContent = `Confidence: ${(res.confidence * 100).toFixed(1)}%`;

  atwaterDesc.innerHTML = state.lang === 'th'
    ? `ความหนาแน่นพลังงานที่คำนวณได้: <strong>${res.estimated_calories} kcal</strong> (สูตร Atwater: ไขมัน×9 + โปรตีน×4 + คาร์บ×4)`
    : `Calculated caloric density: <strong>${res.estimated_calories} kcal</strong> (Atwater: Fat×9 + Prot×4 + Carb×4).`;

  const probs = res.probabilities || {};
  const probA = (probs['A (Healthy)'] || 0) * 100;
  const probB = (probs['B (Moderate)'] || 0) * 100;
  const probC = (probs['C (Limit)'] || 0) * 100;

  document.getElementById('probBarA').style.width = `${probA}%`;
  document.getElementById('probPctA').textContent = `${probA.toFixed(1)}%`;
  document.getElementById('probBarB').style.width = `${probB}%`;
  document.getElementById('probPctB').textContent = `${probB.toFixed(1)}%`;
  document.getElementById('probBarC').style.width = `${probC}%`;
  document.getElementById('probPctC').textContent = `${probC.toFixed(1)}%`;

  if (gradeLetter === 'A') {
    adviceText.textContent = state.lang === 'th'
      ? 'เกณฑ์สุขภาพดีเยี่ยม: ปริมาณน้ำตาล ไขมัน และโซเดียมอยู่ในระดับปลอดภัยต่อสุขภาพ เหมาะสำหรับเป็นอาหารจานหลักในทุกวัน'
      : 'Optimal nutritional profile: Low sugar, balanced lipid profile, and controlled sodium load. Excellent for daily consumption.';
  } else if (gradeLetter === 'B') {
    adviceText.textContent = state.lang === 'th'
      ? 'เกณฑ์สุขภาพระดับปานกลาง: สารอาหารอยู่ในระดับมาตรฐานทั่วไป แนะนำให้ทานร่วมกับอาหารที่มีใยอาหารหรือผักเพิ่มขึ้น'
      : 'Moderate nutritional balance: Meets general dietary requirements. Pair with high-fiber sides to improve overall balance.';
  } else {
    adviceText.textContent = state.lang === 'th'
      ? 'ควรจำกัดปริมาณ: มีน้ำตาล (>15g), ไขมัน (>20g) หรือโซเดียม (>600mg) เกินเกณฑ์สุขภาพ แนะนำให้แบ่งทานหรือทานเป็นครั้งคราว'
      : 'Dietary caution: Elevated free sugar (>15g), fats (>20g), or sodium (>600mg). Recommended for occasional or portion-controlled intake.';
  }
}

// ==========================================
// 10. TAB 4: 2D PCA CLUSTERS MAP
// ==========================================
function initPcaTab() {}

async function loadPcaClusterData() {
  const data = await apiGet('/api/clusters');
  if (!data || !data.clusters) return;

  renderPcaScatterChart(data);
  renderClusterCards(data.clusters);
}

function renderPcaScatterChart(data) {
  const canvas = document.getElementById('pcaScatterChart');
  if (!canvas) return;

  if (state.pcaChart) state.pcaChart.destroy();

  const clusterDatasets = data.clusters.map(c => {
    const cleanClusterName = c.name.replace(/^[^\w\s]+/, '').trim();
    const pts = data.points.filter(p => p.cluster_id === c.id).map(p => ({
      x: p.x,
      y: p.y,
      dishName: p.name,
      category: cleanClusterName,
      healthScore: p.health_score,
      calories: p.calories,
      protein: p.protein,
      grade: p.grade
    }));

    return {
      label: cleanClusterName,
      data: pts,
      backgroundColor: c.color,
      borderColor: 'transparent',
      pointRadius: 4,
      pointHoverRadius: 7
    };
  });

  const isDark = state.theme === 'dark';
  const gridColor = isDark ? 'rgba(255, 255, 255, 0.06)' : 'rgba(0, 0, 0, 0.06)';
  const textColor = isDark ? '#94a3b8' : '#475569';

  state.pcaChart = new Chart(canvas, {
    type: 'scatter',
    data: { datasets: clusterDatasets },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        x: {
          grid: { color: gridColor },
          title: { display: true, text: 'Principal Component 1 (Energy & Protein Density)', color: textColor, font: { family: 'Plus Jakarta Sans', size: 11, weight: '600' } }
        },
        y: {
          grid: { color: gridColor },
          title: { display: true, text: 'Principal Component 2 (Micronutrients & Lipid/Sugar Ratio)', color: textColor, font: { family: 'Plus Jakarta Sans', size: 11, weight: '600' } }
        }
      },
      plugins: {
        legend: {
          labels: { color: textColor, font: { family: 'Plus Jakarta Sans', size: 11, weight: '700' } }
        },
        tooltip: {
          callbacks: {
            label: (ctx) => {
              const raw = ctx.raw;
              return `${raw.dishName} | ${raw.calories} kcal | Prot: ${raw.protein}g | NRF: ${raw.healthScore}`;
            }
          }
        }
      }
    }
  });
}

function renderClusterCards(clusters) {
  const grid = document.getElementById('clusterStatsGrid');
  const pillsContainer = document.getElementById('clusterLegendPills');

  pillsContainer.innerHTML = '';
  grid.innerHTML = '';

  clusters.forEach(c => {
    const cleanName = c.name.replace(/^[^\w\s]+/, '').trim();

    // Legend Pill
    const pill = document.createElement('span');
    pill.className = 'cluster-badge-tag';
    pill.style.background = `${c.color}1a`;
    pill.style.borderColor = c.color;
    pill.style.color = c.color;
    pill.textContent = `${cleanName} (${c.count})`;
    pillsContainer.appendChild(pill);

    // Bento Card
    const card = document.createElement('div');
    card.className = 'cluster-summary-card';
    card.style.borderLeft = `3px solid ${c.color}`;
    card.innerHTML = `
      <div class="cluster-card-head">
        <span class="cluster-card-name" style="color: ${c.color};">${escapeHtml(cleanName)}</span>
        <span class="cluster-card-count">${c.count} recipes</span>
      </div>
      <div class="nutrients-inline-grid">
        <div><div class="nutri-lbl">Avg Cal</div><div class="nutri-num">${c.avg_nutrients.calories}</div></div>
        <div><div class="nutri-lbl">Avg Prot</div><div class="nutri-num">${c.avg_nutrients.protein}g</div></div>
        <div><div class="nutri-lbl">Avg Fat</div><div class="nutri-num">${c.avg_nutrients.fats}g</div></div>
        <div><div class="nutri-lbl">NRF 5.3</div><div class="nutri-num text-emerald">${c.avg_nutrients.health_score}</div></div>
      </div>
    `;
    grid.appendChild(card);
  });
}

// ==========================================
// 11. TAB 5: ML EVALUATION & ANALYTICS
// ==========================================
function initEvalTab() {}

async function loadEvaluationData() {
  const data = await apiGet('/api/evaluation');
  if (!data || !data.confusion_matrix) return;

  document.getElementById('evalAccuracy').textContent = `${(data.accuracy * 100).toFixed(1)}%`;
  document.getElementById('evalMacroF1').textContent = data.macro_f1;
  document.getElementById('evalTestCount').textContent = data.test_sample_count;

  renderConfusionMatrix(data.confusion_matrix);
  renderFeatureImportanceChart(data.feature_importances);
}

function renderConfusionMatrix(cm) {
  const container = document.getElementById('cmTableContainer');
  const labels = cm.labels || ['A (Healthy)', 'B (Moderate)', 'C (Limit)'];
  const matrix = cm.matrix;

  let tableHtml = `
    <table class="cm-grid-table">
      <thead>
        <tr>
          <th>Actual \\ Predicted</th>
          ${labels.map(l => `<th>Pred ${escapeHtml(l.split(' ')[0])}</th>`).join('')}
        </tr>
      </thead>
      <tbody>
  `;

  for (let i = 0; i < labels.length; i++) {
    tableHtml += `<tr><th>Actual ${escapeHtml(labels[i].split(' ')[0])}</th>`;
    for (let j = 0; j < labels.length; j++) {
      const val = matrix[i] ? matrix[i][j] : 0;
      const isDiag = (i === j);
      tableHtml += `<td class="${isDiag ? 'cm-diag' : 'cm-off'}">${val}</td>`;
    }
    tableHtml += `</tr>`;
  }
  tableHtml += `</tbody></table>`;
  container.innerHTML = tableHtml;
}

function renderFeatureImportanceChart(importances) {
  const canvas = document.getElementById('featureImpChart');
  if (!canvas) return;

  if (state.featImpChart) state.featImpChart.destroy();

  const labels = importances.map(item => item.feature);
  const values = importances.map(item => item.importance);

  const isDark = state.theme === 'dark';
  const textColor = isDark ? '#94a3b8' : '#475569';
  const gridColor = isDark ? 'rgba(255, 255, 255, 0.06)' : 'rgba(0, 0, 0, 0.06)';

  state.featImpChart = new Chart(canvas, {
    type: 'bar',
    data: {
      labels,
      datasets: [{
        data: values,
        backgroundColor: '#16a34a',
        borderRadius: 5
      }]
    },
    options: {
      indexAxis: 'y',
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        x: { grid: { color: gridColor }, ticks: { color: textColor, font: { family: 'Plus Jakarta Sans', size: 10 } } },
        y: { grid: { display: false }, ticks: { color: textColor, font: { family: 'Plus Jakarta Sans', size: 11, weight: '600' } } }
      },
      plugins: {
        legend: { display: false }
      }
    }
  });
}

// ==========================================
// 12. TAB 6: DATASET EXPLORER
// ==========================================
function initExplorerTab() {
  const searchInput = document.getElementById('explorerSearchInput');
  const catFilter = document.getElementById('explorerCategoryFilter');
  const gradeFilter = document.getElementById('explorerGradeFilter');
  const prevBtn = document.getElementById('prevPageBtn');
  const nextBtn = document.getElementById('nextPageBtn');

  searchInput.addEventListener('input', () => {
    state.explorer.query = searchInput.value;
    state.explorer.offset = 0;
    loadExplorerData();
  });

  catFilter.addEventListener('change', () => {
    state.explorer.category = catFilter.value;
    state.explorer.offset = 0;
    loadExplorerData();
  });

  gradeFilter.addEventListener('change', () => {
    state.explorer.grade = gradeFilter.value;
    state.explorer.offset = 0;
    loadExplorerData();
  });

  prevBtn.addEventListener('click', () => {
    if (state.explorer.offset > 0) {
      state.explorer.offset -= state.explorer.limit;
      loadExplorerData();
    }
  });

  nextBtn.addEventListener('click', () => {
    if (state.explorer.offset + state.explorer.limit < state.explorer.total) {
      state.explorer.offset += state.explorer.limit;
      loadExplorerData();
    }
  });
}

async function loadExplorerData() {
  const catFilter = document.getElementById('explorerCategoryFilter');
  if (catFilter && catFilter.options.length <= 1) {
    const clusterRes = await apiGet('/api/clusters');
    if (clusterRes && clusterRes.clusters) {
      clusterRes.clusters.forEach(c => {
        const cleanName = c.name.replace(/^[^\w\s]+/, '').trim();
        const opt = document.createElement('option');
        opt.value = c.name;
        opt.textContent = cleanName;
        catFilter.appendChild(opt);
      });
    }
  }

  const { query, category, grade, offset, limit } = state.explorer;
  const endpoint = `/api/dishes?q=${encodeURIComponent(query)}&category=${encodeURIComponent(category)}&grade=${encodeURIComponent(grade)}&offset=${offset}&limit=${limit}`;

  const res = await apiGet(endpoint);
  if (!res || !res.dishes) return;

  state.explorer.total = res.total;
  renderExplorerTable(res.dishes, res.total, offset, limit);
}

function renderExplorerTable(dishes, total, offset, limit) {
  const tbody = document.getElementById('explorerTableBody');
  const pageInfo = document.getElementById('explorerPageInfo');
  const prevBtn = document.getElementById('prevPageBtn');
  const nextBtn = document.getElementById('nextPageBtn');

  tbody.innerHTML = '';

  dishes.forEach((d, idx) => {
    const tr = document.createElement('tr');
    const gradeClass = getGradeClass(d.grade);
    const cleanCat = d.category ? d.category.replace(/^[^\w\s]+/, '').trim() : 'Balanced Recipe';

    tr.innerHTML = `
      <td class="font-numeric text-dim">${offset + idx + 1}</td>
      <td><strong>${escapeHtml(d.name)}</strong></td>
      <td>${escapeHtml(cleanCat)}</td>
      <td><span class="clinical-grade-badge ${gradeClass}">${escapeHtml(d.grade)}</span></td>
      <td class="text-emerald font-numeric">${d.health_score}</td>
      <td class="font-numeric">${d.calories}</td>
      <td class="font-numeric">${d.protein}</td>
      <td class="font-numeric">${d.carbs}</td>
      <td class="font-numeric">${d.fats}</td>
      <td class="font-numeric">${d.sugar}</td>
      <td class="font-numeric">${d.sodium}</td>
    `;

    // Row click selects recipe in similarity tab
    tr.style.cursor = 'pointer';
    tr.title = 'Click to compute similarity';
    tr.addEventListener('click', () => {
      switchTab('tab-search');
      const searchInput = document.getElementById('dishSearchInput');
      if (searchInput) searchInput.value = d.name;
      executeDishSearch(d.name);
    });

    tbody.appendChild(tr);
  });

  const start = total > 0 ? offset + 1 : 0;
  const end = Math.min(total, offset + limit);
  pageInfo.textContent = state.lang === 'th'
    ? `แสดง ${start} - ${end} จาก ${total.toLocaleString()} รายการ`
    : `Displaying ${start} - ${end} of ${total.toLocaleString()} records`;

  prevBtn.disabled = offset <= 0;
  nextBtn.disabled = end >= total;
}

// ==========================================
// 13. UTILITY HELPERS
// ==========================================
function getGradeClass(gradeStr) {
  if (!gradeStr) return 'grade-b';
  if (gradeStr.startsWith('A')) return 'grade-a';
  if (gradeStr.startsWith('C')) return 'grade-c';
  return 'grade-b';
}

function escapeHtml(text) {
  if (typeof text !== 'string') return text;
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}
